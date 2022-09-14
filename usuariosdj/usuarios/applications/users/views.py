from django.shortcuts import render

from django.views.generic import CreateView, FormView

from .forms import UserRegisterForm

from .models import User
# Create your views here.


class UserRegisterView(FormView):
    form_class= UserRegisterForm
    template_name = "users/register.html"
    success_url = '/'

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],#asi pongo los extrafields
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'], 
        )
        #
        return super(UserRegisterView, self).form_valid(form)