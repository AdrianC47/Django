#Dentro de este archivo irá la personalizacion para los campos del modelo que se mostraran en el html
#Y a este codigo le llamaremos formularios en Django
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
