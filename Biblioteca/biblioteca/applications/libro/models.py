from pickletools import optimize
from django.db import models
from django.db.models.signals import post_save #luego de guardar

# apps terceros
from PIL import Image


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
    stock = models.PositiveIntegerField(default =0)

     # Aquí conectamos el manager con el modelo
    objects= LibroManager()

    def __str__(self):
        return str(self.id) + '-' + self.categoria.nombre + '-'+ self.titulo+ '-' + str(self.fecha)  + '-' + str(self.visitas) +'-'+ str(self.stock)

def optimize_image(sender, instance, **kwargs):   #Se pasan los siguientes parametros
# sender hace referencia hacia donde se ejecuta la funcion
# instance hace referencia a la instancia o registro sobre el cual estamos trabajando
# los keywords que generalmente les pasamos en las funciones que utilizamos o trabajos dentro de la ORMde django
    print('===========================')
    print(instance)
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize= True)


post_save.connect(optimize_image,sender = Libro)