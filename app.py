from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def index():
    hello = "<a href=/hello>Say Hello<a/>"
    path = "<a href=/path/i/am/a/path>Dig deep<a/>"
    routes = [hello, path]
    return "<br>".join(routes)


@app.route('/hello/')
def hello_flask():
    return f'Hello, Flask!'


@app.route('/hello/<string:name>/')
def hello_name(name):
    return f'Hello, {name.title()}!'


@app.route('/path/<path:subpath>/')
def show_subpath(subpath):
    return f'Subpath: {subpath}'


print("\n### OUTPUT ###")
with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello_name', name='anna'))
print("##############\n")
