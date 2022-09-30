from django.db import models


class ProductManager(models.Manager):

    def productos_por_user(self, usuario):
        return self.filter(
            user_created = usuario, # filtro mis productos por mi usuario
        )
    
    def productos_con_stock(self):

        return self.filter( # filtro los productos donde el stock sea 0
            stok__gt = 0,
        ).order_by('-num_sales') #ordenado por el numero de ventas