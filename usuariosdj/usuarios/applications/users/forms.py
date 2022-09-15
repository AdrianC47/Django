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
    
    # def clean_password1(self):
    #     pass1 = self.cleaned_data['password1']
    #     if  (len(pass1) <5) :
    #         print('==================================')
    #         print(pass1)
    #         self.add_error('password1', 'La longitud de la contraseña debe ser igual o mayor a 5')

    # def clean_password(self):
    #     pass2 = self.cleaned_data['password2']
    #     if  (len(pass2) <5) :
    #         print('==================================')
    #         print(pass2)
    #         self.add_error('password2', 'La longitud de la contraseña debe ser igual o mayor a 5')
            
    def clean_password2(self):
        if self.cleaned_data['password1']!= self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden')    #añado un error especificando el campo del formulario en el cual quiero mostrarlo

class LoginForm(forms.Form) : #aqui se herda del forms debido a que no estoy trabajando con un modelo y formulario directamente

    username = forms.CharField(
 
        label='Username',
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'style': '{margin: 10px}',
            }
        )
    )
    password = forms.CharField(
        min_length=5,
        label='Contraseña',
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    ) 
 
    