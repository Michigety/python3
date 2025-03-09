from . import db

# 학습 당시, Question, Answer, User 3개 테이블로 구분했지만,
# 게시판이라는 걸 명확히 하기 위해 Board, Post, Comment, User 4개 테이블로 변경.
# Question ~= Post
# Answer ~= Comment
class User(db.Model):
    id = db.Column(db.Text(), primary_key=True)
    username = db.Column(db.Text(), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    email = db.Column(db.Text(), unique=True, nullable=False)
    created = db.Column(db.DateTime(), nullable=False)

class Board(db.Model):
    id = db.Column(db.Text(), primary_key=True)
    name = db.Column(db.Text(), unique=True, nullable=False)
    desc = db.Column(db.Text())
    created = db.Column(db.DateTime(), nullable=False)
    modified = db.Column(db.DateTime())

class Post(db.Model):
    num = db.Column(db.Integer(), primary_key=True)
    user = db.relationship('User', backref=db.backref('post_set_user'))
    author_id = db.Column(db.Text(), db.ForeignKey('user.id', ondelete='CASCADE'))
    board = db.relationship('Board', backref=db.backref('post_set_board'))
    board_id = db.Column(db.Text(), db.ForeignKey('board.id', ondelete='CASCADE'))
    title = db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created = db.Column(db.DateTime(), nullable=False)
    modified = db.Column(db.DateTime())

class Comment(db.Model):
    num = db.Column(db.Integer(), primary_key=True)
    user = db.relationship('User', backref=db.backref('comment_set_user'))
    author_id = db.Column(db.Text(), db.ForeignKey('user.id', ondelete='CASCADE'))
    post = db.relationship('Post', backref=db.backref('comment_set_post'))
    post_num = db.Column(db.Integer(), db.ForeignKey('post.num', ondelete='CASCADE'))
    content = db.Column(db.Text(), nullable=False)
    created = db.Column(db.DateTime(), nullable=False)
    modified = db.Column(db.DateTime())
