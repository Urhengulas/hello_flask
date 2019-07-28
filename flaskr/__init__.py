import os

from flask import Flask

from . import db, auth, blog


def create_app(test_config=None):
    """create and configure the app"""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MONGO_HOST='mongo',  # change to 'mongo' later
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initialize mongo db
    with app.app_context():
        db.init_app(app)

    # register auth.bp
    app.register_blueprint(auth.bp)

    # register blog.bp
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    @app.route('/hello')
    def hello():
        return "Hello, World!"

    return app
