# Generated by Django 4.2.7 on 2023-12-16 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_profiledetails_created_at_profiledetails_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledetails',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
