from rest_framework.views import APIView
#
from firebase_admin import auth
#
from django.shortcuts import render
#
#django import
from django.views.generic import TemplateView

# Serializadores
from  .serializers import LoginSocialSerializer
# Modelos
from .models import User
# Create your views here.

class LoginUser(TemplateView):
    template_name = "users/login.html"


class GoogleLoginView(APIView):
    serializer_class = LoginSocialSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        # serializer = LoginSocialSerializer(data=request.data) # tambien se puede hacer de ésta forma
        serializer.is_valid(raise_exception=True) # si no es valido el is_Valid nos acepta una excepción
        #Ahora sí recupero la info
        id_token = serializer.data.get('token_id')
        #
        decoded_token =  auth.verify_id_token(id_token)
        #
        email = decoded_token['email']
        name = decoded_token['name']
        avatar = decoded_token['picture'] # para google el avatar o la url donde esta la ft del usuario es picture
        verified = decoded_token['email_verified'] #Esto es para saber si la cuenta está verificada
        #
        #Primero debo verificar que el usuario SÍ exista en la BD, entonces voy a usar el get_or_create, funcion de la ORM de django
        #Para el get or create necesito dos variables: 
        # el object que va a ser donde va a estar el objeto, si es que en caso se ha creado/recuperado
        # el created que va a ser un booleano que nos diga si se ha creado o no el registro

        usuario, created = User.objects.get_or_create(
            email=email,  #Especifico en base a que quiero que recupere el usuario
            defaults={    #Aquí añado los valores que no estan en mi vista  para que si no encuentra pues lo cree
               'full_name' : name,
               'email' : email,
               'is_active' : True,
                #Los demás atributos no se están poniendo debido a que no son obligatorios
            }
        )
        #login(usuario)
        return None