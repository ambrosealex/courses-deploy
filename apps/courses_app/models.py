from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=250)
    added_at = models.DateTimeField(auto_now_add=True)
