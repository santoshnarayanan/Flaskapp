from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

'''
This below line is not required as it is configuration parameter in flask version 1.02
'''
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

tags = db.Table('post_tags',
                db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                )

class User(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user',lazy='dynamic')
    # posts = db.relationship('Post')

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    tags = db.relationship('Tag',secondary=tags,backref=db.backref('posts', lazy='dynamic'))


    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Post '{}'>".format(self.title)


class Tag(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(255))

    def __init__(self,title):
        self.title = title

    def __repr__(self):
        return "<Tag '{}'>".format(self.title)


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))

    def __repr__(self):
        return "<Comment '{}'>".format(self.text[:15])

@app.route('/')
def hello_world():
    return 'Hello World!!!!'


if __name__ == '__main__':
    app.run()
