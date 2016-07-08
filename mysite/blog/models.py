from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
	STATUS_CHOICE = (("draft","DRAFT"),("published","PUBLISHED"),)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250,unique_for_date='published')
	author = models.ForeignKey(User,related_name = "blog_posts")
	body = models.TextField()
	published = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10,choices=STATUS_CHOICE,default="draft")
	
	class Meta:
		ordering = ("-published",)

	def __unicode__(self):
		return self.title
    