from django.conf.urls import url

from . import views
from . import views_accounts

urlpatterns = [
	url(r'^index/$', views.index, name='index'),

	url(r'^home/share/(?P<event_id>[0-9]+)/$', views.share, name='share'),
	url(r'^home/$', views.home, name='home'),

	url(r'^accounts/logout/$', views_accounts.logout_view, name='logout'),
	url(r'^accounts/create_account/$', views_accounts.create_account, name='create_account'),
	url(r'^accounts/create_account/connect_social/$', views_accounts.connect_social, name='connect_social'),
	url(r'^accounts/login/$', views_accounts.user_login, name='login'),

	url(r'^test/$', views.test, name='test'),
]
