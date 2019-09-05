import os 
import json
from TwiClient import *
basedir = os.path.abspath(os.path.dirname(__file__))
 
def tweepy_scheduler():
	#print('hello')
	initScrap() # schedule the scrapping 

class Config(object):
	JOBS = [ { 'id': 'job1','func': tweepy_scheduler,'args': (),'trigger': 'interval','seconds': 2 }]
	SCHEDULER_API_ENABLED = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'asdfghjkl' # prevent CSRF attacks
	#Data base scripts 
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'app.db') # path to database
	SQLALCHEMY_TRACK_MODIFICATIONS = False	# ignore
		
