#python -m pytest .\app\controllers\test\test_customer_controllers.py

import pytest
from flask import session
from app import create_app, db
from app.models.customer import Customer 
from app.models.medicine import Medicine
from app.models.category import Category
from app.models.user import User
from app.models.cart import Cart
from app.models.chat import Chat
import sqlalchemy as sa
from datetime import datetime
import uuid
from sqlalchemy import text

class TestData:
    __test__ = False
    def __init__(self):
        self.category_id = None
        self.medicine_id = None
        self.customer_id = None
        self.username = None

@pytest.fixture(scope='function')
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config.from_object('config.TestConfig')
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.session.execute(text('SET FOREIGN_KEY_CHECKS=0;'))
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
        db.session.execute(text('SET FOREIGN_KEY_CHECKS=1;'))
        db.session.commit()

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def test_data(app):
    data = TestData()
    with app.app_context():

        category = Category(name=f"Test Category {uuid.uuid4()}")
        db.session.add(category)
        db.session.commit()
        data.category_id = category.id

 
        medicine = Medicine(
            name=f"Test Medicine {uuid.uuid4()}",
            description="Test Description",
            price=10.0,
            stock=100,
            category_id=category.id
        )
        db.session.add(medicine)
        db.session.commit()
        data.medicine_id = medicine.id

        test_uuid = uuid.uuid4()
        customer = Customer(
            username=f"testuser_{test_uuid}",
            email=f"test_{test_uuid}@test.com",
            password="test123",
            type="customer",
            role="customer"
        )
        db.session.add(customer)
        db.session.commit()
        data.customer_id = customer.id
        data.username = customer.username


        customer = Customer.query.get(customer.id)
        assert customer is not None, "Customer was not created properly"

    return data

def test_dashboard(client, test_data):
    with client.session_transaction() as session:
        session['user_id'] = test_data.customer_id
        session['user_role'] = 'customer'
    response = client.get('/customer/dashboard')
    assert response.status_code == 200

def test_get_cart(client, test_data):
   
    with client.session_transaction() as sess:
        sess['user_id'] = test_data.customer_id
        sess['user_role'] = 'customer'
        sess['logged_in'] = True 
    
 
    with client.application.app_context():
        customer = Customer.query.get(test_data.customer_id)
        cart_item, error = customer.add_to_cart(test_data.medicine_id, 1)
        assert error is None, f"Failed to add item to cart: {error}"
        db.session.commit()
    
  
    response = client.get('/customer/cart', follow_redirects=True)  
    assert response.status_code == 200

def test_add_to_cart(client, test_data):
    with client.session_transaction() as sess:
        sess['user_id'] = test_data.customer_id
        sess['user_role'] = 'customer'
        sess['logged_in'] = True
    
    with client.application.app_context():
      
        Cart.query.filter_by(customer_id=test_data.customer_id).delete()
        db.session.commit()
        

        cart_item, error = Cart.add_to_cart(test_data.customer_id, test_data.medicine_id, 2)
        assert error is None, f"Failed to add item to cart: {error}"
        assert cart_item is not None, "Cart item was not created"
        assert cart_item.quantity == 2
        db.session.commit()

def test_update_cart_item(client, test_data):
    with client.session_transaction() as sess:
        sess['user_id'] = test_data.customer_id
        sess['user_role'] = 'customer'
        sess['logged_in'] = True
    
    with client.application.app_context():
    
        Cart.query.filter_by(customer_id=test_data.customer_id).delete()
        db.session.commit()
        
       
        cart_item, error = Cart.add_to_cart(test_data.customer_id, test_data.medicine_id, 1)
        assert error is None, f"Failed to add item to cart: {error}"
        assert cart_item is not None, "Cart item was not created"
        db.session.commit()
        
       
        updated_item, error = Cart.update_cart_item(test_data.customer_id, test_data.medicine_id, 3)
        assert error is None, f"Failed to update cart item: {error}"
        assert updated_item is not None, "Cart item was not found"
        assert updated_item.quantity == 3
        db.session.commit()

def test_remove_from_cart(client, test_data):
    with client.session_transaction() as sess:
        sess['user_id'] = test_data.customer_id
        sess['user_role'] = 'customer'
        sess['logged_in'] = True
    
    with client.application.app_context():
      
        Cart.query.filter_by(customer_id=test_data.customer_id).delete()
        db.session.commit()
        
      
        cart_item, error = Cart.add_to_cart(test_data.customer_id, test_data.medicine_id, 1)
        assert error is None, f"Failed to add item to cart: {error}"
        assert cart_item is not None, "Cart item was not created"
        db.session.commit()
        
      
        success, error = Cart.remove_from_cart(test_data.customer_id, test_data.medicine_id)
        assert error is None, f"Failed to remove item from cart: {error}"
        assert success is True, "Failed to remove item from cart"
        
    
        cart_item = Cart.query.filter_by(
            customer_id=test_data.customer_id,
            medicine_id=test_data.medicine_id
        ).first()
        assert cart_item is None, "Cart item was not removed"

def test_mycart(client, test_data):
    with client.session_transaction() as sess:
        sess['user_id'] = test_data.customer_id
        sess['user_role'] = 'customer'
        sess['logged_in'] = True
    
   
    with client.application.app_context():
        customer = Customer.query.get(test_data.customer_id)
        cart_item, error = customer.add_to_cart(test_data.medicine_id, 1)
        assert error is None, f"Failed to add item to cart: {error}"
        db.session.commit()
    
    response = client.get('/customer/mycart', follow_redirects=True)
    assert response.status_code == 200

def test_customer_messages(client, test_data):
    with client.session_transaction() as sess:
        sess['user_id'] = test_data.customer_id
        sess['user_role'] = 'customer'
        sess['logged_in'] = True
    
    with client.application.app_context():
     
        Chat.query.filter_by(customer_id=test_data.customer_id).delete()
        db.session.commit()
        
        
        success, error = Chat.add_message(
            customer_id=test_data.customer_id,
            message='Test message',
            is_from_customer=True
        )
        assert error == "Message sent successfully.", f"Failed to add message: {error}"
        assert success is True, "Failed to add message"
        
       
        chat = Chat.query.filter_by(
            customer_id=test_data.customer_id,
            message='Test message',
            is_from_customer=True
        ).first()
        assert chat is not None, "Message was not created"