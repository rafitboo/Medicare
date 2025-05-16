from . import db
from .user import User
from .medicine import Medicine
from .category import Category
from .customer import Customer
from .staff import Staff
from .chat import Chat
from .cart import Cart
from .order import Order

class Admin(User):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'admin',
        'inherit_condition': (id == User.id)
    }

    def __init__(self, **kwargs):
        kwargs['role'] = 'admin'
        kwargs['type'] = 'admin'
        super().__init__(**kwargs)
    def add_user(self, username, email, phone, role='customer', address=None, password=None):

        if User.query.filter((User.username == username) | (User.email == email)).first():
            return False, "A user with this username or email already exists."

        role_classes = {
            'customer': Customer,
            'admin': Admin,
            'staff': Staff
        }


        user_class = role_classes.get(role)
        if not user_class:
            return False, "Invalid role specified."
        
        new_user = user_class(
            username=username,
            email=email,
            phone=phone,
            address=address,
            password=password
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            return True, f"{role.capitalize()} added successfully."
        except Exception as e:
            db.session.rollback()
            return False, f"Error adding user: {e}"
    
    def edit_user(self, user_id, name, email, role, address, phone):
        user = User.query.get(user_id)
        if not user:
            return False

        user.username = name
        user.email = email
        user.role = role
        user.address = address
        user.phone = phone

        try:
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error editing user: {e}")
            return False

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return False

        try:
            Cart.query.filter_by(customer_id=user_id).delete()
            Chat.query.filter_by(customer_id=user_id).delete()
            Order.query.filter_by(customer_id=user_id).delete()

            db.session.delete(user)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting user: {e}")
            return False
    
    def add_category(self, name, description):

        existing_category = Category.query.filter_by(name=name).first()
        if existing_category:
            return False, "Category already exists."

        new_category = Category(name=name, description=description)
        db.session.add(new_category)
        try:
            db.session.commit()
            return True, "Category added successfully."
        except Exception as e:
            db.session.rollback()
            return False, f"Error adding category: {e}"

    def update_category(self, category_id, name, description):

        category = Category.query.get(category_id)
        if not category:
            return False, "Category not found."

        category.name = name
        category.description = description
        try:
            db.session.commit()
            return True, "Category updated successfully."
        except Exception as e:
            db.session.rollback()
            return False, f"Error updating category: {e}"

    def delete_category(self, category_id):

        category = Category.query.get(category_id)
        if not category:
            return False, "Category not found."
        associated_medicines = Medicine.query.filter_by(category_id=category_id).count()
        if associated_medicines > 0:
            return False, "Cannot delete category. There are medicines associated with this category."

        db.session.delete(category)
        try:
            db.session.commit()
            return True, "Category deleted successfully."
        except Exception as e:
            db.session.rollback()
            return False, f"Error deleting category: {e}"

    def add_medicine(self, name, description, category_id, price, stock):
        existing_medicine = Medicine.query.filter_by(name=name).first()
        if existing_medicine:
            return False, "Medicine already exists."

        new_medicine = Medicine(
            name=name,
            description=description,
            category_id=category_id,
            price=price,
            stock=stock
        )
        db.session.add(new_medicine)
        try:
            db.session.commit()
            return True, "Medicine added successfully."
        except Exception as e:
            db.session.rollback()
            return False, f"Error adding medicine: {e}"

    def update_medicine(self, medicine_id, name, description, category_id, price, stock):
        medicine = Medicine.query.get(medicine_id)
        if not medicine:
            return False, "Medicine not found."

        medicine.name = name
        medicine.description = description
        medicine.category_id = category_id
        medicine.price = price
        medicine.stock = stock

        try:
            db.session.commit()
            return True, "Medicine updated successfully."
        except Exception as e:
            db.session.rollback()
            return False, f"Error updating medicine: {e}"

    def delete_medicine(self, medicine_id):
        medicine = Medicine.query.get(medicine_id)
        if not medicine:
            return False, "Medicine not found."

        db.session.delete(medicine)
        try:
            db.session.commit()
            return True, "Medicine deleted successfully."
        except Exception as e:
            db.session.rollback()
            return False, f"Error deleting medicine: {e}"

    def updateStock(self, medicine_id, stock):
        medicine = Medicine.query.get(medicine_id)
        if medicine:
            medicine.stock = stock
            db.session.commit()
            return True
        return False


    
