# Generated by Django 4.2.7 on 2023-12-16 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_profiledetails_created_at_profiledetails_modified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiledetails',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='profiledetails',
            name='modified',
        ),
    ]
