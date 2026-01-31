from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,equal_to
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from Thetechblog.model import User

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),equal_to('pass_confirm',message='Passwords must match')])
    pass_confirm=PasswordField('Confirm Password',validators=[DataRequired()])
    submit=SubmitField('Create Account')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first() and field.data != current_user.email:
            raise ValidationError('Your email has already been registered')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first() and field.data != current_user.username:
            raise ValidationError('Your username has already been registered')
        
class UpdateUserForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('Username',validators=[DataRequired()])
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Update')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first() and field.data != current_user.email:
            raise ValidationError('Your email has already been registered')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first() and field.data != current_user.username:
            raise ValidationError('Your username has already been registered')
    