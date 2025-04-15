from . import db
from .user import User
from .medicine import Medicine
class Admin(User):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }

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

    def respondToChat(self):
        pass  # Implement chat response logic
