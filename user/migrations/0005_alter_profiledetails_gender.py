# Generated by Django 4.2.7 on 2023-12-16 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profiledetails_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledetails',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=255, null=True, verbose_name='Gender'),
        ),
    ]
