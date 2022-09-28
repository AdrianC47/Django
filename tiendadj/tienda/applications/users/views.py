from rest_framework.views import APIView
#
from django.shortcuts import render
#
#django import
from django.views.generic import TemplateView

# Serializadores
from  .serializers import LoginSocialSerializer
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
        return None