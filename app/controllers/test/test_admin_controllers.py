#pytest -v app/controllers/test/test_admin_controllers.py
import pytest
from flask import session
from app import create_app, db
from app.models.admin import Admin
from app.models.medicine import Medicine
from app.models.category import Category
from app.models.user import User
from app.models.staff import Staff
import sqlalchemy as sa
from datetime import datetime
import uuid

class TestData:
    def __init__(self):
        self.admin = None
        self.category = None
        self.medicine = None
        self.user = None

def cleanup_test_data(session):
    try:
        session.query(Medicine).filter(
            Medicine.name.like('Test%')
        ).delete(synchronize_session=False)
        
        session.query(Category).filter(
            Category.name.like('Test%')
        ).delete(synchronize_session=False)
        
        admin_emails = session.query(User.id).filter(
            User.email.like('%test.com'),
            User.type == 'admin'
        ).all()
        admin_ids = [id for (id,) in admin_emails]
        
        staff_emails = session.query(User.id).filter(
            User.email.like('%test.com'),
            User.type == 'staff'
        ).all()
        staff_ids = [id for (id,) in staff_emails]
        
        if admin_ids:
            session.query(Admin).filter(
                Admin.id.in_(admin_ids)
            ).delete(synchronize_session=False)
            
        if staff_ids:
            session.query(Staff).filter(
                Staff.id.in_(staff_ids)
            ).delete(synchronize_session=False)
        
        session.query(User).filter(
            User.email.like('%test.com')
        ).delete(synchronize_session=False)
        
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

@pytest.fixture(scope='function')
def app_client():
    engine = sa.create_engine('mysql://root:@localhost/')
    with engine.connect() as conn:
        conn.execute(sa.text("DROP DATABASE IF EXISTS medicare_test"))
        conn.execute(sa.text("CREATE DATABASE medicare_test"))
        conn.execute(sa.text("USE medicare_test"))
    
    app = create_app()
    app.config.from_object('config.TestConfig')
    
    with app.app_context():
        db.create_all()
    
    yield app
    
    with engine.connect() as conn:
        conn.execute(sa.text("DROP DATABASE medicare_test"))

@pytest.fixture(scope='function')
def test_data(app_client):
    data = TestData()
    unique_id = str(uuid.uuid4())[:8]
    
    with app_client.app_context():
        cleanup_test_data(db.session)
        
        data.admin = Admin(
            username=f'testadmin_{unique_id}',
            email=f'admin_{unique_id}@test.com',
            password='testpass123',
            phone='1234567890',
            role='admin',
            type='admin'
        )
        db.session.add(data.admin)
        db.session.flush()
        
        data.category = Category(
            name=f'Test Category {unique_id}',
            description='Test Category Description'
        )
        db.session.add(data.category)
        db.session.flush()
        
        data.medicine = Medicine(
            name=f'Test Medicine {unique_id}',
            description='Test Medicine Description',
            category_id=data.category.id,
            price=10.99,
            stock=100
        )
        db.session.add(data.medicine)
        db.session.flush()
        
        data.user = Staff(
            username=f'teststaff_{unique_id}',
            email=f'staff_{unique_id}@test.com',
            phone='9876543210',
            role='staff',
            type='staff',
            password='staffpass123',
            address='Test Address'
        )
        db.session.add(data.user)
        db.session.commit()
        
        data.admin_id = data.admin.id
        data.category_id = data.category.id
        data.medicine_id = data.medicine.id
        data.user_id = data.user.id
        
    return data

@pytest.fixture(scope='function')
def client(app_client, test_data):
    with app_client.app_context():
        with app_client.test_client() as client:
            with client.session_transaction() as sess:
                sess['user_id'] = test_data.admin_id
                sess['user_role'] = 'admin'
            yield client
            cleanup_test_data(db.session)

def test_manage_medicines(client, test_data):
    with client.application.app_context():
        response = client.post('/admin/manage_medicines', data={
            'action': 'add',
            'name': 'Test New Medicine',
            'description': 'Test new medicine description',
            'category_id': str(test_data.category_id),
            'price': '15.99',
            'stock': '150'
        })
        assert response.status_code == 302
        
        medicine = Medicine.query.filter_by(name='Test New Medicine').first()
        assert medicine is not None
        assert medicine.price == 15.99
        assert medicine.stock == 150

