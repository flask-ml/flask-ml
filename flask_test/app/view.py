from flask import Flask, request, g, render_template, flash, redirect, session, url_for
# from flask.wtf.csrf import CSRFProtect
from flask.ext.bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS, IMAGES,\
	patch_request_class
from model import *
from form import *
import os
import sys
sys.path.append('..')
from Algorithm.Classification.src.SVM import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adsfhgasfkjhkj'
app.config['UPLOADED_FILES_DEST'] = os.getcwd() + '\\userfiles'

# CSRFProtect(app)
Bootstrap(app)
files = UploadSet('files', DOCUMENTS)
configure_uploads(app, files)
patch_request_class(app) # 文件大小限制默认为16M


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
	

@app.route('/svm', methods=['GET', 'POST'])
def svm():
	form = SvmForm()
	if form.validate_on_submit():
		C = form.C.data
		kernel = form.kernel.data
		max_iter = form.max_iter.data
		gamma = form.gamma.data
		random_state = form.random_state.data
		test_size = form.test_size.data
		svm_score = get_svm(C, kernel, max_iter, gamma, random_state, test_size)
		return render_template('svm.html', form=form, svm_score=svm_score)
	return render_template('svm.html', form=form)


@app.route('/xgboost', methods=['GET', 'POST'])
def xgboost():
	form = XGBoostForm()
	if form.validate_on_submit():
		gamma = form.gamma.data
		max_depth = form.max_depth.data
		learning_rate = form.learning_rate.data
		test_size = form.test_size.data
		xgboost_score = get_XGB(gamma=gamma, max_depth=max_depth, learning_rate=learning_rate, random_state=random_state, test_size=test_size)
		return render_template('xgboost.html', form=form, xgboost_score=xgboost_score)
	return render_template('xgboost.html', form=form)


@app.route('/naivebayes', methods=['GET', 'POST'])
def naivebayes():
	form = NaiveBayesForm()
	if form.validate_on_submit():
		kernel = form.kernel.data
		random_state = form.random_state.data
		test_size = form.test_size.data
		naivebayes_score = get_NB(kernel=kernel, random_state=random_state, test_size=test_size)
		return render_template('naivebayes.html', form= form, naivebayes_score=naivebayes_score)
	return render_template('naivebayes.html', form=form)



@app.route('/knn', methods=['GET', 'POST'])
def knn():
	form = KNNForm()
	if form.validate_on_submit():
		n_neighbors = form.n_neighbors.data
		kernel = form.kernel.data
		random_state = form.random_state.data
		test_size = form.test_size.data
		naivebayes_score = get_NB(kernel=kernel, random_state=random_state, test_size=test_size)
		return render_template('naivebayes.html', form= form, naivebayes_score=naivebayes_score)
	return render_template('naivebayes.html', form=form)


@app.route('/dtree', methods=['GET', 'POST'])
def dtree():
	form = DTreeForm()
	if form.validate_on_submit():
		criterion = form.criterion.data
		min_samples_split = form.min_samples_split.data
		max_features = form.max_features.data
		random_state = form.random_state.data
		test_size = form.test_size.data
		dtree_score = get_DecisionTree(criterion=criterion, min_samples_split=min_samples_split, max_features=max_features, random_state=random_state, test_size=test_size)	
		return render_template('dtree.html', form=form, dtree_score=dtree_score)
	return render_template('dtree.html', form=form)


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


@app.route('/up', methods=['GET', 'POST'])
def up():
	form = UploadForm()
	if form.validate_on_submit():
		filename = files.save(form.file.data)
		file_url = files.url(filename)
		"""
		handle excel as dataset, return form 
		"""
		return render_template('upload.html', form=form, success=file_url)
	return render_template('upload.html', form=form)


if __name__ == '__main__':
	app.run()
