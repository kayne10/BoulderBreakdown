from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models

# Create your models here.
class Forum(models.Model):
	# user is author
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	article_title = models.CharField(max_length=250)
	article_subject = models.CharField(max_length=250)
	article_body = models.TextField(max_length=2000)
	# timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.article_title + '-' + self.user.username

class Comment(models.Model):
	# user is commentor
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
	forum_comment = models.TextField(max_length=1000)
	# timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.forum_comment + '-' + self.user.username

