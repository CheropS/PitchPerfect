from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField, TextAreaField
from wtforms.fields.core import StringField
from wtforms.validators import required

class PitchForms(FlaskForm):

    title=StringField('Pitch title', validators=[required()])
    category=SelectField('pitch category', validators=[required()])
    pitch=TextAreaField('pitch written here', validators=[required()])
    submit=SubmitField('Submit')


class CommentForms(FlaskForm):

    comment=TextAreaField('what do you think', validators=[required()])
    submit=SubmitField

class ProfileUpdateForm(FlaskForm):

    bio=TextAreaField('tell us about you', validators=[required()])
    submit=SubmitField('Submit')
    