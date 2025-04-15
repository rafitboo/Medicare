from . import db

class Prescription(db.Model):
    __tablename__ = 'prescriptions'
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def upload(self):
        pass  # Upload prescription logic

    def approve(self):
        pass  # Approve prescription logic

    def reject(self):
        pass  # Reject prescription logic
