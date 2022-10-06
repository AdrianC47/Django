from rest_framework import viewsets

from .models import Colors, Product
#
from .serializers import ColorsSerializer, ProductSerializer, PaginationSerializer, ProductSerializerViewSet

class ColorViewSet(viewsets.ModelViewSet): #Hago uso del ModelViewSet debido a que lo relaciono directo con el modelo
    serializer_class = ColorsSerializer
    # Los ViewSets siempre para inicializarlos nos piden un parámetro, el queryset
    queryset = Colors.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializerViewSet
    queryset= Product.objects.all()
    pagination_class = PaginationSerializer

