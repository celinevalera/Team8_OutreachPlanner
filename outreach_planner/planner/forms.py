from django import forms
from django import forms
from django.forms import EmailField, EmailInput, ModelForm
from .models import Venue, Event

#Venue Form
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
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'event_name'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'event_date'}),
            'venue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'venue'}),
            'organizer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'organizer'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'volunteers': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'volunteers'}),

        }