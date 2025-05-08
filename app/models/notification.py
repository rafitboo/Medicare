from . import db
from datetime import datetime

class Notification(db.Model):
    __tablename__ = 'notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    notification_type = db.Column(db.String(50), nullable=False)  # e.g., 'stock_alert', 'general', etc.
    
    # Relationships
    staff = db.relationship('User', foreign_keys=[staff_id])
    
    @classmethod
    def create_notification(cls, staff_id, message, notification_type='general'):
        """Create a new notification."""
        notification = cls(
            staff_id=staff_id,
            message=message,
            notification_type=notification_type
        )
        db.session.add(notification)
        try:
            db.session.commit()
            return True, "Notification sent successfully."
        except Exception as e:
            db.session.rollback()
            return False, f"Error sending notification: {e}"
    
    @classmethod
    def get_unread_notifications(cls):
        """Get all unread notifications."""
        return cls.query.filter_by(is_read=False).order_by(cls.timestamp.desc()).all()
    
    @classmethod
    def get_all_notifications(cls):
        """Get all notifications."""
        return cls.query.order_by(cls.timestamp.desc()).all()
    
    @classmethod
    def mark_as_read(cls, notification_id):
        """Mark a notification as read."""
        notification = cls.query.get(notification_id)
        if notification:
            notification.is_read = True
            try:
                db.session.commit()
                return True
            except Exception:
                db.session.rollback()
                return False
        return False
    
    @classmethod
    def mark_all_as_read(cls):
        """Mark all notifications as read."""
        try:
            cls.query.filter_by(is_read=False).update({'is_read': True})
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False 