from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager
from flask_ckeditor import CKEditor
from flask_session import Session
import os

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"

db = SQLAlchemy()
sess = Session()
ckeditor = CKEditor()

# Application factory
def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = "secret"
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    #app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/prime_db"
    #app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://mtxhfipnrdhayb:3050c1a2c47bb7cb33f36d031b12e74a69d200281de4c6eddebe78d951e54cf8@ec2-35-169-9-79.compute-1.amazonaws.com:5432/d3p9qp8g4p4otu"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    
    app.config["UPLOAD_FOLDER"] = "static/images/"
    #app.config["UPLOAD_FOLDER"] = "orbitaltech_blog/static/images"
    
    db.init_app(app)
    login_manager.init_app(app)
    """Keep current user loaded in session"""
    from models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    ckeditor.init_app(app)
    sess.init_app(app)
    
    # Register blueprints
    from auth import auth
    from views import views
    
    app.register_blueprint(auth)
    app.register_blueprint(views)
    
    return app
