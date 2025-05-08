from . import db
from .user import User
from .chat import Chat
from .notification import Notification

class Staff(User):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'staff',
        'inherit_condition': (id == User.id)
    }

    def __init__(self, **kwargs):
        kwargs['role'] = 'staff'
        kwargs['type'] = 'staff'
        super().__init__(**kwargs)

    def viewNewOrders(self):
        pass  # Implement logic to view new orders

    def verifyPayment(self, transaction_id):
        pass  # Implement payment verification logic

    def updateOrderStatus(self, order_id, status):
        pass  # Implement the logic to update order status

    def viewLowStockAlerts(self):
        pass  # Implement low stock alerts logic

    def notifyAdmin(self, message, notification_type='general'):
        """Send a notification to admin."""
        return Notification.create_notification(self.id, message, notification_type)

    def approvePrescription(self, prescription_id):
        pass  # Approve prescription logic
