import uuid

from flaskr import db
from flaskr.models import *
from flaskr.form import *

from datetime import datetime

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    session,
    g
)
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

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
        return redirect(url_for('main.index'))
    return render_template('auth/signup.html', form=form)

@bp.route('signout', methods=['GET', 'POST'])
def signout():
    session.clear()
    g.user = None
    return redirect(url_for('main.index'))

@bp.before_app_request
def load_logged_in_user():
    user = session.get('user')
    if user is None:
        g.user = None