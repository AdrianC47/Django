from django.contrib import admin

from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display= (
        'username',
        'nombres',
        'email',
        'password',
        'genero',
        User.get_full_name,
        'id',
    )

admin.site.register(User, UserAdmin)