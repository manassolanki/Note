from __future__ import unicode_literals

from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

# Create your models here.

class Note(models.Model):
	created_on = models.DateTimeField(auto_now_add=True, null=True)
	modified_on = models.DateTimeField(auto_now_add=True, null=True)
	title = models.CharField(max_length=200)
	text = models.TextField()
    user_id = EmbeddedModelField('User')
	# tags = ListField()


class User(models.Model):
	user_email_id = models.EmailField()
	title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
