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
    type = db.Column(db.String(50), nullable=False, default='customer')

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    orders = db.relationship('Order', backref='customer', lazy=True)
    prescriptions = db.relationship('Prescription', backref='customer', lazy=True)
    messages = db.relationship('Chat', foreign_keys='Chat.customer_id', backref='customer_user', lazy=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if not self.type:
            self.type = 'customer'
        if not self.role:
            self.role = 'customer'

    def check_password(self, input_password):
        return self.password == input_password

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def signup(cls, username, email, phone, password, confirm_password, terms, role='customer', type='customer'):
        """Handle user signup with validation"""
        if not all([username, email, phone, password, confirm_password]):
            return None, "All fields are required"

        if not terms:
            return None, "You must agree to the terms"

        if password != confirm_password:
            return None, "Passwords do not match!"

        if len(password) < 8:
            return None, "Password must be at least 8 characters"

        # Check for existing username
        if cls.query.filter_by(username=username).first():
            return None, "Username already exists"

        # Check for existing email
        if cls.query.filter_by(email=email).first():
            return None, "Email already exists"

        from .customer import Customer
        from .admin import Admin
        from .staff import Staff

        role_classes = {
            'customer': Customer,
            'admin': Admin,
            'staff': Staff
        }

        user_class = role_classes.get(role, cls)
        if user_class not in (Customer, Admin, Staff, cls):
            return None, "Invalid role specified"

        user = user_class(
            username=username,
            email=email,
            phone=phone,
            password=password,
            role=role,
            type=type
        )

        try:
            db.session.add(user)
            db.session.commit()
            return user, None
        except Exception as e:
            db.session.rollback()
            return None, f"Error registering user: {e}"

    @classmethod
    def login(cls, email, password):
        """Handle user login"""
        if not email or not password:
            return None, "Email and password are required"

        user = cls.find_by_email(email)
        if not user or not user.check_password(password):
            return None, "Invalid email or password"

        return user, None

    @staticmethod
    def logout(session):
        session.clear()

    def update_profile(self, **kwargs):
        """Update user profile information"""
        allowed_fields = ['username', 'email', 'password', 'address', 'phone']
        
        for field, value in kwargs.items():
            if field in allowed_fields and value is not None:
                setattr(self, field, value)
        
        try:
            db.session.commit()
            return True, "Profile updated successfully"
        except Exception as e:
            db.session.rollback()
            return False, f"Error updating profile: {str(e)}"

    