# Generated by Django 4.2.7 on 2023-12-16 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_profiledetails_created_at_profiledetails_modified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiledetails',
            name='modified',
        ),
    ]
