import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    """Show all posts"""

    posts = get_db().posts.find()

    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    # POST: write post to db (title, body, user_id) -> redirect to index
    # GET: show form to write post (title, body)
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post = create_post(
                title=title,
                body=body,
            )
            get_db().posts.insert_one(post)

            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


@bp.route('/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update(id: int):

    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            post = create_post(
                title=title,
                body=body,
                post_id=id,
            )

            db = get_db()
            db.posts.replace_one(
                filter={'post_id': id},
                replacement=post,
            )

            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id: int):
    post = get_post(id)  # called to check existence and permissions

    db = get_db()
    db.posts.delete_one({'post_id': id})

    return redirect(url_for('blog.index'))


def create_post(title: str, body: str, post_id=None) -> dict:

    db = get_db()
    user_id = g.user['_id']
    user_name = db.user.find_one({'_id': user_id})['username']

    if post_id is None:
        post_id = calc_post_id()

    post = {
        'post_id': post_id,
        'title': title,
        'body': body,
        'created': datetime.datetime.now(),
        'author': {
            '_id': user_id,
            'username': user_name,
        },
    }
    return post


def get_post(id: int, check_author=True) -> dict:

    db = get_db()
    post = db.posts.find_one({'post_id': id})

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author is True and post['author']['_id'] != g.user['_id']:
        abort(403)

    return post


def calc_post_id():

    post_col = get_db().posts
    num_posts = post_col.count_documents({})

    if num_posts == 0:
        return 1

    for post_id in range(1, num_posts + 2):
        if post_col.find_one({'post_id': post_id}) is None:
            return post_id
