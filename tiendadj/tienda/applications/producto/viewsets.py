from rest_framework import viewsets

from .models import Colors
#
from .serializers import ColorsSerializer

class ColorViewSet(viewsets.ModelViewSet): #Hago uso del ModelViewSet debido a que lo relaciono directo con el modelo
    serializer_class = ColorsSerializer
    # Los ViewSets siempre para inicializarlos nos piden un parámetro, el queryset
    queryset = Colors.objects.all()