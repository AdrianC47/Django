import email
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, FormView, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm, VerificationForm
from .functions import code_generator
from .models import User
# Create your views here.


class UserRegisterView(FormView):
    form_class= UserRegisterForm
    template_name = "users/register.html"
    success_url = '/'

    def form_valid(self, form):
        #
        #Generamos el codigo
        codigo = code_generator()
        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],#asi pongo los extrafields
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'], 
            codRegistro = codigo,
        )
        # Enviar el codigo al email del usuario
        asunto = 'Confirmacion de email'
        mensaje = 'Codigo de verificacion ' +codigo
        email_remitente = "adriancabrera2104@gmail.com"
 
        #
        send_mail(asunto,mensaje, email_remitente, [form.cleaned_data['email'],])#aqui se manda un [] debido a que se puede mandar a mas de un correo aunque no se lo recomienda por el consumo
        # Redirigir a pantalla de validaicon 

        return HttpResponseRedirect(reverse(
            'users_app:user-verification',
            kwargs={'pk':usuario.id}
            )
        )

class LoginUser(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')
    #obtengo el formulario

    def form_valid(self, form):
        user = authenticate( #Con esta funcion haria la comparativa para la autenticación
            username= form.cleaned_data['username'], #recupero los datos del formulario
            password = form.cleaned_data['password']
        )
        #Con esta funcion haria el login pasandole primero el contexto (request) porque  necesita a ese usuario asignarle a un proyecto de la sesion actual
        # y le mando el usuario para que esté activo durante toda la sesión

        login(self.request, user) 
       
        return super(LoginUser, self).form_valid(form)

class LogoutView(View):
    
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('users_app:user-login')
        )

class UpdatePasswordFormView(LoginRequiredMixin,FormView):
    template_name = "users/update.html"
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')
    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(  
            username =usuario.username,  
            password = form.cleaned_data['password1']
        )
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
        logout(self.request)    
        return super(UpdatePasswordFormView, self).form_valid(form)

class CodeVerificationView(FormView):
    template_name = "users/verification.html"
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:user-login')

    def get_form_kwargs(self): # se sobreescribe la funcion,  con algun valor para que lo puedan leer nuestros formularios
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({# Con esto se dice que se envie nuevos kwargs a nuestro formulario
            'pk':self.kwargs['pk']
        })
        return kwargs

    def form_valid(self, form):
        #
        User.objects.filter(
            id = self.kwargs['pk']
        ).update(
            is_active =True
        )
        return super(CodeVerificationView, self).form_valid(form)