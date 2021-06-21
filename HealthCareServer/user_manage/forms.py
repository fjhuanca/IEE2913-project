from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']