from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home', views.home, name='home'),
	url(r'^create_account', views.create_account, name='create_account'),	
] 