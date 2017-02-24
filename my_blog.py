from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return app.send_static_file('about.html')

@app.route('/birthday')
def birthday():
	return app.send_static_file('birthday.html')

@app.route('/post/<int:postnum>')
def post(postnum):
	return 'This is post {}'.format(postnum)

@app.route('/greeting/<string:name>')
def greeting(name):
	return 'Hello {}'.format(name)