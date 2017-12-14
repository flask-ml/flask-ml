from flask.ext.wtf import Form
# from flask.wtf.csrf import CSRFProtect
from wtforms import TextField, BooleanField, TextAreaField, PasswordField, StringField,validators,SubmitField
from model import *


class LoginForm(Form):
    email = StringField('Email', [
    validators.InputRequired("Please enter correct email..")
    ])
    password = PasswordField('Password', [validators.InputRequired()])
    submit = SubmitField(u'Login')

    def validate(self):
        if not Form.validate(self):
            return False
        user = query_user(self.email.data)
        if user is None:
            self.email.errors.append('The account is not exist.')
            return False
        if user.pw != self.password.data:
            self.password.errors.append('The password is not correct.')
            return False
        return True


class RegistrationForm(Form):
    """
    validators验证不通过可能是因为validators.InputRequired()没加
    """
    username = TextField('Username', [validators.Length(min=5, max=25, message='username should be between 5 and 25')])
    email = TextField('Email Address', [validators.Length(min=6, max=135),validators.Email()])
    password = PasswordField('Password', [
        validators.InputRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Password',[validators.InputRequired()])
    accept_tos = BooleanField('I accept the TOS', [validators.InputRequired()])
    submit = SubmitField('Register')

    def validate(self):
        if not Form.validate(self):
            return False
        user = query_user(self.email.data)
        if user != None:
            self.email.errors.append('This email is already in use. Please choose another one.')
            return False
        return True
        

