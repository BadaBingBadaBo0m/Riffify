from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired

ALLOWED_EXTENSIONS = {"mp3"}

class SongForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    song_body = FileField('Song body', validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    