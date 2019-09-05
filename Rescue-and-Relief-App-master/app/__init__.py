from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_apscheduler import APScheduler

app = Flask(__name__) # create an instance of Flask class.
app.config.from_object(Config)
db = SQLAlchemy(app) # create an instance of SQL database
login = LoginManager(app) # logging in instance 
login.login_view = 'login'

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()



#app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
#app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

#celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
#celery.conf.update(app.config)

#@celery.task
#def my_background_task(arg1,arg2):
#	print "hello"

#task = my_background_task.delay(10,20)

#This py file is called when app is instantiated!
from app import views,models # prevent circular imports

