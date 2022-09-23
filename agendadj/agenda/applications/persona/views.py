from ast import keyword
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
#
from rest_framework.generics import ListAPIView

from .models import Person
#
from .serializers import PersonSerializer


class ListaPersonas(ListView):
    template_name ="persona/personas.html"
    context_object_name = "personas"

    def get_queryset(self):
        return Person.objects.all() #Hago que me retorne toa la lista de Personas

class PersonListApiView(ListAPIView):
    # Indico bajo qué serializador queremos que muestre el resultado

    serializer_class= PersonSerializer

    def get_queryset(self): # Con esto genero una Lista
        return Person.objects.all() #Hago que me retorne toa la lista de Personas


class PersonListView(TemplateView):
    template_name = "persona/lista.html"


class PersonSearchApiView (ListAPIView): #Crearemos otra vista de tipo API para aprender  mejor

    serializer_class = PersonSerializer ## Ponemos el Serializador

    def get_queryset(self): # Con esto genero una Lista
        # Pero y si quiero que me retorne un resultado  pero filtrando  en base a un parametro de busqueda

        # Filtramos datos
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains= kword
        )