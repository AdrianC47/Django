# Django
from django.urls import path
# local
from . import views

app_name = "producto_app"

urlpatterns =[
    # lista productos por usuario
    path(
        'api/product/por-usuario/',
        views.ListProductUser.as_view(),
        name='product-producto_by_user'
    ), 
    # lista productos con stock
    path(
        'api/product/con-stock/',
        views.ListProductoStock.as_view(),
        name='product-producto_con_stock'
    ),
    # lista productos por genero 
    path(
        'api/product/por-genero/<gender>/',
        views.ListProductoGenero.as_view(),
        name='product-producto_por_genero'
    ), 
]