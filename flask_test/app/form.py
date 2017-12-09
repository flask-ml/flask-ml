from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, PasswordField, StringField,validators
from model import *

class LoginForm(Form):
    name = StringField('email or name', [
    validators.InputRequired("请输入正确的用户名")
    ])
    pw = PasswordField('pw', [validators.InputRequired()])


    def validate(self):
        if not Form.validate(self):
            return False
        user = query_user(self.name.data)
        if user is None:
            self.name.errors.append('用户名不存在！')
            return False
        if user.pw != self.pw.data:
            self.pw.errors.append('密码错误！')
            return False
        return True


class RegistrationForm(Form):
    username = TextField('usernamee', [validators.Length(min=6, max=25, message='密码应在6-25之间！')])
    email = TextField('Email Address', [validators.Length(min=6, max=135),validators.Email()])
    password = PasswordField('New Password', [
        validators.InputRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.InputRequired()])

    def validate(self):
        if not Form.validate(self):
            return False
        user = query_user(self.username.data)
        if user != None:
            self.username.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True
        

