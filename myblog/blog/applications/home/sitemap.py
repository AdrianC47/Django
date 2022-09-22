from datetime import datetime
from unicodedata import name
from django.urls import reverse_lazy, reverse
from django.contrib.sitemaps import Sitemap
# Importaremos todos los modelos que deseo que se contemplen en el Sitemap
# Models
from applications.entrada.models import Entry

class EntrySitemap(Sitemap):
    # le indicamos con qué frecuencia se realizan cambios sobre el sitemap en el cual estamos trabajando
    changefreq = "weekly" #Semanalmente
    priority = 0.8 # Prioridad de las entradas sobre  las demas páginas
    protocol = 'https'

    # Ahora indico que items van a pertenecer a la clase, por ende sobreescribimos la función items

    def items(self):
        #Aquí va una consulta de qué items va a generar la consulta
        return Entry.objects.filter(public = True) # en este caso seria de todas las entradas pero que estan con estado publicado
    
    # Ahora que ordene cronologicamente en base a la creacion, para ello usaremos la siguiente funcion
    def lastmod(self, obj):
        # Cuando paso el obj le estoy pasando el objeto al cual se conecta el Sitemap, en este caso al modelo Entry 
        return obj.created


#Adicionalmente Django nos pide siempre que sobreescribamos el Sitemap junto con algunas funciones
class Sitemap(Sitemap):
    protocol ='https' #se recomienda siempre poner el https

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly' #semanalmente
    
 