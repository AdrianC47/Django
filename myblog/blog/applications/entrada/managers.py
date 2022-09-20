from django.db import models

class EntryManager(models.Manager):
    ## Procedimientos para Entrada

    def entrada_en_portada(self):
        return self.filter(
            public = True, 
            portada = True,
        ).order_by('-created').first() # Primero los ordeno por fecha de creacion para luego 
                                       # cargar el primer elemento que se encuentre  de mis Entradas que sea publico y esté como portada
