from flask import Flask, request, g, render_template, flash, redirect, session, url_for
from model import *
from form import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adsfhgasfkjhkj'  

@app.before_request
def before_request():
    g.user = None
    s = Session()
    if 'user_name' in session:
    	g.user = s.query(User).filter(User.name == session['user_name']).first()


@app.route('/', methods = ['GET', 'POST'])
def index():
	"""
	游客模式
	"""
	# if not g.user:
	# 	return render_template('index.html')
	return render_template('index.html')
	
@app.route('/login', methods = ['GET', 'POST'])
def login():	
	"""
	登陆
	"""
	login_form  = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		user = query_user(form.name.data)
		session['user_name'] = classToDict(user)
		return redirect(url_for('index'))
	return render_template('login.html')


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
	if request.method == 'POST' and form.validate():
		add_user( form.email.data,
			form.username.data,
			form.password.data)
		flash('Thanks for registering')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)



if __name__ == '__main__':
	app.run()
