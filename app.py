from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

db = SQLAlchemy()

# Application factory
def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/prime_db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    
    login_manager.init_app(app)
    db.init_app(app)
    
    # Register blueprints
    from auth import auth
    from views import views
    
    app.register_blueprint(auth)
    app.register_blueprint(views)
    
    return app