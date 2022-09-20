#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '', 
        views.HomePageView.as_view(),
        name='index',
    ),  
    path(
        'register-subscription', 
        views.SubscriberCreateView.as_view(),
        name='add-subscription',
    ),  
    path(
        'contact', 
        views.ContactCreateView.as_view(),
        name='add-contact',
    ),  
]