import uuid

from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash

from flaskr.models import *
from flaskr.form import SignUpForm

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    obj = {
        'title': 'Hello World',
        'name': 'Flask',
        'content': 'go to board'
    }
    return render_template('index.html', obj=obj)


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            u = User(
                id = str(uuid.uuid4()),
                username = form.username.data,
                password = generate_password_hash(form.password.data),
                email = form.email.data,
                created = datetime.now()
            )
            db.session.add(u)
            db.session.commit()
        else:
            flash('The user already exists.')
        return redirect(url_for('main.signup'))
    return render_template('signup.html', form=form)