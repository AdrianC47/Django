"""
Proyecto Curso Django
"""
import imp
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
#  SEO
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import EntrySitemap, Sitemap

#URLS PRINCIPALES
urlpatterns_main = [ 
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.entrada.urls')),
    re_path('', include('applications.favoritos.urls')),
    # urls para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


#Objeto Sitemap que genera xml
sitemaps = {
    # Indicamos que el mapa del sitio se genere en base a una estructura
    'site':Sitemap(
        [  
            'home_app:index' # indicamos que la estructura está basada principalmente en nuestra URL principal/raíz
        ]
    ),
    #ahora ya irían nuestras URLS secundarias
    'entradas': EntrySitemap
} 

#URLS generadas
urlpatterns_sitemap = [
      
    path(
        'sitemap.xml', #   nombrePag
        sitemap, # |Indico que es una Estructura SiteMap
        {'sitemaps':sitemaps}, #|Estructura Nuestra  
        name='django.contrib.sitemaps.views.sitemap')
 ]

#Este es el que se lee, entonces concatenamos todas las URLS
urlpatterns =  urlpatterns_main + urlpatterns_sitemap