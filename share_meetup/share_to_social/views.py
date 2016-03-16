from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm


def index(request):
	return render_to_response('share_to_social/index.html')
  #  template = loader.get_template('share_to_social/index.html')
   # return HttpResponse(template.render())

# Create your views here.

def user_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'UserForm.html', {'form': form})