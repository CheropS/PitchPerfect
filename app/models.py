
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from dataclasses import dataclass


@login_manager.user_loader
def load_user(pitch_id):
    return User.query.get(int(pitch_id))

# class Pitch(db.Model):
#     __tablename__='pitch'
#     '''This is a class that defines Pitch class
#     '''
#     id=db.Column(db.Integer, primary_key= True)
#     category=db.Column(db.String(255))
#     title=db.Column(db.String(255))
#     description=db.Column(db.Text())
#     pitch=db.Column(db.Text())
#     publishedtime=db.Column(db.DateTime, default=datetime.utcnow)
#     upvote=db.relationship('Upvote', backref='pitch', lazy='dynamic')
#     downvote=db.relationship('Downvote', backref='pitch', lazy='dynamic')
#     comment=db.relationship('Comment', backref='pitch', lazy='dynamic')
#     pass_secure = db.Column(db.String(255))

#     def save_pitch(self):
#         db.session.add(self)
#         db.session.commit()

#     def delete_pitch(self):
#         db.session.delete(self)
#         db.session.commit()

#     def __repr__(self):
#         return f'Pitch {self.post}'

#     @property
#     def password(self):
#             raise AttributeError('You cannot read the password attribute')

#     @password.setter
#     def password(self, password):
#             self.pass_secure = generate_password_hash(password)


#     def verify_password(self,password):
#             return check_password_hash(self.pass_secure,password)


  
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    bio=db.Column(db.String(255))
    pic=db.Column(db.String(255))
    email=db.Column(db.String(255), unique=True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    upvote=db.relationship('Upvote', backref='pitch', lazy='dynamic')
    downvote=db.relationship('Downvote', backref='pitch', lazy='dynamic')
    comment=db.relationship('Comment', backref='pitch', lazy='dynamic')
    password_hash = db.Column(db.String(255))

    

    def __repr__(self):
        return f'User {self.username}'

class UPitch(db.Model):
    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    title=db.Column(db.String(255))
    category=db.Column(db.String(255))
    description=db.Column(db.String(255))
    pitch=db.Column(db.Text())
    publishedtime=db.Column(db.DateTime, default=datetime.utcnow)
    upvote=db.relationship('Upvote', backref='pitch', lazy='dynamic')
    downvote=db.relationship('Downvote', backref='pitch', lazy='dynamic')
    comment=db.relationship('Comment', backref='pitch', lazy='dynamic')
    pass_secure = db.Column(db.String(255))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def delete_pitch(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'UPitch {self.post}'

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

@dataclass
class Upvote(db.Model):
    __tablename__ = 'upvote'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls, id):
        return Upvote.query.filter_by(pitch_id=id).all()

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'


@dataclass
class Downvotes(db.Model):
    __tablename__ = 'downvote'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls, id):
        return Downvotes.query.filter_by(pitch_id=id).all()

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'

    
'''
class user-bio, email, username,pic db.relationship(1:many)
comments-userid, pitchid, comment
upvote
downvote-id,pitch
'''