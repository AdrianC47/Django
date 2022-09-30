#Siempre los paquetes de terceros
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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