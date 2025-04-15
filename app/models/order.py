from . import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    payment_status = db.Column(db.String(50), nullable=False)
    transaction_id = db.Column(db.String(100), nullable=True)

    order_details = db.relationship('OrderDetails', backref='order', lazy=True)

    def confirmPayment(self):
        pass  # Confirm the payment for an order

    def cancelOrder(self):
        pass  # Cancel the order

    def getStatus(self):
        return self.status  # Return order status
