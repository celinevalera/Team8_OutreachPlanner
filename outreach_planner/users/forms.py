from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from planner.models import Volunteer

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}))

    class Meta: 
        model = User
        fields = ('username','first_name','last_name','email', 'password1','password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Retype Password'

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
<<<<<<< HEAD
            'password'
        )
        
=======
            'password',
            'username'
        )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Last Name'}),
        }
>>>>>>> 23ac3a72e967c28a2c8bbb4ed531327cb8b94f56
