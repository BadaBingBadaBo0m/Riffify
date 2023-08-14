from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg" }

class PlaylistForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    picture = FileField('Playlist picture', validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])