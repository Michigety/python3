import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

BASEDIR = os.path.dirname(__file__)

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=convention))
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    if os.path.exists(os.path.join(BASEDIR, 'config.py')):
        app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    from . import models

    from .views import main, board, post
    app.register_blueprint(main.bp)
    app.register_blueprint(board.bp)
    app.register_blueprint(post.bp)

    return app
