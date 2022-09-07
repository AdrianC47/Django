import datetime
from enum import auto
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

        return self.filter( ##Filtra y lista todos los libros con el mismo id de la categoria 
            categoria__id = categoria
        ).order_by('titulo')

    def add_autor_libro(self,libro_id, autor):

        libro = self.get(id=libro_id)#obtengo el libro con la pk del path
        libro.autores.add(autor)#si quiero eliminar solo va el remove a cambio del add
        return libro

class CategoriaManager(models.Manager):
    """Managers para el modelo Categoria"""

    def categoria_por_autor(self, autor):
        return self.filter( 
            categoria_libro__autores__id = autor#aqui primero se pone el atributo del related name en el modelo Libro
        ).distinct()# este distinct lo que hace es que me muestre una sola vez cada resultado obtenido