from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

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
    
    def perform_create(self, serializer):
            videoRecuperado = serializer.validated_data['video']
            print("el video es " ,str(videoRecuperado))
            if not videoRecuperado:
                print("No se ha pasado un video")
                serializer.save(
                    video="https://www.youtube.com/watch?v=B0FbyLbxdKo"
                )
            else:
                serializer.save()
                print("Si se ha pasado un video")
                
    def list(self, request, *args, **kwargs):#Tambien puedo sobreescribir este metodo list a fin de poder filtrar
        # mis productos por usuario
        queryset = Product.objects.productos_por_user(self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk): #method is used to return data of a single object.
    #     prod = self.get_object()
    #     serializer = self.get_serializer(prod)
    #     print("hola")
    #     print(str(prod))
    #     return Response(serializer.data) 

    # def update(self, request, pk=None):
    #     prod = self.get_object()        
    #     serializer = self.get_serializer(prod, data =request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     print("se ha actualizado")
    #     return Response(serializer.data) 

    # def destroy(self, request, *args, **kwargs):
    #     prod = self.get_object()  
    #     self.perform_destroy(prod)
    #     print("Se ha eliminado")
    #     return Response(status=status.HTTP_204_NO_CONTENT)

