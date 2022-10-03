from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

#
from .models import Sale, SaleDetail
# Serializadores
from .serializers import VentaReporteSerializers, ProcesoVentaSerializer

class ReporteVentasList(ListAPIView):
    
    serializer_class = VentaReporteSerializers

    def get_queryset(self):
    
        return Sale.objects.all()

class ReporteVentasList(ListAPIView):
    
    serializer_class = VentaReporteSerializers

    def get_queryset(self):
    
        return Sale.objects.all()

class RegistrarVenta(CreateAPIView):
    """ """
    #Para poder registrar una venta necesito un usuario con permisos
    # authentication_classes = (TokenAuthentication,)
    # permission_classes= [IsAuthenticated]

    serializer_class = ProcesoVentaSerializer

    def create(self, request, *args, **kwargs): #función a sobreescrbir
        serializer = ProcesoVentaSerializer(data=request.data) #aquí descerializo lo que recibo a través del POST
        #
        # Ahora debemos validar si la información es válida
        serializer.is_valid(raise_exception = True) # con el raise indico que me mande una excepción en caso de que los datos no sean correctos
        #Ahora recupero la info que nos están mandando
        tipo_recibo = serializer.validated_data['type_invoce']
        print('*******', tipo_recibo)
        return Response({'code': 'ok'}) #Ojo que siempre un CreateAPIView necesita un response como retorno

