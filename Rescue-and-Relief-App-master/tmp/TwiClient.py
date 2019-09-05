import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pprint
import re

access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_key ="xxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def get_tweets(username):
	auth = OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)

	api  = tweepy.API(auth)

	num_of_tweets = 5 
	tweets = api.user_timeline(screen_name=username)

	tmp = [] 
	tweets_for_csv = [ tweet.text for tweet in tweets]
	for j in tweets_for_csv:
		tmp.append(j)

	for i in range(10):
		u = tmp[i]
		u.encode('utf-8')
		u = re.sub(r"http\S+", "",u)
		print(u)
	#json_load = json.loads(tweets)
	#texts = json_load['text']
	#coded = texts.encode('utf-8')
	#s = str(coded)
	#print(s)

if __name__=='__main__':
	get_tweets('WeAreMessi')

