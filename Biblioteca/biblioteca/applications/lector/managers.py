import datetime
from django.db import models
from django.db.models import Q, Count, Avg, Sum

class PrestamoManager(models.Manager):
    """Managers/Procedimientos para el modelo Prestamo"""

    def libros_promedio_edades(self):
        resultado = self.filter(
            libro__id='6'
        ).aggregate(
            promedio_edad = Avg('lector__edad'),#Accedo a la edad del lector en relacion con un libro prestado
            suma_edad = Sum('lector__edad')# se pueden ir añadiendo más y mas funciones ya que es un diccionario
        )
        return resultado

    def num_libros_prestados(self):
        resultado = self.values(
            #Aqui voy a indicar en base a qué parametro/atributo quiero que annotate empiece a 
            #agrupar los libros y me haga la funcion aritmetica  que le he especificado que en este caso es contar
            'libro'
        ).annotate(
            num_prestados=Count('libro')
        )
        for r in resultado:
            print('=========================')
            print(r, r['num_prestados'])#así accedo al diccionario

        return resultado 