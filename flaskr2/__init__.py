import os

from flask import Flask

BASEDIR = os.path.dirname(__file__)

def create_app():
    app = Flask(__name__)

    if os.path.exists(os.path.join(BASEDIR, 'config.py')):
        app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return app.config['SECRET_KEY']

    return app
