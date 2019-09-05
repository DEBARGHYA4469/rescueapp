import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pprint
import re
import time

access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret = "xxxxxxxxxxxxxxxxxxxxxx"
consumer_key ="xxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

class MyStreamListener(tweepy.StreamListener):
	def __init__(self,start_time,time_limit=60):
		self.start_time = time.time()
		self.limit = time_limit
		self.saveFile = open('outp.json','a')
		super(MyStreamListener,self).__init__()

	def on_data(self,data):
		if(time.time()-self.start_time) < self.limit:
			self.saveFile.write(data)
			self.saveFile.write('\n')
			return True
		else:
			self.saveFile.close()
			return False

if __name__=='__main__':
	auth = OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	api = tweepy.API(auth)

	start_time =time.time()
	stream_data = Stream(auth,MyStreamListener(start_time,20))
	stream_data.filter(track=['Earthquakes','Volcano','Cyclones','disaster','natural disaster','flood','tornado'])
