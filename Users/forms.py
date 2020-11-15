"""User profile form"""

from django import forms


class ProfileForm(forms.Form):
    """Profile form"""
    username= forms.CharField(
        max_length=25, 
        required=True, 
        error_messages={
            'required':'El campo de usuario no puede estar vacio!'
        })
        
    email   = forms.EmailField(required=False)
    picture = forms.ImageField(required=False)