# Generated by Django 4.2.7 on 2023-12-16 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_profiledetails_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledetails',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
