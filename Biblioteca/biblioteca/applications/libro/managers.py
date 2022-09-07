import datetime
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

    def listar_libros2(self, kword,fecha1,fecha2):
    
    #Siempre es recomendable validar lo que sería fechas debido al formato de algunos navegadores

        date1 = datetime.datetime.strptime(fecha1,"%Y-%m-%d").date
        date2 = datetime.datetime.strptime(fecha2,"%Y-%m-%d").date

        resultado=self.filter(
            titulo__icontains= kword,
            fecha__range = (date1,date2)
        )

        return resultado

    def listar_libros_categoria(self,categoria):

        return self.filter(
            categoria__id = categoria
        ).order_by('titulo')