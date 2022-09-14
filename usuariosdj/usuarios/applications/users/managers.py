from django.db import models
#
from django.contrib.auth.models import BaseUserManager
# Un Manager (o manejador) es la interfaz a través de la cual se proveen las operaciones de consulta o 
# queries de la base de datos a los modelos de Django    
class UserManager(BaseUserManager,models.Manager):
    # En este caso debido a que estamos trabajando con el AbstractUser y el Manager pues lo que debemos hacer es sobreescribir funciones

# el is_staff hace referencia a que si el usuario que esta creandose puede on no acceder al admin
# el is_superuser hace referencia a que si el usuario que se esta creando es o no un superusuario

    def _create_user(self, username,email, password, is_staff, is_superuser,**extra_fields): 
        user = self.model (
            username = username,
            email = email,
            is_staff=is_staff, #son booleanos
            is_superuser=is_superuser, #son booleanos
            #el password debo encriptarlo
            **extra_fields
        )
        user.set_password(password) #por medio de esta funcion que trae el BaseUserM ya se encripta automaticamente la password y ahora sí se guarda
        #self.db hace referencia a la bd con la cual estoy trabajando
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self,username,email, password,**extra_fields):# los extra_fields hacen referenccia a cualquier otro atributo que se agregue
         #funcion privada
        return self._create_user(username,email,password,True,True,**extra_fields) #se debe indicar si el usuario es activo(que puede acceder al admin)