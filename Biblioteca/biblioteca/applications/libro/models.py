from distutils.command.upload import upload
from django.db import models
from .managers import CategoriaManager, LibroManager
# from local apps
from applications.autor.models import Autor

# Create your models here.

class Categoria (models.Model):
    nombre = models.CharField(max_length=30)

    objects= CategoriaManager()
    class Meta:
          verbose_name = 'Mi Categoria'
          verbose_name_plural = "Categorias" 

    def __str__(self):
        return str(self.id) + ' -' + self.nombre

class Libro (models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        #El related name especifica el nombre de la relacion inversa
        related_name='categoria_libro' #cuando alguien quiera llegar al modelo Libro pero desde la relacion que tengo con  categoria quiero que utlice este atributo related_name
    )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(
         max_length=50
    )
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada')
    visitas = models.PositiveIntegerField()

     # Aquí conectamos el manager con el modelo
    objects= LibroManager()

    def __str__(self):
        return str(self.id) + '-' + self.categoria.nombre + '-'+ self.titulo+ '-' + str(self.fecha)  + '-' + str(self.visitas) 