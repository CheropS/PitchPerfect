from flask.helpers import url_for
from app.main.forms import PitchForms, ProfileUpdateForm
from app.models import Pitch, User
from flask import render_template
from . import main
from flask_login import login_required
from flask import render_template, redirect, url_for, abort, request
from ..import db, photos
from dataclasses import dataclass


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')



@main.route('/New-Pitch', methods=['POST', 'GET'])
@login_required
def new_pitch():
    form = PitchForms()
    if form.validate_on_submit():
        pitch_id=form.id.data
        title=form.title.data
        category=form.category.data
        pitch=form.pitch.data

        #updating pitch instance
        new_pitch=Pitch(pitch_id=pitch_id, title=title, category=category, pitch=pitch)

        #save review method
        new_pitch.save_pitch()
        return redirect(url_for('pitch', id=pitch_id))
    title=f'{{pitch.title}} pitch'
    return render_template('new_pitch.html',title = title, PitchForms=form)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = ProfileUpdateForm()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@dataclass
class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

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
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls, id):
        return Downvotes.query.filter_by(pitch_id=id).all()

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'