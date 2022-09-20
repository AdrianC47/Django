from django.db import models

class EntryManager(models.Manager):
    ## Procedimientos para Entrada

    def entrada_en_portada(self):
        return self.filter(
            public = True, 
            portada = True,
        ).order_by('-created').first() # Primero los ordeno por fecha de creacion para luego 
                                       # cargar el primer elemento que se encuentre  de mis Entradas que sea publico y esté como portada

    def entradas_en_home(self):
        # Devuelve las últimas 4 entradas en home
        return self.filter (
            public = True,
            in_home = True,
        ).order_by('-created')[:4]#Necesitamos unicamente los 4 primeros que encuentre

    def entradas_recientes(self):
        # Devuelve las 6 entradas más recientes  en home
        return self.filter (
            public = True,
        ).order_by('-created')[:6]