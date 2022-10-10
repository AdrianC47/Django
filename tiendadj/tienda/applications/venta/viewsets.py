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

    # authentication_classes = (TokenAuthentication,)
    # permission_classes= [IsAuthenticated]
    queryset= Sale.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Sale.objects.all()
        #serializer = self.get_serializer(queryset, many=True)
        return Response({'probando':'viewsets1'})

    def retrieve(self, request, pk=None):
        return Response({'probando':'viewsets2'})