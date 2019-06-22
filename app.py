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
        try:
            username = request.form['uname']
            password = request.form['psw']

            if validate_login(uname=username, psw=password) == True:
                return render_template('do_login.html')
            else:
                print("LoginError")

        except KeyError:
            print("KeyError")

    return render_template("login_form.html")


def validate_login(uname, psw):
    true_user = "Lisa"
    true_pass = "password123"

    if uname == true_user and psw == true_pass:
        return True
    else:
        return False
