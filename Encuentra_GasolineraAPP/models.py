from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.


class Roles(models.TextChoices):
    ADMIN = "Admin"
    USUARIO = "Usuario"

    def mostrar(self):
        return self.value
class UsuarioManager(BaseUserManager):
    def create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un email válido")
        user = self.model(email=self.normalize_email(email),**extra_fields )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault("is_susperuser", True)
        return self.create_user(email,password,**extra_fields)



class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)
    rol = models.CharField(max_length=60, choices=Roles.choices, default=Roles.USUARIO)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS = ['username,email,password']

    objects = UsuarioManager()

    def __str__(self):
        return self.username, self.email