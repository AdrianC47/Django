from django.db import models

# Create your models here.
class Departamento(models.Model):# se especifica que este sera un modelo de los modelos que ya existen en Django
    name = models.CharField('Nombre', max_length=50, editable=False) #El 'Nombre' hace referencia con qué texto quiero que
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True) #figure el atributo en el administrador de Django, sin embargo el
    anulate = models.BooleanField('Anulado', default=False)     #name es el nombre real 
#Por defecto los campos son obligatorios
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' +self.shor_name+'-'+str(self.anulate)