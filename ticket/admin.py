from django.contrib import admin
from .models import Ticket

# Define this class for list_display and details
class TicketDetailsAdmin(admin.ModelAdmin):
    """
    This class is for display the field in the Django admin interface and from details
    """
    list_display = ('user', 'title', 'updated',)
    readonly_fields = ('created', 'updated',)

# Registered models are here.
admin.site.register(Ticket, TicketDetailsAdmin)