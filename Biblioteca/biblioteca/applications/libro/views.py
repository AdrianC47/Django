from django.shortcuts import render

from django.views.generic import ListView

# modelos Local

from .models import Libro

class ListLibros(ListView):

    context_object_name= 'lista_libros'
    template_name = "libro/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        
        return Libro.objects.listar_libros(palabra_clave)


