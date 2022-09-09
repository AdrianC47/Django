from tabnanny import verbose
from django.db import models

# Create your models here.
# Managers
from .managers import AutorManager 

class Autor(models.Model):
     nombres = models.CharField(
         max_length=50
     )
     apellidos = models.CharField(
         max_length=50
     )
     nacionalidad = models.CharField(
         max_length=20
     )
     edad = models.PositiveIntegerField()

     # Aquí conectamos el manager con el modelo
     objects= AutorManager()
     
     class Meta:
          verbose_name = 'Mi Autor'
          verbose_name_plural = "Autores"

     def __str__(self):
        return str(self.id) + '-' + self.nombres+ '-' + self.apellidos + '-' + self.nacionalidad + '-' + str(self.edad)