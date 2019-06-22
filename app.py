from flask import Flask
app = Flask(__name__)


@app.route('/hello/')
def hello_flask():
    return f'Hello, Flask!'


@app.route('/hello/<string:name>/')
def hello_name(name):
    return f'Hello, {name.title()}!'
