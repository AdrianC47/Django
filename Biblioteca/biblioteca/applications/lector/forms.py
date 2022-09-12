from msilib.schema import CheckBox
from django import forms
from applications.libro.models import Libro

from .models import Prestamo

class PrestamoForm(forms.ModelForm):
 #Usamos la clase Meta para poder trabajar directamente con el modelo 
    class Meta: #En este caso los metadatos lo que van a a hacer es conectar directametne a nuestro modelo prestamo y convertir cada campo en un formulario HTML (internamente)
        model  = Prestamo
        fields =( #son los campos
            'lector',
            'libro'
        )

class MultiplePrestamoForm(forms.ModelForm):
    # esto me dice que voy a recuperar un conjunto relacionado o de un MODELO en particular de nuestra base de datos
    libros = forms.ModelMultipleChoiceField(
        #Entonces debo indicar qué modelo es ése, por ello necesita el queryset 
        queryset= None,# primero lo declaro ya luego lo obtengo por medio de una funcion
        required = True,# al menos un libro necesito
        widget=forms.CheckboxSelectMultiple, #aqui indico que quiero que se muestre con un Checkbox de multiple seleccion
    )

    class Meta:
        model = Prestamo
        fields = (
            'lector',
        )
    
    
    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        #aqui se puede hacer cualquier proceso que se desee
        self.fields['libros'].queryset = Libro.objects.all() #aqui ya obtengo todos los libros y se asigna el valor al queryset