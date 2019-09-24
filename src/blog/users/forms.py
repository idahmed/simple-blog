from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User

class UserRegisterForm(UserCreationForm):
    """
    form for registering a user.
    """
    class Meta:
        model = User
        fields = [
            'email', 'first_name', 'last_name', 'password1', 'password2'
        ]