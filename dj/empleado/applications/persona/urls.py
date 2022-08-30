from django.urls import path
from  . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-by-area/<shorname>/', views.ListByAreaEmpleado.as_view()), #con el <> emvio parametros 
    
]
