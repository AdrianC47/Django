from pickletools import optimize
from django.db import models
from django.db.models.signals import post_save, pre_save # post_save luego de guardar

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
# los keywords que generalmente les pasamos en las funciones que utilizamos o trabajos dentro de la ORM de django
    print('===========================')
    print(instance)
    if instance.portada: #pregunto si a mi instancia(modelo Libro) le estan mandando una portada 
        portada = Image.open(instance.portada.path) #abro la imagen
        portada.save(instance.portada.path, quality=20, optimize= True) #optimizacion


# Se conecta la funcion con la que quiero trabajar y el modelo, es decir quiero que se ejecute esta funcion 
post_save.connect(optimize_image,sender = Libro)   #Cuando se guarde qué registro(Libro) quiero que se ejecute una función (optimize_image)


def funcion_para_PreSave(sender, instance, **kwargs):
    print('***********************************')
    print(instance)
    if instance.stock:
        instance.stock = instance.stock +1


pre_save.connect(funcion_para_PreSave, sender = Libro)