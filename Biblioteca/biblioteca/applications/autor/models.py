from tabnanny import verbose
from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(
         max_length=50
    )
    apellidos = models.CharField(
         max_length=50
    )
    nacionalidad = models.CharField(
         max_length=30
    )
    edad = models.PositiveIntegerField()

    class Meta:
          verbose_name = 'Mi Autor'
          verbose_name_plural = "Autores"

    def __str__(self):
        return self.nombre+ '-' + self.apellidos + '-' + self.nacionalidad + '-' + str(self.edad)