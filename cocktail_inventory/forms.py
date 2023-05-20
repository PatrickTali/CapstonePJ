from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    submit_button = SubmitField()


class IngredientForm(FlaskForm):
    ingredient = StringField('What ingredient would you like to search for?')
    submit = SubmitField()