from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name=None):
	return 'Hello {}!'.format(name)
