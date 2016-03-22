from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
	url(r'^home', views.home, name='home'),
	url(r'^create_account', views.create_account, name='create_account'),
	url(r'^share', views.share, name='share'),	
	url(r'^login', login, {'template_name': 'share_to_social/login.html'}, name='login')
] 