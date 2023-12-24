from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Ticket


class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']


class TicketUpdateForm(forms.ModelForm):
    """
    Ticket Update form. Where the ticket can update with the full information
    """
    class Meta:
        model = Ticket
        fields = ['title', 'user', 'description', 'status', 'waiting_for', 'assigned_to']