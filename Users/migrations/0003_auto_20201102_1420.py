# Generated by Django 3.1.2 on 2020-11-02 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20201102_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutriologist',
            old_name='state',
            new_name='active',
        ),
        migrations.AlterField(
            model_name='nutriologist',
            name='work_approach',
            field=models.CharField(max_length=60),
        ),
    ]
