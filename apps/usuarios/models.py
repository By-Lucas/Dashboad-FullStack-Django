from django.db import models
from django.contrib.auth.models import(
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

# Criar modelos aqui.

class UsuarioManager(BaseUserManager):
    #Criar usuario
    def create_user(self, email, password=None):
        usuario = self.model(
            email=self.normalize_email(email)
        )
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save()

        return usuario

    #Criar super usuario
    def create_superuser(self, email, password):
        usuario = self.create_user(
            email = self.normalize_email(email),
            password = password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()

        return usuario



class Usuario(AbstractBaseUser, PermissionsMixin):
    #Campo e-mail
    email = models.EmailField(
        verbose_name="E-mail do usuario",
        max_length=194, #limite de caracteres,
        unique=True, #nao pode ter 2 usuarios com 2 emails
    )

    #Sempre que criar um usuario deixar ele como verdadeiro
    is_active = models.BooleanField(
        verbose_name="Usuário está ativo",
        default=True,
    )

    is_staff = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento",
        default=False,
    )

    #verifica se é um super usuario
    is_superuser = models.BooleanField(
        verbose_name="Usuário é um superusuario",
        default=False,
    )

    USERNAME_FIELD = "email"

    objects = UsuarioManager()
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario"

    def __str__(self):
        return self.email


