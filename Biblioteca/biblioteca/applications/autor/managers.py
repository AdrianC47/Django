from django.db import models

#Crearemos una clase la cual que represente todas las funciones que van a pertenecer a ese modelo autor

class AutorManager (models.Manager):
    """Managers para el modelo Autor"""

    def listar_autores(self):

        return self.all()