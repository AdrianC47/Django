# standard library
from datetime import timedelta, datetime
import imp
from django.db import models
from django.conf import settings
#
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
# Apps Terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField


# Managers
from .managers import EntryManager
# Create your models here.

class Category(TimeStampedModel):
    """ Categorias de una entrada   """

    short_name = models.CharField("Nombre Corto", max_length=15, unique=True)
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name + '-' + self.short_name

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
   
    slug = models.SlugField(editable=False, max_length=300) # Atributo para trabajar con las URLS generadas automáticamente , para el SEO


    objects  = EntryManager()
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # calculamos el total de segundos de la hora actual
        now = datetime.now()
        total_time = timedelta(
            # Generamos una cadena 
            hours = now.hour,
            minutes = now.minute,
            seconds = now.second
        )
        # Se genera un número en base al tiempo actual
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique) #convierto mi cadena de texto en un slug para que puda estar en la url

        super(Entry, self).save(*args, **kwargs ) # De esta forma genero el slug unico para la URL a fin de mejorar con el SEO

    def get_absolute_url(self):
        # Aquí tenemos que definir cómo es que se crea la url para cada una de las entradas, entonces revisando mi urls.py
        # se tiene    
        # 'entrada/<slug>/', views.EntryDetailView.as_view(), name='entry-detail'
        # Entonces esta es la URL que necesitaremos para el posicionamiento

        return reverse_lazy(
            'entrada_app:entry-detail', 
            kwargs = { # con el kwargs mando el parametro de la url que en este caso seria el slug
                'slug': self.slug
            }
        )