from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ProfileDetails


class UserRegisterForm(UserCreationForm):
    """
    User registration form. Where Phone Number Can Added
    """
    email = forms.EmailField()
    phone = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'phone', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """
    User Update form. Where user can update their Name & email
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    User Update form. Where user can update their profile details
    """
    class Meta:
        model = ProfileDetails
        fields = ['phone', 'image', 'dob', 'gender', 'martail_status', 'address', 'linkedin', 'occupation', 'jobs', 'nid']
