from django.db import models
from datetime import datetime

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=25)
    venue = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    start_time = models.DateTimeField(blank=False, null=False)
    end_time = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.name