from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=500)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

