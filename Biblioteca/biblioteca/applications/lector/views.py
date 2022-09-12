from datetime import date

from django.shortcuts import render
from django.views.generic.edit import FormView

from .models  import Prestamo
from .forms import PrestamoForm
# Create your views here.

class RegistrarPrestamo(FormView):
    template_name= "lector/add_prestamo.html"  
    form_class = PrestamoForm
    success_url = "." #redirecciono a la misma pagina

    def form_valid(self, form): 
    # De esta forma puedo hacer el registro del objeto 
    # Esto crea desde cero un objeto
    #     Prestamo.objects.create(
    #         lector = form.cleaned_data['lector'],
    #         libro = form.cleaned_data['libro'],
    #         fecha_prestamo = date.today(),
    #         devuelto = False
    #     )

    # Esta es otra forma tambien
    # Pero el Save cuando no existe obvio si srea un nuevo registro sin embargo si ésta variable préstamo la cual estamos haciendo el llamado
    # ya existia en la BD, es decir lo hemos recuperado pues este save estuviera actualizando el registro y no creando una nueva instancia
        prestamo = Prestamo (
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo = date.today(),
            devuelto = False
        )
        prestamo.save()#Con esto guardo la instancia

        return super(RegistrarPrestamo, self).form_valid(form)