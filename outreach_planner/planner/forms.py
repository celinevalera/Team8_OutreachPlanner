from django import forms
from django import forms
from django.forms import EmailField, EmailInput, ModelForm
from .models import Inbox, Venue

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

class MessageForm(ModelForm):
    class Meta:
        model = Inbox
        fields = "recipient","subject","body"
        labels = {
            'recipient': '',
            'subject': '',
            'body': '',
            
        }
        widgets = {
            'recipient': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'recipient'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'subject'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'body'}),
        }