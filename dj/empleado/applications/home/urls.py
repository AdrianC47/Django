from lib2to3.pgen2.token import NAME
from django.urls import path
from  . import views

urlpatterns = [
    path('prueba/', views.IndexView.as_view()), #siempre que trabaje con algo que hereda de Django se pone el .as_view
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/',views.ModeloPruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name ='prueba_add'),
    path(
        'resume-foundation/',
        views.ResumeFoundationView.as_view(),
        name='resume_foundation'
        ), 
]
