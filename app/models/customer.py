from . import db
from .user import User
from .cart import Cart
from .medicine import Medicine

class Customer(User):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'customer',
        'inherit_condition': (id == User.id)
    }

    def __init__(self, **kwargs):
        kwargs['role'] = 'customer'
        kwargs['type'] = 'customer'
        super().__init__(**kwargs)

    def get_cart_data(self):
        cart_items = Cart.get_cart_items(self.id)
        total = Cart.get_cart_total(self.id)
        return cart_items, total, None

    def add_to_cart(self, medicine_id, quantity):
        medicine = Medicine.query.get(medicine_id)
        if not medicine:
            return None, "Medicine not found"
        if quantity > medicine.stock:
            return None, f"Only {medicine.stock} items available in stock!"
        cart_item = Cart.query.filter_by(customer_id=self.id, medicine_id=medicine_id).first()
        if cart_item:
            if quantity > medicine.stock:
                return None, f"You can't add more than {medicine.stock} items of this medicine!"
            cart_item.quantity = quantity
        else:
            cart_item = Cart(customer_id=self.id, medicine_id=medicine_id, quantity=quantity)
            db.session.add(cart_item)
        try:
            db.session.commit()
            return cart_item, None
        except Exception as e:
            db.session.rollback()
            return None, "Failed to update cart"

    def update_cart_item(self, medicine_id, quantity):
        cart_item = Cart.query.filter_by(customer_id=self.id, medicine_id=medicine_id).first()
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

    def remove_from_cart(self, medicine_id):
        cart_item = Cart.query.filter_by(customer_id=self.id, medicine_id=medicine_id).first()
        if not cart_item:
            return None, "Item not found in cart"
        db.session.delete(cart_item)
        try:
            db.session.commit()
            return True, None
        except Exception as e:
            db.session.rollback()
            return None, "Failed to remove item from cart"



