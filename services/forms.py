"""Services Forms"""

from django import forms

from .models import Receta, Nutriologist, Profile


class UpdateRecetaForm(forms.Form):
    """Formulario para actualizar receta"""
    fecha_de_cita = forms.DateField (required=True, error_messages={'required':'El campo de usuario no puede estar vacío!'})

    hora_de_cita = forms.CharField(
        max_length=14, 
        required=True,
        error_messages={
            'required':'El campo no puede estar vacío!',
            'max_length':'No puede tener una longitud mayor a 14 caracteres'
        })

    motivo_de_cita = forms.CharField (
        max_length=39, 
        required=True,
        error_messages={
            'required':'Agrega un motivo a la cita',
            'max_length':'No puede tener una longitud mayor a 40 caracteres'
        })

    dctos_asignados = forms.CharField(
        max_length=500,
        required=False,
        error_messages={
            'max_length':'No puede tener una longitud mayor a 500 caracteres'
        }
    )

    estado = forms.BooleanField(required=False)

    activa = forms.BooleanField(required=False)