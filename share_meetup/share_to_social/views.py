from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .meetup import get_meetup_events
from .models import Meetup_Event

# Create your views here.
@csrf_exempt
def index(request):
    if request.user.is_active:
        return redirect('/home/')
    else:
        return render(request, 'index.html')

@csrf_exempt
@login_required(login_url='/accounts/login/')
def home(request):
#   GET Meetup Event Info from all meetups the user
#   has RSVP'd to and load JSON data into variable
    user = request.user.username

#   Get user's meetup events from Meetup.com, parse from json to text, store in database, load to variable.
    meetup_data = get_meetup_events(user)

#   Load HTML template with Meetup data
    context = {'meetup_data': meetup_data}
    return render(request, 'home.html', context)


def share(request, event_id):
    meetup_content = Meetup_Event.objects.all().filter(event_id=event_id)

    context = {'meetup_content': meetup_content}
    return render(request, 'share.html', context)

def profile(request, username):
    print("")
