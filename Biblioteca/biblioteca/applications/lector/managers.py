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