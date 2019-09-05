import time 

from apscheduler.schedulers.background import BackgroundScheduler 

def print_dtime():
		print "hello"

scheduler = BackgroundScheduler()
scheduler.add_job(func=print_dtime,trigger="interval",seconds=3)
scheduler.start()

