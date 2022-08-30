from ast import keyword
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

#3

class ListByJob(ListView): 
    """Lista Empleados por Trabajo """
    template_name = 'persona/list_by_job.html'
    def get_queryset(self): #manera correcta de hacer los filtros (ojo que son directamente puestos en el path sin get ni post ni na)
        # puedo escribir el codigo que yo quiera, siempre debo retornar una lista de elementos
        trabajo = self.kwargs['job'] #por medio de el self.kwargs mando a llamar al parametro de la url
        lista = Empleado.objects.filter(
             job=trabajo
        )
        return lista
 

#4

class ListEmpleadosByKword(ListView):
    """ Lista empleados por palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('******************')#por medio del request intercepto las solicitudes que se hacen al servidor
        palabra_clave = self.request.GET.get("kword", '')#con el get llamo al input con el id kword
        #print('=========', palabra_clave)
        lista = Empleado.objects.filter(
            first_name= palabra_clave
        )
        print('lista resultado: ',lista)
        return lista
# 1.- Listar todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen a un área de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabras clave
# 5.- Listar habilidades de  un empleado
