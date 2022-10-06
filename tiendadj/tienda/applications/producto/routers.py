from rest_framework.routers import DefaultRouter
#
from .import viewsets

router = DefaultRouter()

router.register(r'colors',viewsets.ColorViewSet, basename="colors") # r'colors' es lo que sería la ruta

urlpatterns = router.urls #Aquí llamo a las urls de mi objeto router