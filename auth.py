"""Database Engine"""
from flask import Blueprint, redirect, render_template
from models import User
from forms import LoginForm, SignUpForm
from app import login_manager

"""Keep current user loaded in session"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

"""Define Blueprint"""
auth = Blueprint("auth", __name__, url_prefix="/")

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("auth.html", form=form, text="Login", btn_action="Login")

@auth.route('/signup', methods={"GET", "POST"})
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
            pass
    return render_template("auth.html", form=form, text="Register", btn_action="Create account")

@auth.route("/log-out")
def logout():
    return redirect("/")