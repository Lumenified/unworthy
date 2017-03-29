#third party imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

#application imports
from ..models import Employee

class RegistrationForm(FlaskForm):
    """
    FlaskForm instead a normal Form to implement the proper ~FORM~
    """
    """E-mail Section"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')
    def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError(message='Email is already in use.')

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError(message='Username is already in use.')

class LoginForm(FlaskForm):
    """
    I recently learned that the object "Form" of flask is deprecated so we
    use FlaskForm as an object
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
