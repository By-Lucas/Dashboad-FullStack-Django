from django.contrib import admin
from usuarios.models import Usuario
# Registar modelos aqui.

#adicionar no administrador o local da tabela USUARIOS
admin.site.register(Usuario)
