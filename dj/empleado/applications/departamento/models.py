from enum import unique
from django.db import models

# Create your models here.
class Departamento(models.Model):# se especifica que este sera un modelo de los modelos que ya existen en Django
    name = models.CharField('Nombre', max_length=50) #El 'Nombre' hace referencia con qué texto quiero que
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True) #figure el atributo en el administrador de Django, sin embargo el
    anulate = models.BooleanField('Anulado', default=False)     #name es el nombre real 
    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural ='Areas de la Empresa'  
        ordering = ['-name'] #si quiero ordenar inversamente se antepone el -
        unique_together =('name', 'shor_name')#aqui indico que combinados dos o mas  atributos no se repita
    #Por defecto los campos son obligatorios
    def __str__(self):
        return str(self.id) + '-' + self.shor_name  
        # return str(self.id) + '-' + self.name + '-' +self.shor_name+'-'+str(self.anulate)