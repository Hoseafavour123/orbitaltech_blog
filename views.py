from flask import Blueprint, render_template

views = Blueprint("views", __name__, url_prefix="/")

#Error handling
@views.errorhandler(404)
def error404(e):
    return render_template("404.html")

@views.errorhandler(500)
def error500(e):
    return render_template("500.html")

@views.route("/", strict_slashes=False)
def index():
    return render_template("index.html")

@views.route("/home", strict_slashes=False)
def home():
    return render_template("base.html")

@views.route("/posts", strict_slashes=False)
def posts():
    return render_template("posts.html")

@views.route("/publish", strict_slashes=False)
def publish():
    return render_template("publish.html")