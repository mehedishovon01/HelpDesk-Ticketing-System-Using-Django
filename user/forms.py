from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ProfileDetails

"""
User registration form. Where Phone Number Can Added
"""
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'phone', 'email', 'password1', 'password2']

"""
User Update form. Where user can update their profile details
"""
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField()
    phone = forms.CharField()
    dob = forms.DateField()
    gender = forms.CharField()
    martail_status = forms.CharField()
    address = forms.CharField()
    linkedin = forms.CharField()
    occupation = forms.CharField()
    jobs = forms.CharField()
    nid = forms.IntegerField()

    class Meta:
        model = ProfileDetails
        fields = ['phone', 'image', 'dob', 'gender', 'martail_status', 'address', 'linkedin', 'occupation', 'jobs', 'nid']
