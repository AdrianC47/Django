from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin): #Le digo que quiero que trabaje con herramientas que 
        list_display =(                #nos ofrece el administrador de Django mediante el admin.ModelAdmin
            'first_name',
            'last_name',
            'departamento',
            'job',
        ) 
        search_fields =  ('first_name',)   
        list_filter = ('job','habilidades')
        #El siguiente parametro solo funciona para las relaciones muchos a muchos
        filter_horizontal=('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)