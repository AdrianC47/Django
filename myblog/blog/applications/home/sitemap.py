from datetime import datetime
from unicodedata import name
from django.urls import reverse_lazy, reverse
from django.contrib.sitemaps import Sitemap
# Importaremos todos los modelos que deseo que se contemplen en el Sitemap
# Models
from applications.entrada.models import Entry

class EntrySitemap(Sitemap):

    changefreq = "weekly" #Semanalmente - le indicamos con qué frecuencia se realizan cambios sobre el sitemap en el cual estamos trabajando
    priority = 0.8 # Prioridad de las entradas sobre  las demas páginas
    protocol = 'https'

    # Ahora indico que items van a pertenecer a la clase, por ende sobreescribimos la función items

    def items(self):
        #Aquí va una consulta de qué items va a generar las urls
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

    # Para casos donde no estén relacionados directamente a lo que se genera con un modelo debemos añadir unas funciones

    def lastmod(self, obj):#lo usamos para indicar un periodo de fecha de creacióm , por defecto es el día
        return datetime.now()
    
    def location(self,obj):# Hace referencia a como genera O donde está la URL
        return reverse_lazy(obj) # Me redirecciona a la misma página
    
 