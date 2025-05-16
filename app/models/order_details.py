from . import db

class OrderDetails(db.Model):
    __tablename__ = 'order_details'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicines.id'), nullable=False)

    medicine = db.relationship('Medicine', lazy='joined')

    @classmethod
    def create(cls, order_id, medicine_id, quantity, price):
        
        try:
            if not all([order_id, medicine_id, quantity, price]):
                raise ValueError("All fields are required")

            if quantity <= 0:
                raise ValueError("Quantity must be positive")

            if price <= 0:
                raise ValueError("Price must be positive")

            detail = cls(
                order_id=order_id,
                medicine_id=medicine_id,
                quantity=quantity,
                price=float(price)
            )

            db.session.add(detail)
            db.session.commit()
            return detail

        except Exception as e:
            db.session.rollback()
            print(f"Error creating order detail: {str(e)}")
            return None
