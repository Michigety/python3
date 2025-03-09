from flask import Blueprint, request, url_for, redirect, render_template
from flaskr.models import *

bp = Blueprint('board', __name__, url_prefix='/board')

@bp.route('/', methods=['GET', 'POST'])
def board():
    page = request.args.get('page', type=int, default=1)
    posts = Post.query.order_by(Post.created.desc())
    posts_pagination = posts.paginate(page=page, per_page=10)
    return render_template('board.html', posts=posts_pagination)