def test_manage_users(client):
    with client.application.app_context():
        response = client.post('/staff/manage_users', data={
            'action': 'add',
            'username': 'newstaff',
            'email': 'newstaff@test.com',
            'phone': '5555555555',
            'role': 'staff',
            'address': 'New Staff Address',
            'password': 'staffpass123'
        })
        assert response.status_code == 302
        
        user = User.query.filter_by(email='newstaff@test.com').first()
        assert user is not None
        assert user.role == 'staff'

def test_manage_categories(client):
    with client.application.app_context():
        response = client.post('/admin/manage_categories', data={
            'action': 'add',
            'name': 'Test New Category',
            'description': 'Test new category description'
        })
        assert response.status_code == 302
        
        category = Category.query.filter_by(name='Test New Category').first()
        assert category is not None
        assert category.description == 'Test new category description'

def test_delete_medicine(client, test_data):
    with client.application.app_context():
        response = client.post(f'/admin/delete_medicine/{test_data.medicine_id}')
        assert response.status_code == 302
        
        deleted_medicine = Medicine.query.filter_by(id=test_data.medicine_id).first()
        assert deleted_medicine is None

def test_batch_update_medicine_stock(client, test_data):
    with client.application.app_context():
        medicines_data = [
            ('Test Batch Med A', '10.99', '100'),
            ('Test Batch Med B', '15.99', '50'),
            ('Test Batch Med C', '20.99', '75')
        ]
        
        for name, price, stock in medicines_data:
            response = client.post('/admin/manage_medicines', data={
                'action': 'add',
                'name': name,
                'description': f'Test medicine {name}',
                'category_id': str(test_data.category_id),
                'price': price,
                'stock': stock
            })
            assert response.status_code == 302
            
        for name, _, _ in medicines_data:
            medicine = Medicine.query.filter_by(name=name).first()
            assert medicine is not None
            
            new_stock = 125
            response = client.post(f'/admin/edit_medicine/{medicine.id}', data={
                'name': medicine.name,
                'description': medicine.description,
                'category_id': str(medicine.category_id),
                'price': str(medicine.price),
                'stock': str(new_stock)
            })
            assert response.status_code == 302
            
            updated_medicine = Medicine.query.filter_by(id=medicine.id).first()
            assert updated_medicine.stock == new_stock

def test_edit_user(client, test_data):
    with client.application.app_context():
        new_username = 'Updated Staff Name'
        new_email = 'updated_staff@test.com'
        new_phone = '9999999999'
        new_address = 'Updated Address'
        
        response = client.post(f'/admin/edit_users/{test_data.user_id}', data={
            'name': new_username,
            'email': new_email,
            'role': 'staff',
            'phone': new_phone,
            'address': new_address
        })
        assert response.status_code == 302
        
        updated_user = User.query.get(test_data.user_id)
        assert updated_user is not None
        assert updated_user.username == new_username
        assert updated_user.email == new_email
        assert updated_user.phone == new_phone
        assert updated_user.address == new_address

def test_delete_user(client, test_data):
    with client.application.app_context():
        response = client.post(f'/admin/delete_user/{test_data.user_id}')
        assert response.status_code == 302
        
        deleted_user = User.query.filter_by(id=test_data.user_id).first()
        assert deleted_user is None

def test_edit_category(client, test_data):
    with client.application.app_context():
        new_name = 'Updated Test Category'
        new_description = 'Updated test category description'
        
        response = client.post(f'/admin/edit_category/{test_data.category_id}', data={
            'name': new_name,
            'description': new_description
        })
        assert response.status_code == 302
        
        updated_category = Category.query.get(test_data.category_id)
        assert updated_category is not None
        assert updated_category.name == new_name
        assert updated_category.description == new_description

def test_delete_category(client, test_data):
    with client.application.app_context():

        Medicine.query.filter_by(category_id=test_data.category_id).delete()
        db.session.commit()
        
        response = client.post(f'/admin/delete_category/{test_data.category_id}')
        assert response.status_code == 302
        
        deleted_category = Category.query.filter_by(id=test_data.category_id).first()
        assert deleted_category is None