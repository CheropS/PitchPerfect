from flask.helpers import url_for
from app.main.forms import PitchForms
from app.models import Pitch
from flask import render_template
from . import main
from flask_login import login_required
from flask import render_template, redirect, url_for

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

# @main.route('/New_Pitch', methods=['POST', 'GET'])
# @login_required
# def newpitch():
#     form=PitchForms()
#     if form.validate_on_submit():

# '''
# route:new pitch
# comments(id)
# user updates-profile
# user updates-picture
# upvote(pitch_id)
# downvote(pitch_id)

# '''
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


