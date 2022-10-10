from django.utils import timezone
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

#
from applications.producto.models import Product

#
from .serializers import ProcesoVentaSerializer2,VentaReporteSerializers

#
from .models import Sale, SaleDetail

class VentasViewSet(viewsets.ViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset= Sale.objects.all()

    def get_permissions(self):
        if (self.action=='list') or ((self.action=='retrieve')):
            permission_classes= [AllowAny] #permitir acceso a todos
        else:
            permission_classes = [IsAuthenticated]
        
        #Retorna un conjunto de permisos que se han usado pero en base a una comprobacion
        #dentro de todos los permisos que existen en Rest_Framework
        return [permission() for permission in permission_classes] #<=es mas python y es la estructura que debe cumplir nuestro metodo

    def list(self, request, *args, **kwargs):
        queryset = Sale.objects.all() 
        serializer = VentaReporteSerializers(queryset, many=True)#OjO que si es un solo dato que vamos a serializer , ya no va el many=True
        return Response(serializer.data)

    def create(self, request):
        serializer = ProcesoVentaSerializer2(data=request.data) 
        serializer.is_valid(raise_exception = True) 
        venta =  Sale.objects.create(
            date_sale =  timezone.now(),   
            amount =0,
            count = 0,
            type_invoce = serializer.validated_data['type_invoce'], 
            type_payment = serializer.validated_data['type_payment'], 
            adreese_send = serializer.validated_data['adreese_send'], 
            user = self.request.user,

        )
        amount = 0 
        count = 0
        productos = Product.objects.filter(
            id__in= serializer.validated_data['productos'] 

        )
        
        cantidades = serializer.validated_data['cantidades']
        
        ventas_detalle = []
        
        for producto, cantidad in zip(productos, cantidades):
            venta_detalle = SaleDetail( 
                sale = venta,
                product = producto,
                count = cantidad,  
                price_purchase = producto.price_purchase, 
                price_sale = producto.price_sale, 
            )
            amount= amount + producto.price_sale * cantidad 
            count = count + cantidad 
            ventas_detalle.append(venta_detalle)
        
        venta.amount =amount
        venta.count = count
        venta.save()

        #
        SaleDetail.objects.bulk_create(ventas_detalle)  
        return Response({'mensaje': 'Venta exitosa 2'})


    def retrieve(self, request, pk=None):
        #mando primero la lista de las ventas y luego el pk de la venta que quiero
        venta = get_object_or_404(Sale.objects.all(), pk=pk)
        serializer = VentaReporteSerializers(venta)
        return Response(serializer.data)