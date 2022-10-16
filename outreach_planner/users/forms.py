from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from planner.models import Volunteer



class RegisterUserForm(UserCreationForm):
    email= forms.EmailField()
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)

    class Meta: 
        model = Volunteer
        fields = ('first_name','last_name','email', 'password1','password2')