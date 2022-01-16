from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    post = models.CharField(max_length=100000)