from dataclasses import fields
from django import forms
from .models import User
from django.db.models import Q 
from django.contrib.auth import authenticate

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

class LoginForm(forms.Form) : #aqui se hereda del forms debido a que no estoy trabajando con un modelo y formulario directamente

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
 
    def clean(self): #Con el nombre clean  ya sabe directamente Django que debe ser una de las primera funciones a ejecutar
    
        #En este caso los campos de username y password no los tengo debido a que son un método, si bien con el cleaned_data los llamo pues necesito indicar de donde los llamo
        #que seria el Formulario, para ello hago lo siguiente
        cleaned_data = super(LoginForm,self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        
        if not authenticate(username= username, password = password):
            raise forms.ValidationError('Los datos de usuario no son correctos')

        return self.cleaned_data
    
class UpdatePasswordForm(forms.Form):
    
    password1 = forms.CharField(
        min_length=5,
        label='Contraseña',
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    ) 
    password2 = forms.CharField(
        min_length=5,
        label='Contraseña',
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    ) 

class VerificationForm(forms.Form):
    codRegistro = forms.CharField( max_length=50)

    def clean_codRegistro(self):
        codigo = self.cleaned_data['codRegistro']

        if len(codigo) == 6:
            # necesito saber si el codigo que manda le pertenece al usuario que se manda su ID por URL
            # se va a hacer esa validacion en los managers
            # Verificamos si el codigo y el id de usuario son validos:
            activo = User.objects.cod_validation (
                self.kwargs['pk'],
                codigo
            )
            if not activo:
                raise forms.ValidationError('El codigo es incorrecto') 
        else:

            raise forms.ValidationError('El codigo es incorrecto')  