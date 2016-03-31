from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone

from .forms import UserForm

# Create your models here.

class Meetup_Event(models.Model):
	def __unicode__(self):
		return self.event_name

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	event_id = models.IntegerField()
	group_name = models.CharField(max_length=200)
	event_name = models.CharField(max_length=200)
	web_link = models.CharField(max_length=200)
	event_time = models.CharField(max_length=200)
	photo_link = models.CharField(max_length=200)



class Meetup_Event_Admin(admin.ModelAdmin):
	list_display = ('group_name', 'event_name', 'event_time')