from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager
from flask_ckeditor import CKEditor
import os

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"

db = SQLAlchemy()

ckeditor = CKEditor()

# Application factory
def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://mtxhfipnrdhayb:3050c1a2c47bb7cb33f36d031b12e74a69d200281de4c6eddebe78d951e54cf8@ec2-35-169-9-79.compute-1.amazonaws.com:5432/d3p9qp8g4p4otu"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    
    app.config["UPLOAD_FOLDER"] = "static/images/"
    
    login_manager.init_app(app)
    ckeditor.init_app(app)
    db.init_app(app)
    
    # Register blueprints
    from auth import auth
    from views import views
    
    app.register_blueprint(auth)
    app.register_blueprint(views)
    
    return app