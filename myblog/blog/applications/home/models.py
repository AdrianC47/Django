import email
from email import message
from tabnanny import verbose
from django.db import models
# Apps Terceros
from model_utils.models import TimeStampedModel

# Create your models here.
class Home(TimeStampedModel):#Los atributos de fecha de creacion/modificacion
    """ Modelo para datos  de la pantalla home"""

    title = models.CharField('Nombre', max_length=30)
    description = models.TextField()
    about_title = models.CharField('Titulo Nosotros', max_length=50)
    about_text = models.TextField()
    contacto_email = models.EmailField(
        'email de contacto',
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Telefono contacto',
        max_length=20
    )

    class Meta:
        verbose_name = "Pagina Principal"
        verbose_name_plural = "Pagina Principal" 
    
    def __str__(self):
        return self.title + '-' + self.description +'-' + self.contacto_email

class Subscribers(TimeStampedModel):
    """ Modelo para Subscripciones"""
    email = models.EmailField()

    class Meta:
        verbose_name = "Subscriptor"
        verbose_name_plural = "Subscriptores"

    def __str__(self):
        return self.email

class Contact(TimeStampedModel):
    """ Modelo para formulario de contacto """
    full_name = models.CharField('Nombres', max_length=60)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Mensajes"