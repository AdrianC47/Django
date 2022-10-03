#
from pyexpat import model
from rest_framework import serializers
# 
from .models import Sale, SaleDetail



class VentaReporteSerializers(serializers.ModelSerializer):
    """ Serializador para ver las ventas en detalle"""

    productos = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = (
            'id',
            'date_sale',
            'amount',
            'count',
            'type_invoce',
            'cancelado',
            'type_payment',
            'state',
            'adreese_send',
            'user',
            'productos'
        )

    def get_productos(self, obj):
        query = SaleDetail.objects.productos_por_venta(obj.id) # Aquí obtengo mi lista de productos
        #Aqui a la lista de productos la serializo con mi serializador   pero para acceder en sí a mi serializador debo poner el .data al final
        productos_serializados = DetalleVentaProductoSerializer(query, many = True).data 
        return productos_serializados

class DetalleVentaProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleDetail
        fields = (
            'id',
            'sale',
            'product',
            'count',
            'price_purchase',
            'price_sale',
        )
        

class ProductDetailSerializers(serializers.Serializer):
    pk = serializers.IntegerField() 
    count = serializers.IntegerField()

class ProcesoVentaSerializer(serializers.Serializer):

    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    productos = ProductDetailSerializers(many=True)

