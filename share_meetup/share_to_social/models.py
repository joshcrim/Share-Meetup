from django.db import models
from .forms import UserForm
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user_profile = models.ForeignKey(User)
	oauth_token = models.CharField(max_length=200)
	oauth_secret = models.CharField(max_length=200)