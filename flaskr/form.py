from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.fields.simple import PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    content = StringField('content', validators=[DataRequired()])


class SignUpForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=1, max=16)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)])
    password_validation = PasswordField('confirm the password', validators=[DataRequired(), EqualTo('password')])
    email = EmailField('email', validators=[DataRequired(), Email()])

class SignInForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=1, max=16)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)])

