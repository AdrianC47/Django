import datetime
#
from django.shortcuts import render

from django.views.generic import TemplateView

class FechaMixin(object): #Usualmente los mixin deben ir al inicio
    
    def get_context_data(self, **kwargs):#Esta funcion es cuando quiero mandar un contexto al template
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now() #contexto fecha
        return context


class HomePage(FechaMixin,TemplateView):
    template_name = "home/index.html"



class TemplatePruebaMixin(FechaMixin,TemplateView):
    template_name = "home/mixin.html"
