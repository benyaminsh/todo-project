from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField()