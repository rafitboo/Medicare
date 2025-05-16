from . import db
from .medicine import Medicine

class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicines.id'), nullable=False)
    
    medicine = db.relationship('Medicine', backref='cart_items')

    __table_args__ = (
        db.UniqueConstraint('customer_id', 'medicine_id', name='unique_cart_item'),
    )

    @classmethod
    def add_to_cart(cls, customer_id, medicine_id, quantity):
        # First, try to get the medicine
        medicine = Medicine.query.get(medicine_id)
        if not medicine:
            return None, "Medicine not found"
        if quantity > medicine.stock:
            return None, f"Only {medicine.stock} items available in stock!"

        # Try to get existing cart item
        cart_item = cls.query.filter_by(customer_id=customer_id, medicine_id=medicine_id).first()
        
        if cart_item:
            # Update existing item's quantity to the new quantity
            if quantity > medicine.stock:
                return None, f"You can't add more than {medicine.stock} items of this medicine!"
            cart_item.quantity = quantity
        else:
            # Create new cart item
            cart_item = cls(customer_id=customer_id, medicine_id=medicine_id, quantity=quantity)
            db.session.add(cart_item)

        try:
            db.session.commit()
            return cart_item, None
        except Exception as e:
            db.session.rollback()
            # If we get a unique constraint violation, try to update the existing item
            if 'unique_cart_item' in str(e):
                existing_item = cls.query.filter_by(customer_id=customer_id, medicine_id=medicine_id).first()
                if existing_item:
                    if quantity > medicine.stock:
                        return None, f"You can't add more than {medicine.stock} items of this medicine!"
                    existing_item.quantity = quantity
                    db.session.commit()
                    return existing_item, None
            return None, "Failed to update cart"

    @classmethod
    def update_cart_item(cls, customer_id, medicine_id, quantity):
        cart_item = cls.query.filter_by(customer_id=customer_id, medicine_id=medicine_id).first()
        if not cart_item:
            return None, "Item not found in cart"
        
        medicine = Medicine.query.get(medicine_id)
        if quantity > medicine.stock:
            return None, f"Only {medicine.stock} items available in stock!"
            
        cart_item.quantity = quantity
        try:
            db.session.commit()
            return cart_item, None
        except Exception as e:
            db.session.rollback()
            return None, "Failed to update cart"

    @classmethod
    def remove_from_cart(cls, customer_id, medicine_id):
        cart_item = cls.query.filter_by(customer_id=customer_id, medicine_id=medicine_id).first()
        if not cart_item:
            return None, "Item not found in cart"
        db.session.delete(cart_item)
        try:
            db.session.commit()
            return True, None
        except Exception as e:
            db.session.rollback()
            return None, "Failed to remove item from cart"

    @classmethod
    def get_cart_items(cls, customer_id):
        return cls.query.filter_by(customer_id=customer_id).join(Medicine).all()

    @classmethod
    def get_cart_total(cls, customer_id):
        items = cls.get_cart_items(customer_id)
        return sum(item.medicine.price * item.quantity for item in items)