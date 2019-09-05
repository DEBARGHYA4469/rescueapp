from app import db 
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin
from app import login # object holding the login instance 
from datetime import datetime

class User(UserMixin,db.Model): # userMixin implements auth,active,id
	id = db.Column(db.Integer,primary_key=True) # set the primary key to be the id
	username = db.Column(db.String(64),index=True,unique=True)
	email = db.Column(db.String(120),index=True,unique=True)
	phone = db.Column(db.String(120),index=True,unique=True)
	password_hash = db.Column(db.String(128))
	status = db.relationship('Status',backref='us',lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.format(self.username)
		
	def set_password(self,password):
		self.password_hash = generate_password_hash(password)
		
	def check_password(self,password):
		return check_password_hash(self.password_hash,password)

class Status(UserMixin,db.Model):
	id  = db.Column(db.Integer,primary_key=True)
	who = db.Column(db.String) # victim or the volunteer
	timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
	help = db.Column(db.Integer)
	danger = db.Column(db.Integer)
	latitude = db.Column(db.String)
	longitude = db.Column(db.String)
	disaster = db.Column(db.String)
	complaints = db.Column(db.String(140))
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

	def __repr__(self):
		return '< Status {} >'.format(self.complaints)
				
@login.user_loader
def load_user(id):
	return User.query.get(int(id)) # id to identify the user...
	
	
	
