from django.conf.urls import url
from . import views

app_name = 'forum'


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^create_forum/$', views.create_forum, name='create_forum'),
	url(r'^(?P<forum_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<forum_id>[0-9]+)/create_comment/$', views.create_comment, name='create_comment'),
]
