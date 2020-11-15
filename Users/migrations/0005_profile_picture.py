# Generated by Django 3.1.2 on 2020-11-15 20:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_remove_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=cloudinary.models.CloudinaryField(default=False, max_length=255, verbose_name='image'),
        ),
    ]
