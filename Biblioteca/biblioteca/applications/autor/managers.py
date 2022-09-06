from django.db import models

from django.db.models import Q ##Esta funcion me va a ayudar a hacer las sentencias  de tipo OR

#Crearemos una clase la cual que represente todas las funciones que van a pertenecer a ese modelo autor

class AutorManager (models.Manager):
    """Managers para el modelo Autor"""

    def buscar_autor(self, kword):

        resultado=self.filter(
            nombre__icontains= kword # esto busca cada caracter en la BD si es similar, es decir si contiene una a , t ,etc
        )

        return resultado

    def buscar_autor2(self, kword):

        resultado=self.filter(
            Q(nombre__icontains= kword) | Q(apellidos__icontains = kword)
        )

        return resultado