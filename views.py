from flask import Blueprint, render_template, flash
from flask_login import login_required
from forms import PostForm
from models import Post
from app import db

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
@login_required
def home():
    return render_template("base.html")

# View all posts
@views.route("/posts", strict_slashes=False)
@login_required
def posts():
    posts = Post.query.order_by(Post.date_posted)
    return render_template("posts.html", posts=posts)

#View post by id
@views.route("/posts/<int:id>")
def post(id):
    post = Post.query.get_or_404(id)
    return render_template("post.html", post=post)

#Publish content
@views.route("/publish", methods=["GET", "POST"], strict_slashes=False)
@login_required
def publish():
    form = PostForm()
    
    if form.validate_on_submit():
        post = Post(title=form.title.data, author=form.author.data, slug=form.slug.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        form.title.data = ''
        form.author.data = ''
        form.slug.data = ''
        form.content.data = ''
        flash("Created successfully!", "success")
    return render_template("publish.html", form=form)