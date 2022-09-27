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