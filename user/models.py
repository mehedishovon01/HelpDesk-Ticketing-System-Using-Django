from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, null=True)
    image = models.ImageField(default='profile_pics/default.jpeg', upload_to='profile_pics', null=True)
    dob = models.DateField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    martail_status = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    occupation = models.CharField(max_length=100, null=True)
    jobs = models.CharField(max_length=100, null=True)
    nid = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile Details"