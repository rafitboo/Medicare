from . import db
from .user import User

class Staff(User):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'staff'
    }

    def viewNewOrders(self):
        pass  # Implement logic to view new orders

    def verifyPayment(self, transaction_id):
        pass  # Implement payment verification logic

    def updateOrderStatus(self, order_id, status):
        pass  # Implement the logic to update order status

    def viewLowStockAlerts(self):
        pass  # Implement low stock alerts logic

    def notifyAdmin(self, medicine_id):
        pass  # Notify admin about low stock

    def approvePrescription(self, prescription_id):
        pass  # Approve prescription logic

    def respondToChat(self):
        pass  # Implement chat response logic
