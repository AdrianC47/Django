#
from tabnanny import verbose
from model_utils.models import TimeStampedModel
#
from django.db import models
#
from .managers import ReunionManager

#

class Hobby(TimeStampedModel):
    """Pasatiempos"""
    hobby = models.CharField('PasaTiempo', max_length=50)
    def __str__(self):
        return str(self.id) +' ' + self.hobby


class Person(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """

    full_name = models.CharField(
        'Nombres', 
        max_length=50,
    )
    job = models.CharField(
        'Trabajo', 
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=15,
        blank=True,
    )

    hobbies = models.ManyToManyField(Hobby)


    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return self.full_name + ' '+str(self.id)

class Reunion(TimeStampedModel):
    """Modelo para Reunion"""
    persona= models.ForeignKey(Person, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    asunto = models.CharField(
        'Asunto de la Reunión',
        max_length=100
    )

    objects =  ReunionManager()
    class Meta:
        verbose_name = 'Reunion'
        verbose_name_plural = 'Reuniones'

    def __str__(self):
        return self.asunto + ' ' + str(self.id)