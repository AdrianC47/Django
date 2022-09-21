from tkinter import Entry
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

from .models import Category, Entry

class EntryListView(ListView):
 
    template_name = "entrada/lista.html"
    context_object_name = "entradas"
    paginate_by = 6

    
    def get_context_data(self, **kwargs): #este metodo sirve para enviar alguna variable extra al template
        context = super(EntryListView, self).get_context_data(**kwargs)
        context["categorias"] = Category.objects.all() # Recuperamos todas las categorias que se tienen en la BD
        return context
    

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        categoria = self.request.GET.get("categoria",'')
        #   Consulta de búsqueda
        resultado = Entry.objects.buscar_entrada(kword,categoria)
        return resultado


class EntryDetailView(DetailView):
    model = Entry
    template_name = "entrada/detail.html"

