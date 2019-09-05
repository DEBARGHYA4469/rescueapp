# script for web forms
from flask_wtf import FlaskForm 
from wtforms import StringField,SelectField,PasswordField,BooleanField,SubmitField,IntegerField,RadioField,TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User,Status 

class LoginForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired()])
	password = PasswordField('Password', validators= [DataRequired()])
	remember_me = BooleanField('Remember_Me')
	submit = SubmitField('Sign In')
	
class RegistrationForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired()])
	email = StringField('Email',validators=[DataRequired(),Email()])
	phone = StringField('Telephone', [DataRequired()])
	password = PasswordField('Password',validators=[DataRequired()])
	password2 = PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('Register')
	
	def validate_username(self,username):
		user= User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')
	
	def validate_email(self,email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email address')


class Status_Update(FlaskForm):
	username = StringField('Username', validators = [DataRequired()])
	password = PasswordField('Password', validators= [DataRequired()])
	phone = StringField('Telephone', [DataRequired()])
	who = RadioField('I am a ', choices = [("vic",'Victim'),("vol",'Volunteer')])
	help = IntegerField("How much help have you received?")
	danger = IntegerField("Rate your danger level in the disaster")
	complaints = TextAreaField("What help do you need?")
	disaster = SelectField(label='disaster?',choices=[('earthquake','earthquake'),('flood','flood'),('volcano','volcano'),('fire','fire'),('wind','wind'),('landslide','landslide')])
	submit = SubmitField('Update Your Status')
	
