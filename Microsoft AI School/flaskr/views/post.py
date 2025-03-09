from datetime import datetime

from flask import Blueprint, request, redirect, render_template, url_for
from flaskr import db
from flaskr.form import PostForm
from flaskr.models import Post

bp = Blueprint('post', __name__, url_prefix='/board/post')

@bp.route('/', methods=['GET', 'POST'])
def index():
    return 'asdf'


@bp.route('/write', methods=['GET', 'POST'])
def write():
    form = PostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            post = Post(user="admin", title=form.title.data, content=form.content.data, created=datetime.now())
            db.session.add(post)
            db.session.commit()
            return redirect('board.index')
    else:
        return render_template('post_write.html', form=form)


