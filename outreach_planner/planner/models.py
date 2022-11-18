
from email.policy import default
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.dispatch import receiver
import uuid

# tables
class Venue(models.Model):
    venue_name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300, blank=True)
    web_link = models.URLField('Event Link', blank=True)
    phone = models.PositiveIntegerField('Contact Number')
    email = models.EmailField('Contact Email', blank=True)
    venue_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.venue_name

class Volunteer(models.Model):
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    participants = models.BooleanField(default= True, null=True)
    

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    event_name = models.CharField('Event Name', max_length=120)
    event_date= models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    organizer = models.ManyToManyField(User, blank=True)
    description = models.TextField(blank=True)
    volunteers = models.ManyToManyField(User, blank=True, related_name='events')
    event_image = models.ImageField(null=True, blank=True, upload_to="images/")
    



    def __str__(self):
        return self.event_name

class Inbox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    subject = models.CharField(max_length=500, blank=True, null = True)
    body = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.first_name+' '+self.user.last_name
