from django import forms

from .models import Prestamo

class PrestamoForm(forms.ModelForm):
 #Usamos la clase Meta para poder trabajar directamente con el modelo 
    class Meta: #En este caso los metadatos lo que van a a hacer es conectar directametne a nuestro modelo prestamo y convertir cada campo en un formulario HTML (internamente)
        model  = Prestamo
        fields =( #son los campos
            'lector',
            'libro'
        )