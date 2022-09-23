from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns =[
    path(
        'personas/',
        views.ListaPersonas.as_view(),
        name='personas'
    )    
]