from django import forms

from .models import Prestamo

class PrestamoForm(forms.ModelForm):

    class Meta: #Usamos la clase Meta para poder trabajar directamente con el modelo 
        model  = Prestamo
        fields =(
            'lector',
            'libro'
        )