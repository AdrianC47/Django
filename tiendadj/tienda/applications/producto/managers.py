from django.db import models


class ProductManager(models.Manager):

    def productos_por_user(self, usuario):
        return self.filter(
            user_created = usuario, # filtro mis productos por mi usuario
        ) 