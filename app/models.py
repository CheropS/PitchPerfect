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

    def __repr__(self):
        return f'User {self.username}'

'''
class user-bio, email, username,pic db.relationship(1:many)
comments-userid, pitchid, comment
upvote
downvote-id,pitch
'''