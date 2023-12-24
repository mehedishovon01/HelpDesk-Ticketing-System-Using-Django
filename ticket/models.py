from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    """
    Defining this class is meant to store information related to a tickets.
    Name_of_the_Class: model class
    """
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', blank=True, null=True)
    STATUS_CHOICES = (
        ('TODO', 'TODO'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('WAITING', 'WAITING'),
        ('DONE', 'DONE'),
    )
    status = models.CharField('Status',
                              choices=STATUS_CHOICES,
                              max_length=255,
                              blank=True,
                              null=True)
    waiting_for = models.ForeignKey(User,
                                    related_name='waiting_for',
                                    blank=True,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='Waiting For')
    # # set in view when status changed to "DONE"
    closed_date = models.DateTimeField(blank=True, null=True)
    assigned_to = models.ForeignKey(User,
                                    related_name='assigned_to',
                                    blank=True,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='Assigned to')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        The __str__ method in a Django model is a special method that defines the human-readable representation of an object. 
        It is called whenever the object needs to be represented as a string, such as when you use str(obj) 
        or when the object is displayed in the Django admin interface.
        return: string
        """
        return str(self.title)
