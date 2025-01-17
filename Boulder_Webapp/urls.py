from django.conf.urls import  include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
 	url(r'^', include('hikes.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^hikes/', include('hikes.urls')),
    url(r'^forum/', include('forum.urls')),
    url(r'^campus/', include('campus.urls')),
    
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
