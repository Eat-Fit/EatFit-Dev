# Generated by Django 3.1.2 on 2020-11-02 20:27

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/pictures')),
                ('is_nutriologist', models.BooleanField(default=False)),
                ('is_client', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Nutriologist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attention_days', models.CharField(blank=True, max_length=50, null=True)),
                ('attention_hours', models.CharField(blank=True, max_length=40, null=True)),
                ('age', models.IntegerField(blank=True, max_length=5, null=True)),
                ('work_approach', models.CharField(max_length=50)),
                ('cedula_prof', models.ImageField(blank=True, null=True, upload_to='nutriologist/cedula')),
                ('biography', models.TextField(blank=True, null=True)),
                ('state', models.BooleanField(default=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Users.profile', to_field='user')),
            ],
        ),
    ]
