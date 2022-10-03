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

    def productos_con_genero(self, genero):
        # lista productos por genero
        if genero == 'M':   # M Mujer V Varón cualquier otro caracter abarca a todos
            mujer = True
            varon = False
        elif genero == 'V': 
            mujer = False
            varon = True
        else: 
            varon = True
            mujer = True
        return self.filter(
            woman = mujer,
            man = varon
        ).order_by('created')

    def filtrar_productos(self, **filtros):
        return self.filter(
            man = filtros['man'],
            woman = filtros['woman'],
            name__icontains = filtros['name'],
        )