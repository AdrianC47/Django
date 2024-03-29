import email
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin ):

    GENDER_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otros'),
    )

    username = models.CharField("Usuario",max_length=10, unique=True)
    email = models.EmailField("Email")
    nombres = models.CharField("Nombres",max_length=30, blank=True)
    apellidos = models.CharField("Apellidos",max_length=30, blank=True)
    genero = models.CharField("Genero",max_length=1, choices=GENDER_CHOICES, blank=True)
    codRegistro = models.CharField(max_length=6, blank=True)

    #
    is_staff  = models.BooleanField(default=False)

    #atributo de AbstractBaseUser que permite determinar si el usuario está activo o no (si el email es correcto o no)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos

    class Meta:
        verbose_name = 'Mi Usuario'
        verbose_name_plural ='Usuarios de la Empresa'

    def __str__(self):
        return self.username + ' ' + self.email + ' ' + str(self.password) + ' ' + self.genero + ' ' +str(self.get_full_name())