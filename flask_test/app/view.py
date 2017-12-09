from flask import Flask, render_template

from flask_test.Algorithm.Classification.src.SVM import main

app = Flask(__name__)

@app.route('/')
def index():
	svm = main(0.2)
	return render_template('base.html', svm=svm)

if __name__ == '__main__':
	app.run()
