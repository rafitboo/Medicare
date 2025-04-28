from . import db
from .user import User
from .chat import Chat

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

    def notifyAdmin(self, medicine_id):
        pass  # Notify admin about low stock

    def approvePrescription(self, prescription_id):
        pass  # Approve prescription logic

    def respondToChat(self, customer_id, message):
        """Respond to a customer message."""
        return Chat.add_message(customer_id, message, is_from_customer=False)

    def get_all_customer_conversations(self):
        """Get all customer IDs who have conversations."""
        return Chat.get_customer_conversations()

    def get_customer_conversation(self, customer_id):
        """Get the conversation with a specific customer."""
        # Mark messages as read when staff views them
        Chat.mark_as_read(customer_id)
        return Chat.get_conversation(customer_id)
