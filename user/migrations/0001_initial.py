# Generated by Django 4.2.7 on 2023-12-13 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(default='profile_pics/default.jpeg', upload_to='profile_pics')),
                ('dob', models.DateField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('martail_status', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('linkedin', models.CharField(max_length=100, null=True)),
                ('occupation', models.CharField(max_length=100, null=True)),
                ('jobs', models.CharField(max_length=100, null=True)),
                ('nid', models.IntegerField(max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
