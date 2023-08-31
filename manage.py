from flask import render_template
from flask_login import login_required
from app import create_app, db
from models import User

app = create_app()

app.app_context().push()
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
