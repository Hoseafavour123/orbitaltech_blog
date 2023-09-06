"""Models"""
from flask_login import UserMixin
from datetime import datetime
from app import db

# User Class
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    about_author = db.Column(db.String(150), nullable=True, default="")
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)
    profile_pic = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return f"[{self.first_name} {self.last_name} - {self.email}]"
    
    def number_of_posts(self):
        posts = 0
        for post in Post.query.all():
            if post.user_id == self.id:
                posts += 1
        return posts
    
    
# Blog Post
class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("users.id"))
    title = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    slug = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(10000), nullable=False)
    
    author = db.relationship(User, backref="posts")
    
    