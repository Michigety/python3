from . import db

class User(db.Model):
    id = db.Column(db.Text(), primary_key=True)
    username = db.Column(db.Text(), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    email = db.Column(db.Text(), unique=True, nullable=False)

class Board(db.Model):
    id = db.Column(db.Text(), primary_key=True)
    name = db.Column(db.Text(), unique=True, nullable=False)
    desc = db.Column(db.Text())
    created = db.Column(db.Datetime(), nullable=False)

class Post(db.Model):
    id = db.Column(db.Text(), primary_key=True)
    user = db.relationship('User')
    author_id = db.Column(db.Text(), db.ForeignKey('user.id', ondelete='CASCADE'))
    title = db.Column(db.Text(), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    created = db.Column(db.Datetime(), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Text(), primary_key=True)
    user = db.relationship('User')
    author_id = db.Column(db.Text(), db.ForeignKey('user.id', ondelete='CASCADE'))
    post = db.relationship('Post')
    post_id = db.Column(db.Text(), db.ForeignKey('post.id', ondelete='CASCADE'))
    body = db.Column(db.Text(), nullable=False)
    created = db.Column(db.Datetime(), nullable=False)
