from django import forms
from django import forms
from django.forms import EmailField, EmailInput, ModelForm
from .models import Venue,Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        labels = {
            'event_name': 'Event Title',
            'event_date': 'Event Date',
            'venue': 'Venue',
            'organizer': 'Organizer',
            'description': 'Event Description',
            'volunteers': 'Attendees',
            'event_image': 'Venue Image',
        }
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
            'venue': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Venue'}),
            'organizer': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Organizer'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'volunteers': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Volunteers'}),
        }
    
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
        labels = {
            'venue_name': 'Venue Name',
            'address': 'Venue Address',
            'web_link': 'Venue Website',
            'phone': 'Contact Number',
            'email': 'Contact Email',
            'venue_image': 'Venue Image',
        }
        widgets = {
            'venue_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'web_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web Link'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Contact Email'}),
            
        }
