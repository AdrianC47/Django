from django.shortcuts import render

from django.views.generic import CreateView, FormView

from .forms import UserRegisterForm
# Create your views here.


class UserRegisterCreateView(FormView):
    form_class= UserRegisterForm
    template_name = "users/register.html"
    success_url = '/'