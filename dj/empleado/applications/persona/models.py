from enum import unique
from django.db import models
#
from applications.departamento.models import Departamento
# Create your models here.
class Empleado(models.Model):
    """ Modelo para tabla empleado"""

    JOB_CHOICES =(
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO ')
    )
    # Contador
    # Administrador
    # Economista
    # Otro 
    first_name = models.CharField("Nombres", max_length=60)
    last_name = models.CharField("Apelidos", max_length=60)
    job = models.CharField("Trabajo", max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural ='Empleados de la Empresa'
        ordering = ['last_name']
        unique_together = ('last_name','first_name')    
    
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' +self.last_name 

class Habilidad(models.Model):
    texto = models.CharField("Texto", max_length=60)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural ='Habilidades'
    def __str__(self):
        return str(self.id) + '-' + self.texto