"""User profile form"""

from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Profile


class ProfileForm(forms.Form):
    """Profile form"""
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