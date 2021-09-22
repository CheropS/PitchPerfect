from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField, TextAreaField
from wtforms.fields.core import StringField
from wtforms.validators import required

class PitchForms(FlaskForm):

    title=StringField('Pitch title')
    category=SelectField('pitch category')
    pitch=TextAreaField('pitch written here')
    submit=SubmitField
    '''
    define based on reviews last week IP
    category-selectfield
    title-stringfield
    pitch-textarea
    submit-submitfield'''

class CommentForms(FlaskForm):
    '''
    two fields 
    comment-textarea
    submit-submitfield
    '''

class ProfileUpdateForm(FlaskForm):
    '''
    bio-textarea
    submit-submit
    note:required needed in all classes
    '''