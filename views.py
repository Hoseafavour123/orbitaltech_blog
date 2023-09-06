from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from forms import PostForm, UserForm
from models import Post, User
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
    posts = Post.query.order_by(Post.date_posted)
    return render_template("home.html", posts=posts)

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
        post = Post(title=form.title.data, user_id=current_user.id, slug=form.slug.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        form.title.data = ''
        form.slug.data = ''
        form.content.data = ''
        flash("Created successfully!", "success")
    return render_template("publish.html", form=form)


#Edit post by id
@views.route("/edit/post/<int:id>", methods=["GET", "POST"], strict_slashes=False)
def edit(id):
    form = PostForm()
    post = Post.query.get_or_404(id)
    
    if post.user_id == current_user.id:
        if form.validate_on_submit():
            post.title = form.title.data
            post.slug = form.slug.data
            post.content = form.content.data
        
            db.session.add(post)
            db.session.commit()
            return redirect(url_for("views.post", id=post.id))
    
        form.title.data = post.title
        form.slug.data = post.slug
        form.content.data = post.content
        return render_template("edit.html", form=form)
    else:
        flash("You can't edit this post!", "danger")
        return redirect(url_for('views.post', id=id))

# Delete Post by id
@views.route("/post/delete/<int:id>")
def delete(id):
    post = Post.query.get_or_404(id)
    
    if post.user_id == current_user.id:
        try:
            db.session.delete(post)
            db.session.commit()
            flash("Post deleted!", "success")
        
            posts = Post.query.order_by(Post.id).all()
            return render_template("home.html", posts=posts)
        except:
            flash("Not successful", "danger")
    else:
        flash("You can't delete post!", "danger")
        return redirect(url_for("views.post", id=id))
        
        
# Search results
@views.route("/search", methods=["POST"], strict_slashes=False)
@login_required
def search():
    searched = request.form.get("searched")
    
    # Search in database
    posts = Post.query.filter(Post.content.like('%' + searched + '%'))
    posts = posts.order_by(Post.title).all()
    
    return render_template("search.html", searched=searched, posts=posts)


# Dashboard
@views.route("/dashboard", methods=["GET", "POST"], strict_slashes=False)
def dashboard():
    form = UserForm()
    
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.email.data = current_user.email
    form.about.data = current_user.about_author
    return render_template("dashboard.html", form=form)


# Update User
@views.route("/users/update/<int:id>", methods=["POST"], strict_slashes=False)
def update_user(id):
    form = UserForm()
    user = User.query.get_or_404(id)
    if form.validate_on_submit():
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data
        user.about_author =  form.about.data
        
        db.session.add(user)
        db.session.commit()
        flash("Updated Successfully!", "success")
        return redirect(url_for("views.dashboard"))
        

# Delete users
@views.route("/users/delete/<int:id>", strict_slashes=False)
@login_required
def delete_user(id):
    try:
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        
        flash("Account Deleted", "danger")
        return redirect(url_for("auth.signup"))
    except Exception as e:
        flash(e, "danger")
        return  render_template("dashboard.html")