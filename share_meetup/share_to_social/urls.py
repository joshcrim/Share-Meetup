from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
	url(r'^share/(?P<event_id>[0-9]+)/', views.share, name='share'),
	url(r'^create_account/', views.create_account, name='create_account'),	
	url(r'^login/', login, {'template_name': 'share_to_social/login.html'}, name='login'),
	url(r'^$', views.home, name='home')
] 