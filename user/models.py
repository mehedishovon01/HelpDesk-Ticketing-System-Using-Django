from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, null=True)
    image = models.ImageField(default='profile_pics/default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile Picture"