# Modelo de django
from django.db import models

# Modelos de perfil y nutriologos
from Users.models import Profile, Nutriologist

# Create your models here.

class Receta(models.Model):
    """Receta Model"""

    nutriologo      = models.ForeignKey (Nutriologist, on_delete=models.CASCADE)

    cliente         = models.ForeignKey (Profile, on_delete=models.CASCADE)

    fecha_de_cita   = models.DateField (blank=False, null=False)

    hora_de_cita    = models.CharField (max_length=15,blank=True,null=False)

    motivo_de_cita  = models.CharField (max_length=40,blank=True, null=True)

    dctos_asignados = models.TextField (blank=True, null=True)

    # Verificar si el nutriologo acepto la cita o no
    estado          = models.BooleanField(default=False) 

    # Verificar si la cita sigue pendiente o si ya termino
    activa          = models.BooleanField(default=True)

    def __str__ (self):
        return str(self.motivo_de_cita)