from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=25)
    event_venue = models.CharField(max_length=25)
    event_description = models.CharField(max_length=100)
    event_starttime = models.DateTimeField(blank=False, null=False)
    event_endtime = models.DateTimeField(blank=False, null=False)

    def get_absolute_url(self):
        return reverse('evnt_det:index')
