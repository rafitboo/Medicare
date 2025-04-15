from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models here to register them with SQLAlchemy in the correct order
from .user import User  # Base user model first
from .admin import Admin
from .staff import Staff
from .customer import Customer
from .category import Category  # Categories before medicines
from .medicine import Medicine  # Medicines after categories
from .cart import Cart  # Cart depends on medicines and customers
from .order import Order  # Orders after customers
from .order_details import OrderDetails  # Order details after orders and medicines
from .chat import Chat  # Chat depends on users
from .prescription import Prescription  # Prescriptions depend on users
