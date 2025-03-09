import uuid

from datetime import datetime
from werkzeug.security import generate_password_hash

from flaskr.models import *
from flaskr.form import SignUpForm

from flask import (
    Blueprint, render_template, request, flash, redirect, url_for
)

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    obj = {
        'title': 'Hello World',
        'name': 'Flask',
        'content': 'go to board'
    }
    return render_template('index.html', obj=obj)

