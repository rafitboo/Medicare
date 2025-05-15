import pytest
from flask import url_for
from app import create_app, db
from app.models.customer import Customer
from app.models.medicine import Medicine
from app.models.user import User
from app.models.cart import Cart
from app.models.order import Order
from app.models.category import Category
from app.models.admin import Admin
import uuid
from sqlalchemy.orm import joinedload
from sqlalchemy import text
from datetime import datetime, timedelta

@pytest.fixture(scope='function')
def app():
    """Create test app"""
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'WTF_CSRF_ENABLED': False,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })
    return app

@pytest.fixture(scope='function')
def _db(app):
    with app.app_context():
        db.create_all()
        yield db
        db.session.rollback()
        db.session.remove()


@pytest.fixture(scope='function')
def auth_customer(_db):
    unique_id = str(uuid.uuid4())[:8]
    user, error = User.signup(
        username=f'testuser_{unique_id}',
        email=f'test_{unique_id}@example.com',
        phone='1234567890',
        password='password123',
        confirm_password='password123',
        terms=True,
        role='customer',
        type='customer'
    )
    
    if error:
        raise Exception(f"Failed to create test user: {error}")
        
    _db.session.flush()
    
    customer = Customer.query.filter_by(id=user.id).first()
    if not customer:
        raise Exception("Customer record not created")
    
    _db.session.commit()
    return customer

@pytest.fixture(scope='function')
def test_category(_db):
    category = Category(
        id=str(uuid.uuid4().int)[:8],
        name=f'Test Category {uuid.uuid4().hex[:8]}',
        description='Test Description',
    )
    _db.session.add(category)
    _db.session.commit()
    return category

@pytest.fixture(scope='function')
def test_medicine(_db, test_category):
    medicine = Medicine(
        name=f'Test Medicine {uuid.uuid4().hex[:8]}',
        description='Test Description',
        price=9.99,
        stock=100,
        category_id=test_category.id,
        expiry_date=datetime.now() + timedelta(days=365),
        low_stock_flag=False
    )
    _db.session.add(medicine)
    _db.session.commit()
    return medicine

class TestCustomerOrders:
    @pytest.fixture(autouse=True)
    def setup(self, _db):
        self.db = _db
        yield

    def test_checkout_empty_cart(self, client, auth_customer):
        with client.session_transaction() as sess:
            sess['user_id'] = auth_customer.id

        response = client.get('/checkout')
        assert response.status_code == 302

    def test_checkout_with_items(self, client, auth_customer, test_medicine):
        cart_item = Cart(
            customer_id=auth_customer.id, 
            medicine_id=test_medicine.id,
            quantity=1
        )
        self.db.session.add(cart_item)
        self.db.session.commit()

        with client.session_transaction() as sess:
            sess['user_id'] = auth_customer.id

        response = client.get('/checkout')
        assert response.status_code == 200
        assert bytes(test_medicine.name, 'utf-8') in response.data

    def test_place_order_cod(self, client, auth_customer, test_medicine):
        cart_item = Cart(
            customer_id=auth_customer.id,
            medicine_id=test_medicine.id,
            quantity=1
        )
        self.db.session.add(cart_item)
        self.db.session.commit()

        self.db.session.refresh(test_medicine)
        
        with client.session_transaction() as sess:
            sess['user_id'] = auth_customer.id

        response = client.post('/place_order', 
            json={
                'payment_method': 'cod',
            },
            headers={'Content-Type': 'application/json'}
        )
        
        assert response.status_code == 200
        
        order = Order.query.filter_by(
            customer_id=auth_customer.id
        ).order_by(Order.order_date.desc()).first()
        
        assert order is not None
        assert order.payment_method == 'Cash on Delivery'
        assert order.status == 'Pending'
        assert order.payment_status == 'Pending'
        
        cart_count = Cart.query.filter_by(customer_id=auth_customer.id).count()
        assert cart_count == 0

    def test_place_order_bkash(self, client, auth_customer, test_medicine):
        cart_item = Cart(
            customer_id=auth_customer.id,
            medicine_id=test_medicine.id,
            quantity=1
        )
        self.db.session.add(cart_item)
        self.db.session.commit()

        self.db.session.refresh(test_medicine)
        
        with client.session_transaction() as sess:
            sess['user_id'] = auth_customer.id

        response = client.post('/place_order', 
            json={
                'payment_method': 'bkash',
            },
            headers={'Content-Type': 'application/json'}
        )
        
        assert response.status_code == 200
        
        order = Order.query.filter_by(
            customer_id=auth_customer.id
        ).order_by(Order.order_date.desc()).first()
        
        assert order is not None
        assert order.payment_method == 'bKash'
        assert order.status == 'Pending'
        assert order.payment_status == 'Pending'
        
        cart_count = Cart.query.filter_by(customer_id=auth_customer.id).count()
        assert cart_count == 0

    def test_order_history(self, client, auth_customer, test_medicine):
        cart_item = Cart(
            customer_id=auth_customer.id,
            medicine_id=test_medicine.id,
            quantity=2
        )
        self.db.session.add(cart_item)
        self.db.session.commit()

        orders = []
        for i in range(2):
            order = Order.create(
                customer_id=auth_customer.id,
                total_price=test_medicine.price * 2,
                payment_method='Cash on Delivery' if i == 0 else 'bKash',
                status='Delivered' if i == 0 else 'Pending',
                payment_status='Paid' if i == 0 else 'Pending',
                order_date=datetime.now() - timedelta(days=i)
            )
            self.db.session.add(order)
            self.db.session.flush()
            orders.append(order)
        
        self.db.session.commit()

        # Set user session
        with client.session_transaction() as sess:
            sess['user_id'] = auth_customer.id

        # Test order history endpoint - updated URL to match controller route
        response = client.get('/order-history')  # Changed to match route in customer_controller.py
        assert response.status_code == 200

        # Verify response content
        assert bytes('Delivered', 'utf-8') in response.data
        assert bytes('Pending', 'utf-8') in response.data
        
        # Verify specific order details are present
        for order in orders:
            assert bytes(str(order.total_price), 'utf-8') in response.data
            assert bytes(order.payment_method, 'utf-8') in response.data
            assert bytes(order.status, 'utf-8') in response.data