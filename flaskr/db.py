from flask import current_app, g

import pymongo


def init_app(app):

    db = get_db()
    db.posts.create_index(
        keys=[('post_id', pymongo.ASCENDING)],
        unique=True,
        min=1,
    )
    # app.teardown_appcontext(close_db)


def get_db() -> pymongo.database.Database:

    if 'db' not in g:
        client = pymongo.MongoClient(
            host=current_app.config['MONGO_HOST'],
            username='root',  # TODO: put username, password into ./instance/config.py
            password='example',
        )
        g.db = client.flaskr

    return g.db


# def close_db(e=None):

#     db = g.pop('db', None)

#     if db is not None:
#         db.close()
