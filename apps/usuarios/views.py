from django.shortcuts import render
from django.http import HttpResponse
from visitantes.models import Visitantes
# Criar as views do servidor aqui

def index(request):
    #Buscat todos os registros dos clientes e armazenando nesta variave
    #
    todos_visitantes = Visitantes.objects.all()


    #colocar nome da pagina dashboard
    context = {
        "nome_pagina": "Início Dashboard",
        "todos_visitantes": todos_visitantes
    }

    return render(request, "index.html", context) #selecionar template

