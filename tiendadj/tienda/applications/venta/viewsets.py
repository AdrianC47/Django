from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

#
from applications.producto.models import Product

#
from .serializers import ProcesoVentaSerializer2,VentaReporteSerializers

#
from .models import Sale, SaleDetail

class VentasViewSet(viewsets.ViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes= [IsAuthenticated]
    serializer_class = VentaReporteSerializers
    queryset= Sale.objects.all()