from flask import render_template
from flask_login import login_required
from flask_migrate import Migrate
from app_factory import create_app, db
from models import User, Post

app = create_app()

if __name__ == "__main__":
    app.run()
