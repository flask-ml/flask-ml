from flask.ext.wtf import Form
# from flask.wtf.csrf import CSRFProtect
from wtforms import TextField, BooleanField, TextAreaField, PasswordField, StringField,validators,SubmitField, SelectField
from flask.ext.wtf.file import FileField, FileAllowed, FileRequired
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
        

class SvmForm(Form):
    C = SelectField('C', choices=[
        (0.1, '0.1'),
        (1, '1'),
        (10, '10'),
        (100, '100'),
    ], coerce=float)
    kernel = SelectField('kernel', choices=[
        ('rbf', 'rbf'),
        ('linear', 'linear'),
        ('poly', 'ploy'),
        ('sigmoid', 'sigmoid'),
    ])
    max_iter = SelectField('max_iter', choices=[
        (1, '1'),
        (10, '10'),
        (100, '100'),
    ], coerce=int)
    gamma = SelectField('gamma', choices=[
        ('auto', 'auto'),
    ])
    random_state = SelectField('random_state', choices=[
        (1, '1'),
        (10, '10'),
        (100, '100'),
    ], coerce=int)
    test_size = SelectField('test_size', choices=[
        (0.1, '0.1'),
        (0.2, '0.2'),
        (0.3, '0.3'),
    ], coerce=float )
    play = SubmitField('Play')


class XGBoostForm(Form):
    gamma = SelectField('gamma', choices=[
        (0.1, '0.1'),
        (0.2, '0.2'),
        (0.3, '0.3'),
    ])
    max_depth = SelectField('max_depth', choices=[
        (1, '1'),
        (10, '10'),
        (100, '100'),
    ])
    learning_rate = SelectField('learning_rate', choices=[
        (0.001, '0.001'),
        (0.002, '0.002'),
        (0.01, '0.01'),
    ])
    test_size = SelectField('test_size', choices=[
        (0.1, '0.1'),
        (0.2, '0.2'),
        (0.3, '0.3'),
    ])
    play = SubmitField('Play')


class NaiveBayesForm(Form):
    kernel = SelectField('kernel', choices=[
        ('GuassianNB', 'GuassianNB'),
        ('MultinomialNB', 'MultinomialNB'),
        ('BernoulliNB', 'BernoulliNB'),
    ])
    random_state = SelectField('random_state', choices=[
        (1, '1'),
        (10, '10'),
        (100, '100'),
    ])
    test_size = SelectField('test_size', choices=[
        (0.1, '0.1'),
        (0.2, '0.2'),
        (0.3, '0.3'),
    ])
    play = SubmitField('Play')


class KNNForm(Form):
    n_neighbors = SelectField('n_neighbors', choices=[
        (5, '5'),
        (10, '10'),
        (100, '100'),        
    ])
    algorithm = SelectField('algorithm', choices=[
        ('auto', 'auto'),
    ])
    random_state = SelectField('random_state', choices=[
        (1, '1'),
        (10, '10'),
        (100, '100'),
    ])
    test_size = SelectField('test_size', choices=[
        (0.1, '0.1'),
        (0.2, '0.2'),
        (0.3, '0.3'),
    ])
    play = SubmitField('Play')


class DTreeForm(Form):
    criterion = SelectField('criterion', choices=[
        ('gini', 'gini'),
    ])
    min_samples_split = SelectField('min_samples_split', choices=[
        (2, '2'),
        (4, '4'),
        (6, '6'),
        (8, '8'),
    ])
    max_features = SelectField('max_features', choices=[
        (None, 'None'),
    ])
    random_state = SelectField('random_state', choices=[
        (1, '1'),
        (10, '10'),
        (100, '100'),
    ])
    test_size = SelectField('test_size', choices=[
        (0.1, '0.1'),
        (0.2, '0.2'),
        (0.3, '0.3'),
    ])
    play = SubmitField('Play')



class UploadForm(Form):
    """
    upload file
    """
    file = FileField('Upload', validators=[
        FileAllowed(['csv', 'xls', 'xlsx'], "Format of upload file can't distinguish"),
        FileRequired("no file upload")
        ])
    submit = SubmitField('Upload')