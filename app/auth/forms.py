#registering users
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Email, EqualTo
from ..models import User
from wtforms import ValidationError
#registering users
#login users
from wtforms import StringField,PasswordField,BooleanField,SubmitField
#login users


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address')
    username = StringField('Enter your username',validators = [])
    password = PasswordField('Password',validators = [ EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [])
    submit = SubmitField('Sign Up')
    
    #custom validators
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')
        
        #registering users