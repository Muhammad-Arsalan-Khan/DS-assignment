from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="enter the username"), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired("email is required"), Email("enter a valid email address")])
    password = PasswordField('Password', validators=[DataRequired("password is required"), Length(min=6 , message="password should be at least 6 characters long")])
    submit = SubmitField('Register')    