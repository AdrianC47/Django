from operator import mod
from django.db import models
from django.db.models.signals import post_delete 

from django.http import HttpResponseRedirect
from applications.lector.managers import PrestamoManager
from .signals import update_libro_stock

from applications.libro.models import Libro
from applications.autor.models import Persona
# Create your models here.

class Lector(Persona):

    class Meta:
        verbose_name = "Lector"
        verbose_name_plural = "Lectores"
 

class Prestamo(models.Model):
    lector = models.ForeignKey(
        Lector,
        on_delete=models.CASCADE
    )
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name='libro_prestamo'
    )
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(
        blank=True, 
        null=True
    )
    devuelto = models.BooleanField()

    # Aquí conectamos el manager con el modelo
    objects= PrestamoManager()


    def save(self, *args, **kwargs):
        print('==================================')
        # Aqui al sobreeescribir el metodo save lo que pudiera hacer es validaciones
        # tal como disminuir el stock
        self.libro.stock = self.libro.stock - 1
        self.libro.save( )
        super(Prestamo, self).save(*args, **kwargs)


    class Meta:
        verbose_name = "Mi Prestamo"
        verbose_name_plural = "Prestamos"
    def __str__(self):
        return self.lector.nombres + '-' + self.libro.titulo + '-' + str(self.fecha_prestamo) + '-' + str(self.fecha_devolucion) + '-' +str(self.devuelto)


post_delete.connect(update_libro_stock, sender=Prestamo)