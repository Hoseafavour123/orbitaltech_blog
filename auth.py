from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix="/")

@auth.route("/login")
def login():
    return "<h1>Login page</h1>"

@auth.route('/signup')
def signup():
    return "<h1>Sign Up Page</h1>"