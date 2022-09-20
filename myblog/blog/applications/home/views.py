import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView,CreateView

# Apps Entrada
from applications.entrada.models import Entry
# Models 
from .models import Home
# Forms
from .forms import SubscribersForm, ContactForm

class HomePageView(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Cargamos el home
        context["home"] = Home.objects.latest('created')
        # contexto de portada
        context["portada"] = Entry.objects.entrada_en_portada() #Contexto/Variable portada
        # Contexto para los artículos en home (in_home)
        context["entradas_home"] = Entry.objects.entradas_en_home()
        # Entradas Recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        # Enviamos Formulario de Subscripción
        context["form"] =  SubscribersForm
        return context
    

class SubscriberCreateView(CreateView):
    # En este caso por el modal de foundation ya no se necesita un template 
    form_class = SubscribersForm #El CreateView guarda un registro en base a la info del formulario
    success_url = "/"

# No siempre es necesario jalar directamente el formulario
class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '/'
#Necesito que este View reciba un html pero bajo el formato del ContactForm
