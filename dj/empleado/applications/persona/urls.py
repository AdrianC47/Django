from django.urls import path
from  . import views

app_name ='persona_app' #esto me sirve para dar un nombre a todo el conjunto (arreglo) de url
urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view(), name='listaEmpleados'),
    path('listar-by-area/<shorname>/', views.ListByAreaEmpleado.as_view(), name='listEmArea'), #con el <> emvio parametros 
    path('listar-by-job/<job>/', views.ListByJob.as_view(), name='listEmJob'), #con el <> emvio parametros 
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view(), name='listEmKeyword'), #con el <> emvio parametros 
    path('lista-habilidades-empleado/', views.ListHabilidadesEmpleado.as_view(), name='listHab'), #con el <> emvio parametros 
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='DetalleEmpleado'),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='AddEmpleado'),  
    path(
        'success/',
        views.SuccessView.as_view(),
        name='correcto'
        ),
    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
        ),
    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
        ),

]
