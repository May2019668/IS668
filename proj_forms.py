from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class StudentForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Lastnme', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    major = StringField('Major', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('New Student')

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class AssignmentForm(FlaskForm):
	assignment_title = StringField('Assignment Title', validators=[DataRequired(), Length(min=2, max=200)])
	assignment_number = StringField('Assignment Number', validators=[DataRequired(), Length(min=1, max=3)])
	submit = SubmitField('New Assignment')
				

    		    
