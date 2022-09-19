from django.contrib import admin

from .models import Home, Subscribers, Contact
# Register your models here.
admin.site.register(Home)
admin.site.register(Subscribers)
admin.site.register(Contact)