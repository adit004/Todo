from django.db import models

# Create your models here.

class Todo(models.Model):
    event_name = models.CharField(max_length=20)
    discription = models.CharField(max_length=40)
    date = models.DateField()