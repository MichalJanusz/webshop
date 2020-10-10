from django import forms
from django.contrib.auth.forms import AuthenticationForm


# Create your forms here

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'login'}), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}), label=False)
