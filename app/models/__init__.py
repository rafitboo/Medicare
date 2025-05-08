from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from .user import User 
from .admin import Admin
from .staff import Staff
from .customer import Customer
from .category import Category  
from .medicine import Medicine  
from .cart import Cart  
from .order import Order  
from .order_details import OrderDetails  
from .chat import Chat 
from .prescription import Prescription  
from .chat import Chat
from .notification import Notification
