"""Database Engine"""
from flask import Blueprint, redirect, render_template, flash, url_for
from models import User
from forms import LoginForm, SignUpForm
from app import login_manager, db
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

"""Keep current user loaded in session"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

"""Define Blueprint"""
auth = Blueprint("auth", __name__, url_prefix="/")

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("views.home"))
            else:
                flash("Invalid password!", "danger")
        except Exception as e:
            flash("Email not registered!", "danger")
            
    return render_template("auth.html", form=form, text="Login", btn_action="Login")

@auth.route('/signup', methods={"GET", "POST"})
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash("The email is already registered.", "danger")
        else:
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = generate_password_hash(form.password.data, method="sha256")
            new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Successfully registered!", "success")
            return redirect(url_for("auth.login"))
    return render_template("auth.html", form=form, text="Register", btn_action="Create account")

@auth.route("/log-out")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.index"))