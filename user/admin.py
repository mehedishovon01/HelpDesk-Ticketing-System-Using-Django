from django.contrib import admin
from .models import ProfileDetails

# Define this class for list_display and details
class ProfileDetailsAdmin(admin.ModelAdmin):
    """
    This class is for display the field in the Django admin interface and from details
    """
    list_display = ('id', 'user', 'created_at', 'modified',)
    readonly_fields = ('created_at', 'modified',)

# Registered models are here.
admin.site.register(ProfileDetails, ProfileDetailsAdmin)
