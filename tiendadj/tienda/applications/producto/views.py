#Siempre los paquetes de terceros
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from django.shortcuts import render
#
from .serializers import ProductSerializer
#
from .models import Product

class ListProductUser(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated] #Doy permiso de mostrar la View  solo si está autenticado

    def get_queryset(self):
        # Para recuperar un usuario:
        print('***************')
        Usuario = self.request.user
        print(Usuario)
        return Product.objects.productos_por_user(Usuario)

class ListProductoStock(ListAPIView):
    # Se lista todos los productos que tienen stock
    serializer_class = ProductSerializer
    #authentication_classes = (TokenAuthentication,) #Esto unicamente hace la autenticación, verifica que el Token EXISTE o que le pertenece a un usuario
    permission_classes = [IsAuthenticated, IsAdminUser] #Doy permiso de mostrar la View  solo si está autenticado y si el usuario es admin

    def get_queryset(self):

        return Product.objects.productos_con_stock()

class ListProductoStock(ListAPIView):
    # Se lista todos los productos que tienen stock
    serializer_class = ProductSerializer
    #authentication_classes = (TokenAuthentication,) #Esto unicamente hace la autenticación, verifica que el Token EXISTE o que le pertenece a un usuario
    permission_classes = [IsAuthenticated, IsAdminUser] #Doy permiso de mostrar la View  solo si está autenticado y si el usuario es admin

    def get_queryset(self):

        return Product.objects.productos_con_stock()


class ListProductoGenero(ListAPIView):
    serializer_class = ProductSerializer 

    def get_queryset(self):
        # Recupero el parámetro
        genero = self.kwargs['gender']
        return Product.objects.productos_con_genero(genero)


