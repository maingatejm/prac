from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	photo = models.ImageField()
	content = models.TextField()
	def __str__(self):
		return self.title

class Comment(models.Model):
	author = models.CharField(max_length=50)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
