"""Users Models"""

from django.db import models
from django.contrib.auth.models import User

# Cloudinary imports
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    """ Profile model """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # picture = models.ImageField(
    #     upload_to= 'users/pictures',
    #     blank=True, 
    #     null=True
    # )

    picture = CloudinaryField('image', blank = True, null = True)

    is_nutriologist = models.BooleanField(default=False)

    is_client = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)


class Nutriologist (models.Model):
    """Nutriologist model"""
    usuario = models.OneToOneField (Profile, to_field='user', on_delete=models.CASCADE)

    attention_days  = models.CharField (max_length=50, blank=True, null=True)

    attention_hours = models.CharField (max_length=40, blank=True, null=True)

    age             = models.IntegerField (blank=True, null=True)

    work_approach   = models.CharField (max_length=60, blank=False) #Enfoque del nutriologo como ej. especialista en obecidad etc etc etc.

    cedula_prof_det = models.CharField (max_length=60, blank=True, null=True)

    cedula_prof_img = CloudinaryField('image', blank = True, null = True)

    biography       = models.TextField (blank=True, null=True)

    active          = models.BooleanField (default=True)

    def __str__ (self):
        return str(self.usuario)

    
