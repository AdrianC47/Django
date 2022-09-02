from django.shortcuts import render
from django.views.generic.edit import FormView #el formView es una vista generica un nivel mas abajo que las otras
from .forms import NewDepartamentoForm
from django.views.generic import ListView
from applications.persona.models import Empleado
from .models import Departamento
# Create your views here.




class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name= 'departamentos'



# Aquí lo que voy a realizar es realizar un registro de dos modelos en una sola vista utilizando el FormView
# y un formulario que no depende del modelo 
class NewDepartamentoView(FormView):
    template_name ='departamento/new_departamento.html'
    form_class =NewDepartamentoForm #le paso el formulario que recibira los datos
    success_url = '/'

    def form_valid(self, form):
        print('*****estamos en el form valid**********')
        depa = Departamento(#se puede crear un registro tambien de esta forma
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname']
        )
        depa.save()#Con esto guardo la instancia

        nombre = form.cleaned_data['nombre']#aqui recupero los datos ingresados en el formulario
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create( #Para hacer un registro uso la ORM de Django y el create por ende aqui no es necesario el save()
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento=depa
        )  

        return super(NewDepartamentoView, self).form_valid(form)