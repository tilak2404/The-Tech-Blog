from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,TextAreaField

from wtforms.validators import DataRequired

class BlogPostForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    text=TextAreaField('Text',validators=[DataRequired()])
    submit=SubmitField('Post')
    