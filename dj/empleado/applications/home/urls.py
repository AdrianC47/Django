from django.urls import path
from  . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()), #siempre que trabaje con algo que hereda de Django se pone el .as_view
]
