import functools
from bson.objectid import ObjectId

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        error = None

        if not username or not password:
            error = "Username and password are required"
        elif query_user(username) is not None:
            error = f"User {username} is already registered."

        if error is None:
            user = {
                'username': username,
                'password': generate_password_hash(password),
            }
            db.user.insert_one(user)

            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        error = None

        user = query_user(username)

        if user is None or check_password_hash(user['password'], password) is False:
            error = 'Username or password is incorrect.'

        if error is None:
            session.clear()
            session['user_id'] = str(user['_id'])

            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('auth/login.html')


def query_user(name: str) -> dict:

    return get_db().user.find_one({'username': name})


@bp.before_app_request
def load_logged_in_user():

    user_id = ObjectId(session.get('user_id'))

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().user.find_one({'_id': user_id})


@bp.route('/logout')
def logout():

    session.clear()

    return redirect(url_for('index'))


def login_required(view):

    @functools.wraps(view)
    def wrapped_view(**kwargs):

        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
