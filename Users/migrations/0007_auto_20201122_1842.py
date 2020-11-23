# Generated by Django 3.1.2 on 2020-11-23 01:42

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20201115_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutriologist',
            name='cedula_prof',
        ),
        migrations.AddField(
            model_name='nutriologist',
            name='cedula_prof_det',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='nutriologist',
            name='cedula_prof_img',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]