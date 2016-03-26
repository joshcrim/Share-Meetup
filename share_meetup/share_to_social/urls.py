from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
	url(r'^home/share/(?P<event_id>[0-9]+)', views.share, name='share'),
	url(r'^home/(?P<username>[-\w]+)', views.home, name='home'),
	url(r'^index/create_account', views.create_account, name='create_account'),
	url(r'^index/auth_view', views.auth_view, name='auth_view'),
	url(r'^index/login', views.login, name='login'),
	url(r'^index/', views.index, name='index')
] 