from flask import Flask, request, g, render_template, flash, redirect, session, url_for
from flask_ml.flask_test.Algorithm.Classification.src.SVM import main

app = Flask(__name__)

@app.route('/')
def index():
	svm = main(0.2)
	return render_template('base.html', svm=svm)

if __name__ == '__main__':
	app.run()
