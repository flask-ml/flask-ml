from flask import Flask, request, g, render_template, flash, redirect, session, url_for
from flask_test.Algorithm.Classification.src.SVM import get_svm

app = Flask(__name__)

@app.route('/')
def index():
	svm = get_svm(0.2)
	return render_template('base.html', svm=svm)

if __name__ == '__main__':
	app.run()



