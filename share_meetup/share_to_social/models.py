from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_Length=200)
	username = models.CharField(max_Length=200)

class Profile(models.Model):
	user = models.ForgeinKey(User)
	oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)