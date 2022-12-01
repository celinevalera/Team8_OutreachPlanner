from django import forms
from django import forms
from django.forms import ModelForm
from .models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        labels = {
            'body': '',
        }
        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Enter your message here'}),
        }