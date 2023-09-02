from flask import render_template
from flask_login import login_required
from flask_migrate import Migrate
from app import create_app, db
from models import User, Post

app = create_app()
app.app_context().push()
db.create_all()

# Database migration
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
