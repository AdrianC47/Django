import datetime
from enum import auto
from statistics import mode
from django.db import models
from django.db.models import Q, Count 
class LibroManager(models.Manager):
    """Managers para el modelo Libro"""

    def listar_libros(self, kword):
    
        resultado=self.filter(#filtro por titulo y por la fecha
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

    def listar_libros_categoria(self,categoria):#mando un parametro
        #SE LISTAN LOS LIBROS!!!
        #similar a un select * from LIBROS where categoria.id = categoria
        return self.filter( ##Filtra y lista todos los LIBROS con el mismo id(paranetro) de la categoria 
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


    def listar_categoria_libros(self):
        # Usamos annotate cuando queremos hacer una anotación en cada objeto que nos devuelva de un queryset, 
        # como si quisiéramos agregar una propiedad extra a cada objeto de tu queryset, pero directo desde la base de datos.
        # En este caso es para añadir el atributo count o cantidad a categoria
        resultado =  self.annotate(
        #En este caso el  num_libros va a ser mi atributo nuevo para mi modelo Categoria
            num_libros=Count('categoria_libro')#Aqui se hace uso de el related_name  
        )

    #SOLO CON EL FIN DE PROBAR SE HACE ESTE FOR
        for r in resultado:
            print("*******************")
            print(r, r.num_libros) ##gracias al annotate es como si el num_libros fuese un nuevo atributo del modelo Categoria
        return resultado #<==Esto es un QuerySet
