"""empleado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#ESTE ES MI URL PRINCIPAL, AQUI VOY A LLAMAR A LOS DEMAS URL DE LAS APPS
from django.contrib import admin
from django.urls import path, include
from applications.home.views import IndexView #llamo a la clase que esta dentro de la  vista de mi aplicacion home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')), # con el include indico que incluya el otro urls
    path('', include('applications.persona.urls')), # con el include indico que incluya el otro urls
    path('', include('applications.departamento.urls')) # con el include indico que incluya el otro urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Esto es para que vaya generando los links en base a las imagenes que se tenga 
