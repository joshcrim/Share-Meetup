from django.contrib import admin
from .models import Meetup_Event, Meetup_Event_Admin
# Register your models here.
admin.site.register(Meetup_Event, Meetup_Event_Admin)