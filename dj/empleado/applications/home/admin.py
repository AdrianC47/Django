from atexit import register
from django.contrib import admin
from .models import Prueba
# Register your models here.

#Le digo a Django que quiero intetractuar con el modelo creado con

admin.site.register(Prueba)