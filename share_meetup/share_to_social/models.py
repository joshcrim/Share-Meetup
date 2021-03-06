from django.db import models
from django.conf import settings
from django.contrib import admin


class Meetup_Event(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	event_id = models.IntegerField()
	group_name = models.CharField(max_length=200)
	event_name = models.CharField(max_length=200)
	web_link = models.CharField(max_length=200)
	event_time = models.CharField(max_length=200)
	photo_link = models.CharField(max_length=200)
# meetup_post = models.CharField(max_length=140)

	def __str__(self):
		return self.event_name


class Meetup_Event_Admin(admin.ModelAdmin):
	list_display = ('group_name', 'event_name', 'event_time')
