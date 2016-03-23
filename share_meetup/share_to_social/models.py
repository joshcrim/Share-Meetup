from django.db import models
from .forms import UserForm
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Meetup_Event(models.Model):
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	event_id = models.IntegerField()
	group_name = models.CharField(max_length=200)
	event_name = models.CharField(max_length=200)
	web_link = models.CharField(max_length=200)
	event_time = models.CharField(max_length=200)

	def __str__(self):
		return self.event_name

class Twitter_Profile(models.Model):
	def __unicode__(self):
		return self.user.user.username

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	twitter_id = models.DecimalField(max_digits=20, decimal_places=0, null=True)
	oauth_token = models.CharField(max_length=200)
	oauth_secret = models.CharField(max_length=200)
	twitter_username = models.CharField(max_length=200,null=True)


