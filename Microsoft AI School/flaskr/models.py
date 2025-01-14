from . import db

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
    user = db.relationship('User', backref=db.backref('post_set'))
    author_id = db.Column(db.Text(), db.ForeignKey('user.id', ondelete='CASCADE'))
    title = db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created = db.Column(db.DateTime(), nullable=False)
    modified = db.Column(db.DateTime())

class Comment(db.Model):
    num = db.Column(db.Integer(), primary_key=True)
    user = db.relationship('User', backref=db.backref('comment_set_user'))
    author_id = db.Column(db.Text(), db.ForeignKey('user.id', ondelete='CASCADE'))
    post = db.relationship('Post', backref=db.backref('comment_set_post'))
    post_num = db.Column(db.Text(), db.ForeignKey('post.num', ondelete='CASCADE'))
    body = db.Column(db.Text(), nullable=False)
    created = db.Column(db.DateTime(), nullable=False)
    modified = db.Column(db.DateTime())
