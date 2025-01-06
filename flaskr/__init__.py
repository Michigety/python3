import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

BASEDIR = os.path.dirname(__file__)

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    if os.path.exists(os.path.join(BASEDIR, 'config.py')):
        app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    @app.route('/')
    def index():
        return app.config['SECRET_KEY']

    return app
