from django.conf import settings
from .models import User
from .models import Meetup_Event
import requests
import json
import datetime

def get_meetup_events(user):
	refresh_url = settings.SOCIAL_MEETUP_REFRESH_URL
	access_url = settings.SOCIAL_MEETUP_API_URL
	user = User.objects.get(username=user)
	social_auth = user.social_auth.get(provider='meetup')

	refresh_request = requests.post(refresh_url + social_auth.extra_data['refresh_token'])
	refresh_request = json.loads(refresh_request.text)

	social_auth.extra_data['access_token'] = refresh_request['access_token']
	social_auth.extra_data['refresh_token'] = refresh_request['refresh_token']
	social_auth.save

	events = requests.get(access_url + social_auth.extra_data['access_token'])
	events = json.loads(events.text)

	for items in events:
		#Check for meetup ID exists in database to prevent duplicates
		if Meetup_Event.objects.filter(event_id=items['id']).exists():
			pass
		else:
			#Convert UTC epoch time to local event time and date
			event_time = (items['time'] + items['utc_offset'])
			event_time = datetime.datetime.fromtimestamp((event_time)/1e3).strftime('%b %d - %I:%M %p')

			#Store meetup data from GET request in database
			meetup_data = Meetup_Event(
				user=user,
				event_id=items['id'],
				group_name=items['group']['name'],
				event_name=items['name'],
				web_link=items['short_link'],
				event_time=event_time)

			meetup_data.save()

	return Meetup_Event.objects.all().order_by('-event_time')
