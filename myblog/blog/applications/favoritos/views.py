from django.shortcuts import render
# Necesitamos indicar que solo un usuario logeado pueda ingresar a las vistas de aqui entonces necesito:
from django.contrib.auth.mixins import LoginRequiredMixin # Este paquete
#
from django.views.generic import ListView
#
from django.urls import reverse_lazy, reverse
#
from .models import Favorites

# Create your views here.


class UserPageView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = "entradas_user"
    login_url = reverse_lazy("users_app:user-login")

    def get_queryset(self):

        return Favorites.objects.entradas_user(self.request.user) #mando como parametro el usuario activo