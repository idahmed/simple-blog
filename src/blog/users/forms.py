from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User, Profile

class UserRegisterForm(UserCreationForm):
    """
    form for registering a user.
    """
    class Meta:
        model = User
        fields = [
            'email', 'first_name', 'last_name', 'password1', 'password2'
        ]


class ProfileForm(forms.ModelForm):
    """
    form to create or update a profile.
    """

    class Meta:
        model = Profile
        fields = [
            'profile_pic', 'gender', 'bio', 'address', 'phone'
        ]