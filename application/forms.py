from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from . import photos

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class AddProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    tags = StringField('Tags', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    colour = StringField('Colour', validators=[DataRequired()])
    primary_image = FileField(validators=[FileAllowed(photos, 'Primary Image'), FileRequired('File was empty!')])
    secondary_image = FileField(validators=[FileAllowed(photos, 'Secondary Image'), FileRequired('File was empty!')])
    tertiary_image = FileField(validators=[FileAllowed(photos, 'Tertiary Image'), FileRequired('File was empty!')])
    ean = StringField('EAN', validators=[DataRequired()])
    price = StringField("Price", validators=[DataRequired()])
    currency = StringField("Currency", validators=[DataRequired()])
    submit = SubmitField('Add Product')