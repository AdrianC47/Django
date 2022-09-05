from ast import keyword
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView,DeleteView

# Models

from .models import Empleado
# Forms

from .forms import EmpleadoForm

#1
class ListAllEmpleados(ListView): #Toda vista generica o todo vista basada en clases requiere de un template html
    template_name = 'persona/list_all.html'
    # model = Empleado Si se sobreescribe el metodo getQuerySet ya no es necesario el model
    #para hacer paginacion en Django se hace lo siguiente
    paginate_by = 5
    context_object_name= 'lista' 
    ordering = 'first_name'
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        # si full name fuera jorge pozo y la palabra que viene seria Jo lo que hace icontains es buscar la J dentro de jorge 
        # Entonces si no se ingresa nada pues me lista todo ya que todos los empleados en el full name llevan un espacio
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave #
        )
        print('lista resultado: ',lista)
        return lista


class ListaEmpleadosAdmin(ListView): #Toda vista generica o todo vista basada en clases requiere de un template html
    template_name = 'persona/lista_empleados.html'
    # model = Empleado Si se sobreescribe el metodo getQuerySet ya no es necesario el model
    #para hacer paginacion en Django se hace lo siguiente
    paginate_by = 10
    context_object_name= 'empleados' 
    ordering = 'first_name'
    model=Empleado


#2
class ListByAreaEmpleado(ListView): 
    """Lista Empleados de un Area """
    template_name = 'persona/list_by_area.html'
    context_object_name='empleados'
    # queryset =Empleado.objects.filter( forma menos recomendada de obtener datos mediante consultas
    #     departamento__shor_name='Informática'
    # )

    def get_queryset(self): #manera correcta de hacer los filtros
        # puedo escribir el codigo que yo quiera, siempre debo retornar una lista de elementos
        area = self.kwargs['shorname'] #por medio de el self.kwargs mando a llamar al parametro de la url
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista

#3

class ListByJob(ListView): 
    """Lista Empleados por Trabajo """
    template_name = 'persona/list_by_job.html'
    def get_queryset(self): #manera correcta de hacer los filtros (ojo que son directamente puestos en el path sin get ni post ni na)
        # puedo escribir el codigo que yo quiera, siempre debo retornar una lista de elementos
        trabajo = self.kwargs['job'] #por medio de el self.kwargs mando a llamar al parametro de la url
        lista = Empleado.objects.filter(
             job=trabajo
        )
        return lista
 

#4

class ListEmpleadosByKword(ListView):
    """ Lista empleados por palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('******************')#por medio del request intercepto las solicitudes que se hacen al servidor
        palabra_clave = self.request.GET.get("kword", '')#con el get llamo al input con el id kword
        #print('=========', palabra_clave)
        lista = Empleado.objects.filter(
            first_name= palabra_clave
        )
        print('lista resultado: ',lista)
        return lista


# 5 

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        parametroId = self.request.GET.get("paramId")# se pone '' porque es una tupla
        if(parametroId != None):
            empleado = Empleado.objects.get(id=parametroId) #aqui se usa el get puesto que solo quiero un objeto de toda mi lista de empleados
            lista = empleado.habilidades.all()
        else:
            lista = []
        return lista
        #print(empleado.habilidades.all()) #con el all() recupero todas las habilidades de un empleado

# 1.- Listar todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen a un área de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabras clave
# 5.- Listar habilidades de  un empleado



class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    
    def get_context_data(self, **kwargs): #este metodo sirve para enviar alguna variable extra al template
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #todo un proceso
        context['titulo'] = 'Empleado del mes'
        return context
    


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):#esta vista sirve para registrar algo en un modelo de BD, es una vista generica
    model = Empleado          #para crear registros en el modelo de base de datos
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    # fields = ['first_name', 'last_name', 'job','departamento','habilidades', 'avatar'] #Se requiere del fields para poder indicar qué
                               # atributos del modelo queremos registrar por defecto, o que se pinten en pantalla
    #fields =('__all__') # <=== de esta manera selecciono todos los atributos
    success_url=reverse_lazy('persona_app:empleados_admin') #Tambien se debe indicar la url de la pag a donde se redireccionara una vez hecho un submit del formulario
                                                     #Con el . indico que se redireccione a la misma pag


#Se plantea que se pueda guardar el nombre y apellido en un solo atributo, para ello se intercepta el siguiente 
#método
    def form_valid(self, form):
        #Lógica  del proceso
        #empleado = form.save()#Con esta instruccion lo que estoy diciendo es que almacene el formulario que ya tiene datos validos  en la BD(sin embargno no es muy optimo puesto que se guardaria 2 veces en la BD)
        empleado = (form.save(commit=False))#con esto ya no se hace doble guardado sino solo se crea la instancia
        print(empleado)        
        empleado.full_name = empleado.first_name + ' '+ empleado.last_name
        empleado.save()#Esto es una instancia entonces puedo llamar al metodo save que tiene internamente por la ORM de Django
        return super(EmpleadoCreateView,self).form_valid(form) #con el super heredo de mi clase EmpleadoCreateView la funcion form valid para sobreescribirla

class EmpleadoUpdateView(UpdateView):
    model=Empleado
    template_name = "persona/update.html"

    fields=  ['first_name', 'last_name','full_name', 'job','departamento','habilidades']
    success_url=reverse_lazy('persona_app:empleados_admin')

    # El orden comun  es primero el post y luego el form_valid
    # En el request vienen todas las solicitudes que se hagan por el protocolo HTTP hacia nuestro servidor
    def post(self, request, *args, **kwargs):
        print('*********************MÉTODO POST*************************')
        print('=========================================================')
        print(request.POST) # me manda un diccionario
        print(request.POST['last_name'])# de esta forma recupero valores del metodo post y puedo operar con los mismos
        return super().post(request, *args, **kwargs)

    def form_valid (self, form):
        #Logica del proceso
        print('******************METODO FORM VALID ****************')
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url=reverse_lazy('persona_app:empleados_admin')

 

 #================================================================================
 #=============================INICIO DEL PROYECTO================================
 #================================================================================

 
class InicioView(TemplateView):
    """Vista que carga la pagina de inicio"""
    template_name = "inicio.html"
    