import requests
import json
import datetime
from twython import Twython
from api_keys import *

# Get's all meetup events the user has RSVP'd for (this will eventually only get upcoming events)

def getMeetupEvents():

	r = requests.get('https://api.meetup.com/self/events?fields=short_link&key=' + meetup_api_key)

	rw = json.loads(r.text)

	for items in rw:
		group_name = items['group']['name']
		event_name = items['name']
		web_link = items['short_link']
		event_time_epoch = items['time']
		event_time_UTC = datetime.datetime.fromtimestamp(event_time_epoch / 1000).strftime('%m-%d-%Y %H:%M')

		event = group_name +" - " + event_name + ", " + event_time_UTC + " " + web_link

		print(event)



#Posts param value to Twitter

def postToTwitter(post_content):

	twitter = Twython(twitter_app_key, twitter_app_secret,
                  twitter_oauth_token, twitter_oauth_token_secret)

	twitter.update_status(status=post_content)

#In Progress-------------------------------------#
def postToFacebook(post_content):
	facebook_app_key
	facebook_app_secret
#------------------------------------------------#


postToTwitter(getMeetupEvents())


#getMeetupEvents()
