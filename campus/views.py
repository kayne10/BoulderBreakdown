from django.conf.urls import url
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import CampusObject

def index(request):
	all_campus_objects = CampusObject.objects.all()
	return render(request, 'campus/index.html', {'all_campus_objects': all_campus_objects})
