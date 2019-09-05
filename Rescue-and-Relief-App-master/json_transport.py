import json 
from app import db,models

from pprint import pprint

users = models.User.query.all() 

json_info = []

for u in users:
	latest_status = u.status.all()[-1] #latest status
	Objinfo = {}
	Objinfo['phone'] = u.phone
	Objinfo['lat'] = latest_status.latitude
	Objinfo['lon'] = latest_status.longitude
	Objinfo['danger'] = latest_status.danger
	Objinfo['who'] = latest_status.who
	Objinfo['help'] = latest_status.help
	Objinfo['complaints'] = latest_status.complaints
	Objinfo['username'] = u.username
	Objinfo['email'] = u.email
	json_info.append(Objinfo)

pprint(json_info) 	
