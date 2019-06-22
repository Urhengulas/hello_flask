from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<string:name>/')
def hello_name(name=None):
    try:
        name = name.title()
    except:
        pass

    return render_template('hello.html', name=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template("do_login.html")
    else:
        return render_template("login_form.html")
