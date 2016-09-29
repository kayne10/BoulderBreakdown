from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from star_ratings.models import Rating

# Create your models here.
class Hike(models.Model):
	hike_title = models.CharField(max_length=250)
	hike_map = models.CharField(max_length=1000)
	hike_description = models.TextField(max_length=2000)
	hike_image = models.ImageField(null=True, blank=True,
		width_field="width_field",
		height_field="height_field")
	width_field = models.IntegerField(default=0)
	height_field = models.IntegerField(default=0)
	ratings = GenericRelation(Rating, related_query_name='hike')
	


	def __str__(self):
		return self.hike_title

# Hike.objects.filter(ratings_isnull=False).order_by('ratings_average')