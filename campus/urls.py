from django.conf.urls import url
from . import views

app_name = 'campus'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^live_music/$', views.live_music, name='live_music'),
	url(r'^restaurants_bars/$', views.restaurants, name='restaurants'),
	url(r'^recreational_dispos/$', views.recreational_dispos, name='recreational_dispos'),
]