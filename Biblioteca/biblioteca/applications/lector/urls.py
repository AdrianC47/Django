
from django.contrib import admin
from django.urls import path
from . import views

app_name ='lector_app'
urlpatterns = [
    path(
        'prestamo/add/',
        views.AddPrestamo.as_view(),
        name="prestamo-add"
    ),

    path(
        'error/',
        views.ErrorView.as_view(),
        name="PaginaNoEncontrada"
    ),
]
