from django.shortcuts import render
from django.views.generic import ListView

#models
from .models import Empleado
#1
class ListAllEmpleados(ListView): #Toda vista generica o todo vista basada en clases requiere de un template html
    template_name = 'persona/list_all.html'
    model = Empleado
    context_object_name= 'lista' 

#2
class ListByAreaEmpleado(ListView): 
    """Lista Empleados de un Area """
    template_name = 'persona/list_by_area.html'
    # queryset =Empleado.objects.filter( forma menos recomendada de obtener datos mediante consultas
    #     departamento__shor_name='Informática'
    # )

    def get_queryset(self): #manera correcta de hacer los filtros
        # puedo escribir el codigo que yo quiera, siempre debo retornar una lista de elementos
        area = self.kwargs['shorname'] #por medio de el self.kwargs mando a llamar al parametro de la url
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista
 

# 1.- Listar todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen a un área de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabras clave
# 5.- Listar habilidades de  un empleado
