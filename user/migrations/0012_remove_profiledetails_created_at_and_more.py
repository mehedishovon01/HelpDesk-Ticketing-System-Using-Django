# Generated by Django 4.2.7 on 2023-12-16 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_rename_created_profiledetails_created_at'),
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