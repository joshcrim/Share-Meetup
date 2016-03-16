from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.user_form, name='user_form')
	url(r'^$', views.index, name='index'),
]