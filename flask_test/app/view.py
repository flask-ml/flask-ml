from flask import Flask, request, g, render_template, flash, redirect, session, url_for
# from flask.wtf.csrf import CSRFProtect
from flask.ext.bootstrap import Bootstrap
from model import *
from form import *
import sys
sys.path.append('..')
from Algorithm.Classification.src.SVM import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adsfhgasfkjhkj'
# CSRFProtect(app)
Bootstrap(app)


@app.before_request
def before_request():
    g.user = None
    s = Session()
    if 'email' in session:
    	g.user = s.query(User).filter(User.email == session['email']).first()
    	print(g.user)


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
	"""
	游客模式
	"""
	# if not g.user:
	# 	return render_template('index.html')

	# test svm
	if request.method == 'POST':
		if request.form['svm-param']:
			svm_score = get_svm(float(request.form['svm-param']))
			return render_template('index.html', svm_score = svm_score)
	return render_template('index.html')
	
@app.route('/login', methods = ['GET', 'POST'])
def login():	
	form  = LoginForm(request.form)
	if form.validate_on_submit():
		user = query_user(form.email.data)
		print(user)
		session['email'] = classToDict(user)['email']
		print(session['email'])
		return redirect(url_for('index'))
	return render_template('login.html', form = form, title_name = "Login")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
	"""
	清空session里保存的当前用户
	"""
	flash('You were logged out')
	session.pop('user_id', None)
	return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	if form.validate_on_submit():
		add_user(form.email.data,
			form.username.data,
			form.password.data)
		flash('Thanks for registering')
		return redirect(url_for('login'))
	return render_template('register.html', title_name = "Register", form=form)



if __name__ == '__main__':
	app.run()
