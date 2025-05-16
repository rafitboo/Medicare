from . import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Pending')
    payment_method = db.Column(db.String(50), nullable=False, default='Cash on Delivery')
    payment_status = db.Column(db.String(50), nullable=False, default='Pending')
    transaction_id = db.Column(db.String(50), nullable=True)
    bkash_number = db.Column(db.String(11), nullable=True)

    order_details = db.relationship('OrderDetails', backref='order', lazy=True)

    @classmethod
    def create(cls, customer_id, total_price, payment_method='Cash on Delivery', status='Pending', payment_status='Pending', order_date=datetime.utcnow()):
        try:
            # Input validation
            if not customer_id:
                raise ValueError("Customer ID is required")
            if not total_price:
                raise ValueError("Total amount is required")
            
            order = cls(
                customer_id=customer_id,
                total_price=float(total_price),
                payment_method=payment_method,
                payment_status=payment_status,
                status=status,
                order_date=order_date
            )

            db.session.add(order)
            db.session.commit()
            return order

        except Exception as e:
            db.session.rollback()
            return None
        
    def confirmPayment(self):
        pass  # Confirm the payment for an order

    def cancelOrder(self):
        pass  # Cancel the order

    def getStatus(self):
        return self.status  # Return order status
