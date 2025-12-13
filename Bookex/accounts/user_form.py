from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    #firstname = forms.CharField(max_length=30, required=True)
    #lastname = forms.CharField(max_length=30, required=True)
    phonenumber = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'placeholder': '09196432585'}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter your address'}))
    #password = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname', 'phonenumber', 'address', 'password1', 'password1']
