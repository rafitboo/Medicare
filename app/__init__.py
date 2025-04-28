from flask import Flask # type: ignore
from .models import db

def create_app():
    app = Flask(__name__, 
                template_folder='view/templates',
                static_folder='view')
    app.config['SECRET_KEY'] = "my_secret_key"
    app.config.from_object('config.Config')

    # Initialize database
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    from .controllers.home import home
    from .controllers.auth_controller import auth
    from .controllers.customer_controller import customer
    from .controllers.admin_controller import admin

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(customer, url_prefix='/') 
    app.register_blueprint(admin, url_prefix='/')
    
    return app