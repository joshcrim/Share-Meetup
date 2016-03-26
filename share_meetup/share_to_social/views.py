from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import loader
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm
from .models import Meetup_Event

from time import strftime, gmtime
from twython import Twython
import requests
import json
import datetime


# Create your views here.
@csrf_exempt
def home(request, username):
    #GET Meetup Event Info from all meetups the user has RSVP'd to and load JSON data into variable

        user = User.objects.get(username=username)
        user = user.username

        meetup_api_key = settings.MEETUP_API_KEY

        request_events = requests.get('https://api.meetup.com/self/events?fields=short_link,group_photo&key=' + meetup_api_key)
        events = json.loads(request_events.text)

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
                meetup_data = Meetup_Event(user=user, event_id=items['id'], group_name=items['group']['name'], event_name=items['name'], web_link=items['short_link'], event_time=event_time)

                meetup_data.save()

        meetup_data = Meetup_Event.objects.all().order_by('-event_time')

        #Load HTML template with Meetup data
        template = loader.get_template('home.html')
        return HttpResponse(template.render({'meetup_data': meetup_data}))


def share(request, event_id):
    meetup_data = Meetup_Event.objects.get(event_id=event_id)
    post_content = meetup_data.group_name +" - " + meetup_data.event_name + ", " + meetup_data.event_time + " " + meetup_data.web_link
    
    twitter = Twython(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET,
                  settings.TWITTER_OAUTH_TOKEN, settings.TWITTER_OAUTH_TOKEN_SECRET)

    twitter.update_status(status=post_content)

    meetup_content = Meetup_Event.objects.all().filter(event_id=event_id)
    template = loader.get_template('share.html')

    return HttpResponse(template.render({'meetup_content': meetup_content}))


def create_account(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = create_account(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/login')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

        return render(request, 'create_account.html', {'form': form})

def twitter_connect(request):
    twitter_app_key = settings.TWITTER_APP_KEY
    twitter_app_secret = settings.TWITTER_APP_SECRET

    request_token_url = 'http://twitter.com/oauth/request_token'
    access_token_url = 'http://twitter.com/oauth/access_token'
    authorize_url = 'http://twitter.com/oauth/authorize'

    consumer = oauth.Consumer(twitter_consumer_key,twitter_consumer_secret)
@csrf_exempt
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def profile(request, username):
    print("")
@csrf_exempt
def login(request):
    if request.method == 'POST':

        form = request.POST['username', 'password']

        return HttpResponseRedirect('login.html')

    else:
        template = loader.get_template('login.html')
        return HttpResponse(template.render())
@csrf_exempt
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/home/%s/' % username)

    else:
        return render(request, 'index.html')