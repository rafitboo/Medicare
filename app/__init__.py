from flask import Flask # type: ignore
from .models import db

def create_app():
    app = Flask(__name__, 
                template_folder='view/templates',
                static_folder='view')
    app.config['SECRET_KEY'] = "my_secret_key"
    app.config.from_object('config.Config')

    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    from .controllers.home import home
    from .controllers.auth_controller import auth
    from .controllers.customer_controller import customer
    from .controllers.admin_user_controller import admin_user
    from .controllers.admin_inventory_controller import admin_inventory
    from .controllers.admin_chat_controller import admin_chat
    from .controllers.staff_controller import staff

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin_user, url_prefix='/')
    app.register_blueprint(admin_inventory, url_prefix='/')
    app.register_blueprint(admin_chat, url_prefix='/')


    app.register_blueprint(customer, url_prefix='/') 
    app.register_blueprint(staff, url_prefix='/')

    return app