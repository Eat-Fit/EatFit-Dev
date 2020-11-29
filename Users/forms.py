"""User profile form"""

from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Profile


class ProfileForm(forms.Form):
    """Profile update form"""
    username= forms.CharField(
        max_length=25, 
        required=True, 
        error_messages={
            'required':'El campo de usuario no puede estar vacio!'
        })
        
    email   = forms.EmailField(required=True)

    # picture = forms.ImageField(required=False)
    picture = CloudinaryFileField(
        required=False,
        options = {
            'gravity':"face", 'height':324, 'width':324, 'crop':"fill"
        })


class NutriologistForm(forms.Form):
    """Nutriologist update profile form"""

    picture = CloudinaryFileField(
        required=False,
        options = {
            'gravity':"face", 'height':324, 'width':324, 'crop':"fill"
        })

    username = forms.CharField(
        max_length=15, 
        required=True, 
        error_messages={
            'required':'El campo de usuario no puede estar vacío!',
            'max_length':'No puede tener una longitud mayor a 15 caracteres'
        })

    email = forms.EmailField(required=True)

    attention_days = forms.CharField(
        required=True,
        max_length=45,

        error_messages={
            'required':'El campo no puede estar vacío!',
            'max_length':'No puede tener una longitud mayor a 50 caracteres'
        }
        )     

    attention_hours = forms.CharField(
        max_length=35,
        required=True,
        error_messages={
            'required':'El campo no puede estar vacío!',
            'max_length':'No puede tener una longitud mayor a 40 caracteres'
        })
    
    age = forms.CharField(required=False, error_messages={'required':'El campo no puede estar vacío!'})

    work_approach = forms.CharField (required=True, error_messages={'required':'El campo no puede estar vacío!'})

    cedula_prof_det = forms.CharField (required=True, error_messages={'required':'El campo no puede estar vacío!'})

    biography = forms.CharField (
        max_length=800,
        required=True,
        error_messages={
            'required':'El campo no puede estar vacío!',
            'max_length':'No puede tener una longitud mayor a 800 caracteres'
        }
        )

    