from django.conf.urls import url
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import CampusObject

def index(request):
	all_campus_objects = CampusObject.objects.all()
	return render(request, 'campus/index.html', {'all_campus_objects': all_campus_objects})

def restaurants(request):
	return render(request, 'campus/restaurants.html')

def live_music(request):
	return render(request, 'campus/live_music.html')

def recreational_dispos(request):
	return render(request, 'campus/recreational_dispos.html')