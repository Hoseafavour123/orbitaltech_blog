from flask import Blueprint, render_template

main = Blueprint("main", __name__, url_prefix="/")

@main.route("/home")
def home():
    return render_template("base.html")

@main.route("/posts")
def posts():
    return render_template("posts.html")

@main.route("/publish")
def publish():
    return render_template("publish.html")