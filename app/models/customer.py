from . import db
from .user import User

class Customer(User):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'customer',
        'inherit_condition': (id == User.id)
    }

    def __init__(self, **kwargs):
        super(Customer, self).__init__(**kwargs)
        self.type = 'customer'
        self.role = 'customer'

    # Additional customer-specific methods...


    def searchMedicine(self, keyword):
        pass  # Implement medicine search logic

    def filterMedicines(self, category, priceRange):
        pass  # Implement logic to filter medicines by category or price range

    def viewMedicineDetails(self, medicine_id):
        pass  # Implement medicine details viewing logic

    def addToCart(self, medicine_id, quantity):
        pass  # Add medicine to cart

    def placeOrder(self):
        pass  # Place an order

    def trackOrders(self):
        pass  # Implement order tracking logic

    def uploadPrescription(self, file):
        pass  # Implement logic for uploading prescription

    def startChat(self):
        pass  # Start a chat with staff/admin
