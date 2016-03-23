from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.models import User
from .forms import UserForm
from .models import Meetup_Event
import requests
import json
import datetime


# Create your views here.
def home(request):
    meetup_api_key= settings.MEETUP_API_KEY

    user= User.objects.get(username="josh")

    request_events  = requests.get('https://api.meetup.com/self/events?fields=short_link,group_photo&key=' + meetup_api_key)

    events = json.loads(request_events.text)

    template = loader.get_template('index.html')
    return HttpResponse(template.render({'events': events}))


def share(request):
    template= loader.get_template('share.html')
    return HttpResponse(template.render())


def create_account(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form= UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/login')

        # if a GET (or any other method) we'll create a blank form
    else:
        form= UserForm()

        return render(request, 'UserForm.html', {'form': form})

def twitter_connect(request):
    twitter_app_key= settings.TWITTER_APP_KEY
    twitter_app_secret= settings.TWITTER_APP_SECRET

    request_token_url= 'http://twitter.com/oauth/request_token'
    access_token_url= 'http://twitter.com/oauth/access_token'
    authorize_url= 'http://twitter.com/oauth/authorize'

    consumer= oauth.Consumer(twitter_consumer_key,twitter_consumer_secret)

