from distutils.command.upload import upload
from tabnanny import verbose
from unicodedata import category
from xml.parsers.expat import model
from django.db import models
from django.conf import settings

# Apps Terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(TimeStampedModel):
    """ Categorias de una entrada   """

    short_name = models.CharField("Nombre Corto", max_length=15, unique=True)
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

class Tag (TimeStampedModel):
    """Etiquetas de un Artículo """
    name  = models.CharField("Nombre", max_length=30)

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

class Entry(TimeStampedModel):
    """ Modelo para entradas o articulos """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, #Hago referencia a mi modelo User de Django
        on_delete=models.CASCADE,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    tag = models.ManyToManyField(Tag)
    title = models.CharField(
        'Titulo',
        max_length=200
    )
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('contenido')
    public = models.BooleanField(default=False) #atributo que determina si el articulo que hemos escrito puede publicarse o no
    image = models.ImageField(
        'Imagen',
        upload_to = 'Entry',
    )
    portada = models.BooleanField(default=False) # Atributo que indica si queremos que este articulo esté en la portada o no
    in_home = models.BooleanField(default=False) # Atributo que indica si queremos que el articulo figure en la pantalla principal
    slug = models.SlugField(editable=False, max_length=300)

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    def __str__(self):
        return self.title