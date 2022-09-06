from django.db import models

#Crearemos una clase la cual que represente todas las funciones que van a pertenecer a ese modelo autor

class AutorManager (models.Manager):
    """Managers para el modelo Autor"""

    def buscar_autor(self, kword):

        resultado=self.filter(
            nombre__icontains= kword # esto busca cada caracter en la BD si es similar, es decir si contiene una a , t ,etc
        )

        return resultado