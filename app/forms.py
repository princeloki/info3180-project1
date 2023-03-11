from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, FileField, IntegerField, TextAreaField, SelectField, DecimalField, SubmitField
from wtforms.validators import InputRequired

class PropertiesForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    no_bedrooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    no_bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired()])
    type = SelectField('Property Type', 
                       choices=[
                           ('house', 'House'),
                           ('apartment', 'Apartment')
                       ])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[
        FileAllowed(['jpg', 'png'], 'Images only'),
        FileRequired()
    ])
    
    submit = SubmitField('Add Property')