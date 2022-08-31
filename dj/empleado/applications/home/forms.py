#Dentro de este archivo irá la personalizacion para los campos del modelo que se mostraran en el html
#Y a este codigo le llamaremos formularios en Django
from logging import PlaceHolder
from tkinter import CENTER
from django import forms
from .models import Prueba
#Lo que voy a hacer aqui es escribir codigo Python que haga que se conecte los campos que tengo en el modelo mediante un formulario

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad'
        )
        widgets ={
            'titulo': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese el Titulo aquí',
                
                    
                }
            )
        }

    def clean_cantidad(self):#Ojo que el def debe ir a la altura de el class en la indentacion
        cantidad = self.cleaned_data['cantidad'] #aqui recupero el valor del atributo que se ha ingresado en el formulario
        if cantidad <10 : #raise es para excepciones en python
                raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad;