from app.main.forms import PitchForms
from app.models import Pitch
from flask import render_template
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/New_Pitch', methods=['POST', 'GET'])
@login_required
def newpitch():
    form=PitchForms()
    if form.validate_on_submit():
        
'''
route:new pitch
comments(id)
user updates-profile
user updates-picture
upvote(pitch_id)
downvote(pitch_id)

'''