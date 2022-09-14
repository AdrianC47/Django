from django.shortcuts import render

from django.views.generic import CreateView

from .forms import UserRegisterForm
# Create your views here.


class UserRegisterCreateView(CreateView):
    form_class= UserRegisterForm
    template_name = "users/register.html"
    success_url = '/'