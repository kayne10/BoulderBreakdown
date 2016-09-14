from django.conf.urls import url
from . import views

app_name = 'hikes'


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^info/$', views.info, name='info'),
	url(r'^hikes/$', views.index, name='index'),
	url(r'^(?P<hike_id>[0-9]+)/$', views.detail, name='detail'),
]