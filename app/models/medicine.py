from . import db
from datetime import datetime

class Medicine(db.Model):
    __tablename__ = 'medicines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    expiry_date = db.Column(db.Date, nullable=True)
    low_stock_flag = db.Column(db.Boolean, default=False)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def isLowStock(self):
        return self.stock < 10  # Example check for low stock

    def isNearExpiry(self):
        return self.expiry_date and self.expiry_date < datetime.utcnow()

    def updateStock(med_ids, cart_items):
        for med_id in med_ids:
            medicine = Medicine.query.get(med_id)
            for item in cart_items:
                quantity = item.quantity
                if medicine.id == item.medicine_id:
                    if quantity > medicine.stock:
                        return None, f"Only {medicine.stock} items available in stock!"
                    medicine.stock -= quantity
                    db.session.commit()
                else:
                    return None, "Medicine not found"
        return True