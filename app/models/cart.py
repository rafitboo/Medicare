from . import db
from .medicine import Medicine

class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicines.id'), nullable=False)

    @classmethod
    def add_to_cart(cls, customer_id, medicine_id, quantity):
        medicine = Medicine.query.get(medicine_id)
        if not medicine:
            return None, "Medicine not found"
        if quantity > medicine.stock:
            return None, f"Only {medicine.stock} items available in stock!"

        cart_item = cls.query.filter_by(customer_id=customer_id, medicine_id=medicine_id).first()
        if cart_item:
            new_quantity = cart_item.quantity + quantity
            if new_quantity > medicine.stock:
                return None, f"You can't add more than {medicine.stock} items of this medicine!"
            cart_item.quantity = new_quantity
        else:
            cart_item = cls(customer_id=customer_id, medicine_id=medicine_id, quantity=quantity)
            db.session.add(cart_item)

        db.session.commit()
        return cart_item, None

    @classmethod
    def update_cart_item(cls, customer_id, medicine_id, quantity):
        cart_item = cls.query.filter_by(customer_id=customer_id, medicine_id=medicine_id).first()
        if not cart_item:
            return None, "Item not found in cart"
        cart_item.quantity = quantity
        db.session.commit()
        return cart_item, None

    @classmethod
    def remove_from_cart(cls, customer_id, medicine_id):
        cart_item = cls.query.filter_by(customer_id=customer_id, medicine_id=medicine_id).first()
        if not cart_item:
            return None, "Item not found in cart"
        db.session.delete(cart_item)
        db.session.commit()
        return True, None

    @classmethod
    def get_cart_items(cls, customer_id):
        return cls.query.filter_by(customer_id=customer_id).join(Medicine).all()