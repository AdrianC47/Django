from statistics import mode
from django.db import models

class LibroManager(models.Manager):
    """Managers para el modelo Libro"""

    def listar_libros(self, kword):
    
        resultado=self.filter(
            titulo__icontains= kword,
            fecha__range = ('2000-04-21','2020-05-25')
        )

        return resultado