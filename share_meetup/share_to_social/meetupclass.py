from django.conf import settings
from .models import User
from .models import Meetup_Event
import requests
import json
import datetime

class Meetup(object):

	REFRESH_URL = settings.SOCIAL_MEETUP_REFRESH_URL
	ACCESS_URL = settings.SOCIAL_MEETUP_API_URL
	AUTH_PROVIDER = user.social_auth.get(provider='meetup')

	def __init__(self, user):
		self.user = User.objects.get(username=user)
		self.accessToken = self.AUTH_PROVIDER.extra_data['access_token']
		self.refreshToken = self.AUTH_PROVIDER.extra_data['refresh_token']

	def refresh_tokens(self):
		refresh_request = requests.post(self.refresh_url + self.refresh_token)

		self.refresh = json.loads(refresh_request.text)

		self.accessToken = self.refresh['access_token']
		self.refreshToken = self.refresh['refreshToken']

		self.AUTH_PROVIDER.save()

	def get_events(self):
		events = requests.get(self.ACCESS_URL + self.accessToken)
		self.events = json.loads(events.text)

	def save_events(self):
		for items in self.events:
			if Meetup_Event.objects.filter(event_id=items['id']).exists():
				pass
		else:
			event_time = (items['time'] + items['utc_offset'])
			event_time = datetime.datetime.fromtimestamp((event_time)/1e3).strftime('%b %d - %I:%M %p')
			meetup_data = Meetup_Event(
				user=self.user,
				event_id=items['id'],
				group_name=items['group']['name'],
				event_name=items['name'],
				web_link=items['short_link'],
				event_time=event_time)

			meetup_data.save()

	return Meetup_Event.objects.all().order_by('-event_time')
