from flask import render_template,url_for
from flask import flash,redirect # for flash messages and redirecting on logging.
from app import app
from app import db# import the database
from app.forms import LoginForm
from flask_login import current_user,login_user # state of the user
from app.models import User,Status
from flask_login import logout_user,login_required
from flask import request
from werkzeug.urls import url_parse
from app.forms import RegistrationForm,Status_Update
from googleplaces import GooglePlaces, types, lang
from pprint import pprint
import json
import unicodedata
import re
import datetime
import requests


@app.route('/',methods=['GET','POST']) # decorators for routing 
@app.route('/index',methods=['GET','POST']) # index page 
def index():
	tweet = [] 
	tf = open("outp.json","r")
	for line in tf:
		try:
			tweet.append(json.loads(line))
		except:
			continue
	tweet_text = ""
	for t in tweet:
		tweet_text = tweet_text + "  " + t['text'] 
	tweet_text = re.sub(r"http\S+", "", tweet_text)
	tweet_text = unicodedata.normalize('NFKD',tweet_text).encode('ascii','ignore')
	
	form = Status_Update()

	# add the json parsing
	users = User.query.all()
	json_info = [] 

	for u in users:
		if(len(u.status.all()) !=0):
			latest_status = u.status.all()[-1] #latest status
			Objinfo = {}
			Objinfo['phone'] = u.phone
			Objinfo['lat'] = latest_status.latitude
			Objinfo['lng'] = latest_status.longitude
			Objinfo['danger'] = latest_status.danger
			Objinfo['who'] = latest_status.who
			Objinfo['help'] = latest_status.help
			Objinfo['complaints'] = latest_status.complaints
			Objinfo['username'] = u.username
			Objinfo['email'] = u.email
			Objinfo['disaster']=latest_status.disaster
			json_info.append(Objinfo)
	# add the json parsing

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			return redirect(url_for('index'))
		#login_user(user)

		user.phone = form.phone.data
		db.session.add(user)

		# find the coordinate from ip address#
		#proxies = {'http':'http://debarghya4469:7hX3esbL@202.141.80.20:3128','https':'https://debarghya4469:7hX3esbL@202.141.80.20:3128',} 
		SECRET_KEY_IPSTACK = "xxxxxxxxxxxxxxxxxxxxxxxxx"

		req = requests.get('http://ipinfo.io/ip')
		#req = requests.get('http://ipinfo.io/ip',proxies=proxies)
		ipaddr = unicodedata.normalize('NFKD', req.text).encode('ascii','ignore')

		url = 'http://api.ipstack.com/'+ipaddr+'?access_key='+SECRET_KEY_IPSTACK+'&format=1'

		#ip_json = requests.get(url,proxies=proxies)
		ip_json = requests.get(url)
		jsonData=ip_json.json()

		latitude = str(jsonData['latitude'])
		longitude = str(jsonData['longitude'])

		# find the coordinate from ip address#

		st_up = Status(disaster=form.disaster.data,latitude=latitude,longitude=longitude,complaints=form.complaints.data,who=form.who.data,help=form.help.data,danger=form.danger.data,timestamp=datetime.datetime.utcnow(),us=user)

		#update the database
		db.session.add(st_up)
		db.session.commit()
		

		flash('your status is updated!')
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)


	curr_lat = "26.1"
	curr_lon = "91.6906578"

	utility_centers = [] 

	if current_user.is_authenticated: # if the current user is authenticated !!
		active_user = User.query.filter_by(id=int(current_user.get_id())).first() # get the current user
		if(len(active_user.status.all())!=0):
			curr_lat = active_user.status.all()[-1].latitude
			curr_lon = active_user.status.all()[-1].longitude

		google_places = GooglePlaces("AIzaSyCNLxPxFmG3kfrALBUkRFb_R5UdemVnqqQ")
		coords = curr_lat + " " + curr_lon
		query_result = google_places.nearby_search(location=coords,radius=20000, types=[types.TYPE_HOSPITAL,types.TYPE_PHARMACY,types.TYPE_DOCTOR,types.TYPE_ATM,types.TYPE_FOOD,types.TYPE_HEALTH,types.TYPE_POLICE,types.TYPE_CITY_HALL])

		place = query_result.places
		
		try:
			for p in place:
				placeObj = {}
				placeObj['name']=p.name
				placeObj['lat']=str(p.geo_location['lat'])
				placeObj['lng']=str(p.geo_location['lng'])
				utility_centers.append(placeObj);
				print(placeObj)				

		except Exception as e: # this part of hl done !!!
			print e


	return render_template('index.html',title='Home page',alltext=tweet_text,utility_centers=utility_centers,form=form,json_info=json_info,curr_lat=curr_lat,curr_lon=curr_lon)

	
@app.route('/register',methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data,email=form.email.data)
		user.set_password(form.password.data) # set the hashed password
		db.session.add(user)
		db.session.commit()
		flash('congratulation you just signed up!')
		return redirect(url_for('login'))
	return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['GET','POST']) # index page 
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title='Sign In', form=form)
		
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))
		
@app.route('/donations')
def donations():
    return render_template('donations.html',title="Donate")

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/safety')
def safety():
    return render_template('safety.html',title='safety precautions')	

	
