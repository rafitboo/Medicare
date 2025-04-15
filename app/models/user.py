from . import db
from .cart import Cart
from .medicine import Medicine

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    role = db.Column(db.String(20), nullable=False, default='customer')
    type = db.Column(db.String(50), nullable=False, default='customer')  # Set default to 'customer'

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    orders = db.relationship('Order', backref='customer', lazy=True)
    prescriptions = db.relationship('Prescription', backref='customer', lazy=True)
    chats_sent = db.relationship('Chat', foreign_keys='Chat.sender_id', backref='sender', lazy=True)
    chats_received = db.relationship('Chat', foreign_keys='Chat.receiver_id', backref='receiver', lazy=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if not self.type:
            self.type = 'customer'
        if not self.role:
            self.role = 'customer'

    def check_password(self, input_password):
        return self.password == input_password  # plain text comparison

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def register(cls, username, email, phone, password, role='customer', type='customer'):
        if cls.query.filter_by(email=email).first():
            return None, "Email already exists"

        user = cls(
            username=username,
            email=email,
            password=password,
            phone=phone,
            role=role,
            type=type
        )
        db.session.add(user)
        db.session.commit()
        return user, None

    @classmethod
    def login(cls, email, password):
        user = cls.find_by_email(email)
        if user and user.check_password(password):
            return user
        return None

    @staticmethod
    def logout(session):
        session.clear()

    