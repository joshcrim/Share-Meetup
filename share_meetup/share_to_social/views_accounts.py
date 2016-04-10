from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm

@csrf_exempt
def create_account(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        userform = UserForm(request.POST)
        # check whether it's valid:

        if userform.is_valid():
            # process the data in form.cleaned_data as required
            userform = User.objects.create_user(**userform.cleaned_data)
            userform.save()
            # redirect to a new URL:
            return redirect('/index/')

        # if a GET (or any other method) we'll create a blank form
    else:
        userform = UserForm()
        return render(request, 'create_account.html', {'userform': userform})

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
    else:
        return render(request, 'index.html')

@csrf_exempt
def logout_view(request):
    logout(request)
    return render(request, 'index.html')

@csrf_exempt
def connect_social(request):
    return render(request, 'connect_social.html')