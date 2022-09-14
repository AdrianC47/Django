from dataclasses import fields
from django import forms
from .models import User
from django.db.models import Q 


class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        min_length=5,
        label='Contraseña',
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        min_length=5,
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
    
 

    def clean_password2(self):
        if self.cleaned_data['password1']!= self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden')    #añado un error especificando el campo del formulario en el cual quiero mostrarlo


 
    