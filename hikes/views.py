from django.conf.urls import url
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Hike

def index(request):
	all_hikes = Hike.objects.all()
	return render(request, 'hikes/index.html', {'all_hikes': all_hikes})
	
def info(request):
	return render(request, 'hikes/info.html')

# Refer to youtube tutorial about detail template
def detail(request, hike_id):
    try:
    	hike = Hike.objects.get(pk=hike_id)
    	ratings = Hike.objects.filter(id=hike_id).order_by('ratings_average')
    except Hike.DoesNotExist:
    	raise Http404("Hike does not exist")
    return render(request, 'hikes/detail.html', {'hike': hike, 'ratings': ratings})

def home(request):
	all_hikes = Hike.objects.all()
	return render(request, 'hikes/home.html', {'all_hikes': all_hikes})

def ratings(request):
	return render(request, 'hikes/ratings.html')

