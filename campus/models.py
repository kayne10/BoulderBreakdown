from django.db import models
from django.core.urlresolvers import reverse


class CampusObject(models.Model):
	title = models.CharField(max_length=100)
	description_url = models.CharField(max_length=200)
	# image = models.FileField()
	# color = RGBColorField()

	def __str__(self):
		return self.title

# class Item(models.Model):
	
