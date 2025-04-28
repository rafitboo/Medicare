from . import db
from .user import User
from .medicine import Medicine
from .category import Category
from .customer import Customer
from .staff import Staff
from .chat import Chat

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

    def add_medicine(self, name, description, category_id, price, stock):
        """Add a new medicine."""
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
        """Update an existing medicine."""
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
        """Delete a medicine."""
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

    def viewAllOrders(self):
        pass  # Implement logic to view all orders

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
        if user:
            try:
                db.session.delete(user)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                print(f"Error deleting user: {e}")
                return False
        return False

    def add_user(self, username, email, phone, role='customer', address=None, password=None):
        """Add a new user and update the role-specific table with minimal redundancy."""
        # Validate existing user
        if User.query.filter((User.username == username) | (User.email == email)).first():
            return False, "A user with this username or email already exists."

        # Map roles to their respective classes
        role_classes = {
            'customer': Customer,
            'admin': Admin,
            'staff': Staff
        }

        # Validate role and get the appropriate class
        user_class = role_classes.get(role)
        if not user_class:
            return False, "Invalid role specified."

        # Create the user object dynamically
        new_user = user_class(
            username=username,
            email=email,
            phone=phone,
            address=address,
            password=password
        )

        # Commit to database
        try:
            db.session.add(new_user)
            db.session.commit()
            return True, f"{role.capitalize()} added successfully."
        except Exception as e:
            db.session.rollback()
            return False, f"Error adding user: {e}"

    def respondToChat(self, customer_id, message):
        """Respond to a customer message."""
        return Chat.add_message(customer_id, message, is_from_customer=False)

    def get_all_customer_conversations(self):
        """Get all customer IDs who have conversations."""
        return Chat.get_customer_conversations()

    def get_customer_conversation(self, customer_id):
        """Get the conversation with a specific customer."""
        # Mark messages as read when admin views them
        Chat.mark_as_read(customer_id)
        return Chat.get_conversation(customer_id)

    def add_category(self, name, description):
        """Add a new category."""
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
        """Update an existing category."""
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
        """Delete a category."""
        category = Category.query.get(category_id)
        if not category:
            return False, "Category not found."

        # Check if any medicines are associated with this category
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
