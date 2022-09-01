from django.shortcuts import render
from django.views.generic import TemplateView, ListView,CreateView  #llamo a una vista propia de Django(vista generica)

from .models import Prueba
from .forms import PruebaForm
#LOGICA DEL NEGOCIO

#Los archivos html deben ir siempre en una carpeta llamada templates
class IndexView(TemplateView): #aqui se hace herencia , esto es la logica, en este caso la logica es muy sencilla ya que simplemente
    template_name = 'home/prueba.html' #me dice muestrame un template llamado home.html
                                #Sin embargo esta logica puede luego tener metodos/funciones por ejemplo consultar una bd, guardar registros, etc


class ResumeFoundationView(TemplateView):
    template_name = "home/resume_foundation.html"

class PruebaListView(ListView):
    template_name= 'home/lista.html'
    #Como esto lo que hace va a listar pues necesita mas cosas por ejemplo qué vamos a listar, para ello pasaremos un parametro
    queryset=['Heroes del Silencio','Nirvana','Oasis']##llamado queryset
    #Para poder llamar o mostrar un objeto/variable en un template necesito un object_context_name y se usan SIEMPRE {{}}
    context_object_name= 'lista_prueba' 


class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/lista_prueba.html"
    context_object_name='lista_prueba'

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'

class HomeTemplate1View(TemplateView):
    template_name = "home/home1.html"

class HomeTemplate2View(TemplateView):
    template_name = "home/home2.html"

class HomeTemplate3View(TemplateView):
    template_name = "home/home3.html"