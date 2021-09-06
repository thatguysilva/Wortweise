from django.db import models
from django import forms
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=255)
	time = models.CharField(max_length=255)
	slug = models.SlugField(max_length=200, unique=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)
	body = models.TextField()
	
	class Meta:
        	ordering = ['-created_on']
	
	def __str__(self):
		return self.title + ' | ' + str(self.author)

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    message = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.message, self.name)
