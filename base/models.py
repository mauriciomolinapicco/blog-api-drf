from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    posted = models.DateTimeField(auto_now_add=True) 