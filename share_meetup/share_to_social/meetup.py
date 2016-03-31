from django.conf import settings

from .models import Meetup_Event

import requests
import json
import datetime

def get_meetup_events(user):
	meetup_api_key = settings.MEETUP_API_KEY
	meetup_url = settings.MEETUP_API_URL

	events = requests.get(meetup_url + meetup_api_key)
	events = json.loads(events.text)

	for items in events:
		#Check for meetup ID exists in database to prevent duplicates
		if Meetup_Event.objects.filter(event_id=items['id']).exists():
			pass
		else:
			#Convert UTC epoch time to local event time and date
			utc_offset = items['utc_offset']
			event_time_epoch = items['time']
			event_time = datetime.datetime.fromtimestamp((event_time_epoch + utc_offset) / 1e3).strftime('%b %d - %I:%M %p')

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
