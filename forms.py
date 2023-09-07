"""Forms"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, EmailField
import email_validator
from wtforms.validators import InputRequired, Length, Email, EqualTo
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField


class SignUpForm(FlaskForm):
    first_name = StringField(validators=[InputRequired(), Length(min=2, max=50)])
    last_name = StringField(validators=[InputRequired(), Length(min=2, max=50, message="Name too short")])
    email = EmailField(validators=[InputRequired(), Email(message="Enter a valid email")])
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20, message="Password must be at least 4 characters")])
    confirm_pwd = PasswordField(validators=[InputRequired(), Length(min=4, max=20), EqualTo("password", message="Passwords must match!")])
    

class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    password = PasswordField(validators=[InputRequired()])
    

class PostForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    slug = StringField("Slug", validators=[InputRequired()])
    content = CKEditorField("Content", validators=[InputRequired()])
    
    
class UserForm(FlaskForm):
    first_name = StringField(validators=[InputRequired(), Length(min=2, max=50)])
    last_name = StringField(validators=[InputRequired(), Length(min=2, max=50, message="Name too short")])
    email = EmailField(validators=[InputRequired(), Email(message="Enter a valid email")])
    about = StringField(widget=TextArea())
    profile_pic = FileField("Profile Picture")