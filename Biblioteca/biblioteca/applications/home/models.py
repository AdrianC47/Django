from django.db import models

# Create your models here.
class Persona(models.Model):
    """Model definition for Persona."""
    full_name = models.CharField('nombres', max_length=50)
    pais = models.CharField('Pais', max_length=30)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativo', max_length=10)#referencia o sobrenombre para identificarlo rapidamente
    

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'persona' #así especifico el nombre de la tabla para la BD
        unique_together = ('pais','apelativo')  #no quiero que se ingrese dentro de mi BD un registro donde pais y apelativo sean los mismos
        constraints = [ #de esta forma añado restricciones
            models.CheckConstraint(check=models.Q(edad__gte =18),name='edad_mayor_18')
        ]

    def __str__(self):
        """Unicode representation of Persona."""
        return self.full_name