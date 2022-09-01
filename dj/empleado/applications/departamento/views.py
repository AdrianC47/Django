from django.shortcuts import render
from django.views.generic.edit import FormView #el formView es una vista generica un nivel mas abajo que las otras
from .forms import NewDepartamentoForm
# Create your views here.

class NewDepartamentoView(FormView):
    template_name ='departamento/new_departamento.html'
    form_class =NewDepartamentoForm #le paso el formulario que recibira los datos
    success_url = '/'

    def form_valid(self, form):
        print('*****estamos en el form valid**********')

        return super(NewDepartamentoView, self).form_valid(form)