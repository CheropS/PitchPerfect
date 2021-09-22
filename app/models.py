from sqlalchemy.orm import backref
from . import db

class Pitch:
    '''This is a class that defines Pitch class
    '''

    def __init__(self, id, category, title, description):
        self.id=id
        self.category=category
        self.title=title
        self.description=description

class User:
    '''
    This is a class that defines a user's bio data
    '''

    def __init__(self, user_id, bio, username, picture):
        self.user_id=user_id
        self.bio=bio
        self.username=username
        self.pic=picture 

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    bio=db.Column(db.String(255))
    pic=db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'User {self.username}'

class UPitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title=db.Column(db.String(255))
    category=db.Column(db.String(255))
    description=db.Column(db.String(255))
    pitch=db.Column(db.Text())
    publishedtime=db.Column(db.DateTime)
    upvote=db.relationship('Upvote', backref='pitch', lazy='dynamic')
    downvote=db.relationship('Downvote', backref='pitch', lazy='dynamic')
    comment=db.relationship('Comment', backref='pitch', lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def delete_pitch(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Pitch {self.post}'
    
'''
class user-bio, email, username,pic db.relationship(1:many)
comments-userid, pitchid, comment
upvote
downvote-id,pitch
'''