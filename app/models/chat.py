from . import db
from datetime import datetime

class Chat(db.Model):
    __tablename__ = 'chats'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    is_from_customer = db.Column(db.Boolean, default=True)
    is_read = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship with the user (customer) - remove the backref since it's defined in User model
    customer = db.relationship('User', foreign_keys=[customer_id])
    
    @classmethod
    def add_message(cls, customer_id, message, is_from_customer=True):
        """Add a new message to the chat."""
        new_message = cls(
            customer_id=customer_id,
            message=message,
            is_from_customer=is_from_customer
        )
        db.session.add(new_message)
        try:
            db.session.commit()
            return True, "Message sent successfully."
        except Exception as e:
            db.session.rollback()
            return False, f"Error sending message: {e}"
    
    @classmethod
    def get_customer_conversations(cls):
        """Get all unique customer IDs with messages."""
        from sqlalchemy import distinct
        customer_ids = db.session.query(distinct(cls.customer_id)).all()
        return [id[0] for id in customer_ids]
    
    @classmethod
    def get_conversation(cls, customer_id):
        """Get entire conversation with a specific customer."""
        return cls.query.filter_by(customer_id=customer_id).order_by(cls.timestamp).all()
    
    @classmethod
    def mark_as_read(cls, customer_id):
        """Mark all messages from a customer as read."""
        unread_messages = cls.query.filter_by(customer_id=customer_id, is_read=False).all()
        for message in unread_messages:
            message.is_read = True
        try:
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    def sendMessage(self):
        pass  # Send message logic

    def receiveMessage(self):
        pass  # Receive message logic
