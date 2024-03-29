from ast import keyword
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
#
from rest_framework.generics import (
      ListAPIView,
      CreateAPIView, 
      RetrieveAPIView,
      DestroyAPIView,
      UpdateAPIView,
      RetrieveUpdateAPIView
)

from .models import Person, Reunion
#
from .serializers import ( 
    PersonSerializer,
    PersonaSerializer,
    PersonaSerializer2,
    PersonaSerializer3,
    ReunionSerializer,
    ReunionSerializer2,
    ReunionSerializerLink,
    PersonPagination,
    CountReunionSerializer
)


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

class PersonCreateView(CreateAPIView):

    serializer_class = PersonSerializer


class PersonDetailView(RetrieveAPIView): # Vista para ver el detalle API de una clase
    # A diferencia del DetailView, aqui ya no se trabaja con el parámetro model sino con el parámetro query set
    # Donde dentro de éste parámetro voy a especificar un conjunto de datos donde se va a hacer la búsqueda

    serializer_class = PersonSerializer
    queryset= Person.objects.all() #Ojo que tambien se pueden hacer filtros

class PersonDeleteView(DestroyAPIView):

    serializer_class = PersonSerializer
    queryset= Person.objects.all() #Ojo que tambien se pueden hacer filtros

class PersonUpdateView(UpdateAPIView):

    serializer_class = PersonSerializer
    queryset= Person.objects.all()

class PersonRetrieveUpdateView(RetrieveUpdateAPIView):

    serializer_class = PersonSerializer
    queryset= Person.objects.all()

# Call for Serializers.Serializer

class PersonApiLista(ListAPIView):
    """
        Vista para interactuar con Serializadores
    """
    #serializer_class = PersonaSerializer
    serializer_class = PersonaSerializer3
    def get_queryset(self): # Con esto genero una Lista
        return Person.objects.all() #Hago que me retorne toa la lista de Personas


 

class ReunionApiLista(ListAPIView):

    serializer_class = ReunionSerializer
    def get_queryset(self):  
        return Reunion.objects.all() 

class ReunionApiListaLink(ListAPIView):

    serializer_class = ReunionSerializerLink
    def get_queryset(self):  
        return Reunion.objects.all() 

class PersonPaginationList(ListAPIView):
    """
        Lista Personas con Paginacion
    """
    serializer_class = PersonaSerializer
    pagination_class = PersonPagination#Tiene que ser igualado a un serializador o estructura que contemple paginacion

    def get_queryset(self): 
        return Person.objects.all()

class ReunionByPersonJob(ListAPIView):
    """
        Lista Personas agrupadas por trabajo
    """
    serializer_class = CountReunionSerializer
    def get_queryset(self):  
        return Reunion.objects.cantidad_reuniones_job() 