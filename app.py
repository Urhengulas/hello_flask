from flask import Flask, request
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_login()
    else:
        return show_login_form()


def do_login():
    return "<h3>logging you in<h3/>"


def show_login_form():
    return """
    <form>
        Username:<br>
        <input type="text" name="username"><br>
        Password:<br>
        <input type="text" name="password">
    </form>
    """
