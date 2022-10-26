from django import forms
from django import forms
from django.forms import EmailField, EmailInput, ModelForm
from .models import Venue
from .models import Event

#Venue Form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        labels = {
            'event_name': '',
            'event_date': '',
            'venue': '',
            'organizer': '',
            'description': '',
            'volunteers': '',
        }
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'venue': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Venue'}),
            'organizer': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Organizer'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'volunteers': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Volunteers'}),
        }
    
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
        labels = {
            'venue_name': '',
            'address': '',
            'web_link': '',
            'phone': '',
            'email': '',
        }
        widgets = {
            'venue_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'web_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web Link'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Contact Email'}),

        }