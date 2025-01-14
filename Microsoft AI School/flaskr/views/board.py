from flask import Blueprint, request, url_for, redirect, render_template
from flaskr.models import *

bp = Blueprint('board', __name__, url_prefix='/board')

@bp.route('/')
def index():
    page = request.args.get('page', type=int, default=1)
    board = Board.query.order_by(Board.created.desc())
    board_pagination = board.paginate(page=page, per_page=10)
    return render_template('board.html')

