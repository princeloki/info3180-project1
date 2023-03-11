from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, FileField, IntegerField, TextAreaField, SelectField, DecimalField, SubmitField
from wtforms.validators import InputRequired

class PropertiesForm(FlaskForm):
    title = StringField('title', validators=[InputRequired()])
    no_bedrooms = IntegerField('no_bedrooms', validators=[InputRequired()])
    no_bathrooms = IntegerField('no_batthrooms', validators=[InputRequired()])
    location = StringField('location', validators=[InputRequired()])
    price = IntegerField('price', validators=[InputRequired()])
    type = SelectField('type', 
                       choices=[
                           ('house', 'House'),
                           ('apartment', 'Apartment')
                       ])
    description = TextAreaField('description', validators=[InputRequired()])
    photo = FileField('image', validators=[
        FileAllowed(['jpg', 'png'], 'Images only'),
        FileRequired()
    ])
    
    submit = SubmitField('Add Property')