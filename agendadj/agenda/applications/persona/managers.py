import imp
from django.db import models
#
from django.db.models import Count

class ReunionManager(models.Manager):
 
# Si utilizamos el annotate, nos devuelve un conjunto o un query  set agregado a este query set 
# una nueva columna con el valor de la operación aritmética que nosotros estemos realizando. 
# Sin embargo, si utilizamos el aggregate nos va a devolver un diccionario especificando únicamente 
# el valor, sin otros datos más, únicamente el valor de la función aritmética que nosotros 
# estemos indicando.# Sin embargo como es un diccionario le puedo agregar más elementos al diccionario
# producto de funciones/operaciones aritméticas

    def cantidad_reuniones_job(self):
        resultado = self.values(
            #Aqui voy a indicar en base a qué parametro/atributo quiero que annotate empiece a 
            #agrupar las reunioness y me haga la funcion aritmetica  que le he especificado que en este caso es contar
            'persona__job' # agrupo en base al trabajo
       
        ).annotate(
            cantidad = Count('id') #id de la reunion
        )
        print('******************************')
        print(resultado)
        return resultado