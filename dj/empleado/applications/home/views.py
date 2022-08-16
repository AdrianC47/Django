from django.shortcuts import render
from django.views.generic import TemplateView #llamo a una vista propia de Django(vista generica)
# Create your views here.
#LOGICA DEL NEGOCIO

#Los archivos html deben ir siempre en una carpeta llamada templates
class IndexView(TemplateView): #aqui se hace herencia , esto es la logica, en este caso la logica es muy sencilla ya que simplemente
    template_name = 'home/home.html' #me dice muestrame un template llamado home.html
                                #Sin embargo esta logica puede luego tener metodos/funciones por ejemplo consultar una bd, guardar registros, etc
