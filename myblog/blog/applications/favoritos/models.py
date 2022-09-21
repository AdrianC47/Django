from enum import unique
from tabnanny import verbose
from django.db import models
from django.conf import settings
# Apps Terceros
from model_utils.models import TimeStampedModel
#
from applications.entrada.models import Entry
#
from .managers import FavoritesManager

# Create your models here.

class Favorites(TimeStampedModel):
    """Modelo para Favoritos"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE
    )

    entry = models.ForeignKey(
        Entry, 
        related_name='entry_favorites',
        on_delete=models.CASCADE
    )

    objects= FavoritesManager()

    class Meta:
        #Cuando un usuario guarde algún blog favorito, no nos gustaría que guarde el mismo blog como favorito, una única vez
        #Para ello uso el unique_together
        unique_together = ('user', 'entry') #tanto el usuario con una misma entrada que tengan el mismo ID no se van a poder registrar 2 veces
        verbose_name = 'Entrada Favorita'
        verbose_name_plural = "Entradas Favoritas"

    def __str__(self):
        return self.entry.title