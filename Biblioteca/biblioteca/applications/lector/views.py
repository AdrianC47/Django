from datetime import date


from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models  import Prestamo, Libro
from .forms import PrestamoForm, MultiplePrestamoForm
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

        #Aqui se disminiuira el stock

        libro = form.cleaned_data['libro']
        libro.stock = libro.stock - 1
        libro.save()#aqui actualizo el libro
        return super(RegistrarPrestamo, self).form_valid(form)

class AddPrestamo(FormView):
    template_name= "lector/add_prestamo.html"  
    form_class = PrestamoForm
    success_url = "." #redirecciono a la misma pagina

    def form_valid(self, form): 

# Se plantea como ejercicio el caso en el que un lector hace un prestamo y aun no devuelve el libro
# pero a pesar de ello vuelve a pedir prestado el mismo libro pero sin haber devuelto el ejemplar
# get_or_create funciona así: si el registro existe nos lo devuelve y si no pues lo crea

        #Para el get or create necesito dos variables: 
        # el object que va a ser donde va a estar el objeto, si es que en caso se ha creado/recuperado
        # el created que va a ser un booleano que nos diga si se ha creado o no el registro

        obj, created = Prestamo.objects.get_or_create(
            lector = form.cleaned_data['lector'],# si se obtiene del formulario un objeto con lector y libro
            libro = form.cleaned_data['libro'], # y buscandolo lo encuentra con el parametro devuelto en false solo lo obtiene y no lo crea
            devuelto = False,
            #Aquí añado los valores que no estan en el formulario para que si no encuentra pues lo cree
            defaults={
                'fecha_prestamo' :date.today()
            }
        )
        
        if created:

            return super(AddPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect('/error/')

    
class ErrorView(TemplateView):
    template_name = "lector/error.html"


class AddMultiplePrestamo(FormView):
    template_name= "lector/add_multiple_prestamo.html"  
    form_class = MultiplePrestamoForm
    success_url = "." #redirecciono a la misma pagina

    def form_valid(self, form): 
        #
        print(form.cleaned_data['lector'])
        print(form.cleaned_data['libros'])
        # 
        prestamos = []
        for l in form.cleaned_data['libros']:
            prestamo = Prestamo (
                lector = form.cleaned_data['lector'],
                libro = l,
                fecha_prestamo = date.today(),
                devuelto = False
            )
            prestamos.append(prestamo)#se añade a la lista el objeto, si bien se pudiera usar el save pues hacer eso por cada registro no es optimo

        libros = []
        
        for l in prestamos:
            l.libro.stock -= 1
            libros.append(l.libro)

        Libro.objects.bulk_update(
            libros,
            ['stock'],
        )
        # la siguiente funcion es de la ORM de django y es para guardar varios objetos de un modelo a partir de una lista
        # y lo hace en una sola consulta, lo que hace nuestro codigo mas optimo
        Prestamo.objects.bulk_create(  
            prestamos
        )
        
        return super(AddMultiplePrestamo, self).form_valid(form)    
    