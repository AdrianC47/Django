from django.shortcuts import render
# Necesitamos indicar que solo un usuario logeado pueda ingresar a las vistas de aqui entonces necesito:
from django.contrib.auth.mixins import LoginRequiredMixin # Este paquete
#
from django.views.generic import ListView, View
#
from django.http import HttpResponseRedirect
#
from django.urls import reverse_lazy, reverse
#
from .models import Favorites
#
from applications.entrada.models import Entry


# Create your views here.


class UserPageView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = "entradas_user"
    login_url = reverse_lazy("users_app:user-login")

    def get_queryset(self):

        return Favorites.objects.entradas_user(self.request.user) #mando como parametro el usuario activo

class AddFavoritosView(View):
    
    def post(self, request, *args, **kwargs):
        # recuperar el usuario
        usuario = self.request.user
        # Recuperamos la entrada por el id de la URL
        entrada = Entry.objects.get(id=self.kwargs['pk'])
        # Registramos/Añadimos la entrada a favoritos
        Favorites.objects.create(
            user = usuario,
            entry = entrada,
        )
        return HttpResponseRedirect(
                reverse(
                    'favoritos_app:perfil'
                )
        )