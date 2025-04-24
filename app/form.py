from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    message = TextAreaField('Message: ', validators=[DataRequired()])
    submit = SubmitField('Submit')