from dataclasses import fields
from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Repite la Contraseña',
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )    
    class Meta:
        """Meta definition for UserRegisterform."""

        model = User
        #fields = ('__all__')# si quiero que muestre todos los atributos
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero'
        )