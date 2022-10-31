
from concurrent.futures import thread
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

# tables
class Venue(models.Model):
    venue_name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300, blank=True)
    web_link = models.URLField('Event Link', blank=True)
    phone = models.PositiveIntegerField('Contact Number')
    email = models.EmailField('Contact Email', blank=True)

    def __str__(self):
        return self.venue_name

class Volunteer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    event_name = models.CharField('Event Name', max_length=120)
    event_date= models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    organizer = models.ManyToManyField(User, blank=True)
    description = models.TextField(blank=True)
    volunteers = models.ManyToManyField(Volunteer, blank=True)

    def __str__(self):
        return self.event_name

class ThreadModel(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

class MessageModel(models.Model):
    thread = models.ForeignKey(ThreadModel, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    body = models.CharField(max_length = 1000)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)



