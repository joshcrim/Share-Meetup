def getMeetupEvents():

	request_events = requests.get('https://api.meetup.com/self/events?fields=short_link&key=' + meetup_api_key)

	events = json.loads(request_events.text)

	for items in events:
		event_id = items['id']

		if event_id == Meetup_Event.object.filter(event_id)
			group_name = items['group']['name']
			event_name = items['name']
			web_link = items['short_link']
			event_time_epoch = items['time']
			event_time_UTC = datetime.datetime.fromtimestamp(event_time_epoch / 1000).strftime('%m-%d-%Y %H:%M')

			#event = group_name +" - " + event_name + ", " + event_time_UTC + " " + web_link

			#print(event)
			meetup_data = Meetup_Event(event_id=event_id, group_name=group_name, event_name=event_name, web_link=web_link, event_time=event_time)

			meetup_data.save()

		<form class='col 12' method="post" action="{% url 'django.contrib.auth.views.login' %}">

		login, {'template_name': 'share_to_social/login.html'},

		post_content = meetup_data.group_name + " - " + meetup_data.event_name + ", " + meetup_data.event_time + " " + meetup_data.web_link