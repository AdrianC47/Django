#
from django.utils import timezone
from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

#
from .models import Sale, SaleDetail
from applications.producto.models import Product
# Serializadores
from .serializers import VentaReporteSerializers, ProcesoVentaSerializer, ProcesoVentaSerializer2

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
    authentication_classes = (TokenAuthentication,)
    permission_classes= [IsAuthenticated]

    serializer_class = ProcesoVentaSerializer

    def create(self, request, *args, **kwargs): #función a sobreescrbir
        serializer = ProcesoVentaSerializer(data=request.data) #aquí descerializo lo que recibo a través del POST
        #
        # Ahora debemos validar si la información es válida
        serializer.is_valid(raise_exception = True) # con el raise indico que me mande una excepción en caso de que los datos no sean correctos
        #Ahora recupero la info que nos están mandando
        # tipo_recibo = serializer.validated_data['type_invoce']
        # print('*******', tipo_recibo)
        venta =  Sale.objects.create(
            date_sale =  timezone.now(),   
            amount =0,
            count = 0,
            type_invoce = serializer.validated_data['type_invoce'], 
            type_payment = serializer.validated_data['type_payment'], 
            adreese_send = serializer.validated_data['adreese_send'], 
            user = self.request.user,
        # Los demás datos se están poniendo por default 
        )
        # variables para venta
        amount = 0 # monto total de venta
        count = 0
        # Recuperamos  los productos de la venta
        productos = serializer.validated_data['productos']
        #
        ventas_detalle = []
        #
        for producto in productos:
            prod = Product.objects.get(id=producto['pk']) #Ojo que aquí va pk debido a que en el serializador está como pk

            # prod = Product.objects.filter(id__in)=[1,2,3,4,5,6] #De esta forma recupero los objetos con este id
            
            venta_detalle = SaleDetail( # Creo mi detalle de venta
                sale = venta,
                product = prod,
                count = producto['count'],#atributo del serializador y del modelo
                price_purchase = prod.price_purchase, # atributo propio del modelo
                price_sale = prod.price_sale, 
            )
            amount= amount + prod.price_sale * producto['count'] # saco el monto toal
            count = count + producto['count'] # saco la cantidad
            #Añado mi detalle a mi lista de detalles
            ventas_detalle.append(venta_detalle)
        
        venta.amount =amount
        venta.count = count # Cantidad de Productos
        venta.save()

        #
        SaleDetail.objects.bulk_create(ventas_detalle)  
        return Response({'mensaje': 'Venta exitosa'}) #Ojo que siempre un CreateAPIView necesita un response como retorno

