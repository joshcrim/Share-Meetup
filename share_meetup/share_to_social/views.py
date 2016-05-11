from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .forms import UserForm
from .meetup import get_meetup_events
from .models import Meetup_Event


@csrf_exempt
def index(request):
    if request.user.is_active:
        return redirect('/home/')
    else:
        userform = UserForm()
        return render(request, 'index.html', {'userform': userform})


@csrf_exempt
@login_required(login_url='/accounts/login/')
def home(request):
#   If user has connected a social account (!refine to only meetup account!)
#   load the home page with their meetup events. Else redirect to social connection page.
    if request.user.social_auth.exists():
        user = request.user.username
        meetup_data = get_meetup_events(user)
        context = {'meetup_data': meetup_data}
        return render(request, 'home.html', context)
    else:
        return render(request, 'connect_social.html')


@csrf_exempt
def test(request):
    userform = UserForm()
    return render(request, 'test.html', {'userform': userform})


#! !# Currently unused
def share(request, event_id):
    meetup_content = Meetup_Event.objects.all().filter(event_id=event_id)

    context = {'meetup_content': meetup_content}
    return render(request, 'share.html', context)
#! !#
