from operator import mod
from django.db import models

from applications.libro.models import Libro

# Create your models here.

class Lector(models.Model):
    nombre = models.CharField(
         max_length=50
    )
    apellidos = models.CharField( 
        max_length=50
    )
    nacionalidad = models.CharField( 
        max_length=20
    )
    edad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre + '-' + self.apellidos + '-' + self.nacionalidad + '-' + self.edad

class Prestamo(models.Model):
    lector = models.ForeignKey(
        Lector,
        on_delete=models.CASCADE
    )
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE
    )
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(
        blank=True, 
        null=True
    )
    devuelto = models.BooleanField()

    def __str__(self):
        return self.lector.nombre + '-' + self.libro.titulo + '-' + self.fecha_prestamo + '-' + self.fecha_devolucion + '-' +self.devuelto