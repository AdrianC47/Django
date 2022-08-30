from django.urls import path
from  . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view())
    
]
