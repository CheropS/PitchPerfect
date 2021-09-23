from flask.helpers import url_for
from app.main.forms import PitchForms, ProfileUpdateForm
from app.models import User, UPitch, Upvote, Downvotes
from flask import render_template
from . import main
from flask_login import login_required, current_user
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
        new_pitch=UPitch(pitch_id=pitch_id, title=title, category=category, pitch=pitch)

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


@main.route('/like/<int:pitch_id>', methods=['POST', 'GET'])
@login_required
def like(pitch_id):
    get_pitches = Upvote.get_upvotes(pitch_id)
    valid_string = f'{current_user.id}:{pitch_id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string + " " + to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index', id=pitch_id))
        else:
            continue
    new_vote = Upvote(user=current_user, pitch_id=pitch_id)
    new_vote.save()
    return redirect(url_for('main.index', pitch_id=pitch_id))


@main.route('/dislike/<int:pitch_id>', methods=['POST', 'GET'])
@login_required
def dislike(pitch_id):
    pitch = Downvotes.get_downvotes(pitch_id)
    valid_string = f'{current_user.id}:{pitch_id}'
    for p in pitch:
        to_str = f'{p}'
        print(valid_string + " " + to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index', id=pitch_id))
        else:
            continue
    new_downvote = Downvotes(user=current_user, pitch_id=pitch_id)
    new_downvote.save()
    return redirect(url_for('main.index', pitch_id=pitch_id))