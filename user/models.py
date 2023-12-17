from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as timezone

# Return User's Full Name
def user_str(self):
    """
    This function is used for return the User's First & Last Name by default
    return: String
    """
    return f"{self.first_name} {self.last_name}"

"""
In Python 3, there is no __unicode__ method. Instead, use the __str__ method for string representation. 
Python 3 uses Unicode by default for string handling.
"""
User.__str__ = user_str


# Users models are here.
class ProfileDetails(models.Model):
    """
    Defining this class is meant to store information related to a user's profile. 
    Additionally, here defined an inner class named GenderChoices & MaritailChoices within the ProfileDetails model, 
    and it inherits from models.TextChoices. This inner class is used to define choices for the gender and martail_status field.
    Name_of_the_Class: inner class
    """
    # Gender Choices are defined here
    class GenderChoices(models.TextChoices):
        """
        This class is an enumeration class that defines choices for the gender field in the ProfileDetails model.
        Each choice is represented as a pair of a human-readable name (e.g., 'Male') and its corresponding value (e.g., 'Male'). 
        values: string literals
        Name_of_the_Class: enumeration class
        """
        Male = 'Male'
        Female = 'Female'
        Other = 'Other'
    
    # Martail Status are defined here
    class MaritailChoices(models.TextChoices):
        """
        This class is an enumeration class that defines choices for the martail_status field in the ProfileDetails model.
        Each choice is represented as a pair of a human-readable name (e.g., 'Maried') and its corresponding value (e.g., 'Maried').
        values: string literals
        Name_of_the_Class: enumeration class
        """
        Maried = 'Maried'
        Unmaried = 'Unmaried'
        Other = 'Other'

    """
    Profile Details Fields where all the details data will be stored with user table's foreign key, choices, images,
    auto_now_add, auto_now, datefield and textfields
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, null=True)
    image = models.ImageField(default='profile_pics/default.jpeg', upload_to='profile_pics', null=True)
    dob = models.DateField(max_length=100, null=True)
    gender = models.CharField(choices=GenderChoices.choices, default=GenderChoices.Male, max_length=255, blank=True, null=True)
    martail_status = models.CharField(choices=MaritailChoices.choices, default=MaritailChoices.Maried, max_length=255, blank=True, null=True)
    address = models.TextField(max_length=600, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    occupation = models.CharField(max_length=100, null=True)
    jobs = models.CharField(max_length=100, null=True)
    nid = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        The __str__ method in a Django model is a special method that defines the human-readable representation of an object. 
        It is called whenever the object needs to be represented as a string, such as when you use str(obj) 
        or when the object is displayed in the Django admin interface.
        return: string
        """
        return f"{self.user.username}'s Profile Details"
