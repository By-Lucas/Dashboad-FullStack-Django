from django.contrib import messages
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed

from visitantes.models import Visitantes
from visitantes.forms import (
    VisitantesForm, AutorizaClienteForm
)

from django.utils import timezone

# Criar as views aqui

# Chamar template de registarar clientes(visitantes)
@login_required
def registar_visitante(request):

    form = VisitantesForm()

    if request.method == "POST":
        form = VisitantesForm(request.POST)
        #se o formulario for valido, vai salvar ele
        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.registrador_por = request.user.porteiro
            visitante.save()
            
            #mensagem de regstrado ao registrar
            messages.success(
                request,
                "Cliente registrado com sucesso!"
            )
            # apos salvar o clinete, vai redirecionar para paina principal
            return redirect("index")
        


    context = {
        "nome_pagina": "Registrar cliente",
        "form": form
    }

    return render(request, "registrar_visitante.html", context)

#alterar cliente por visitantes
@login_required
def informacoes_visitantes(request, id):

    visitante = get_object_or_404(
        Visitantes,
        id=id
    )

    form = AutorizaClienteForm()

    if request.method == "POST":
        form = AutorizaClienteForm(
            request.POST,
            instance=visitante
        )
        if form.is_valid(): #se o formulario é valido, ele vai salvar e enviar uma mensagem de sucesso abaixo
            # o nome "salvar_visitante" pode ser alterado por "Cliente" se apresentar algum problema
            visitante_save = form.save(commit=False)

            visitante_save.STATUS = "ATIVO"
            visitante_save.hoaraio_autorizacao = timezone.now()

            #essa parte de salvar autorizacao e horario pode adicionar "visitante_save" em caso de erros
            visitante_save.save()

            messages.success(
                request,
                "Cadastro do cliente autorizado com sucesso"
            )

            return redirect("index")

    context = {
        "nome_pagina": "Informações clientes",
        "visitante": visitante,
        "form": form,
    }

    return render(request,"informacoes_visitantes.html", context)

#opcao de finalizar o visitante
@login_required
def finalizar_visita(request, id):

    if request.method == "POST":
        #Pode mudar o nome da variavel abaixo
        finalizar_visitante = get_object_or_404(
            Visitantes, 
            id=id
        )

        finalizar_visitante.STATUS = "FINALIZADO"
        finalizar_visitante.horario_saida = timezone.now()

        finalizar_visitante.save()

        messages.success(
            request,
            "Cliente finalizado com sucesso"
        )

        return redirect("index")

    #permite que a view seja utilizada apenas com método post
    else:
        return HttpResponseNotAllowed(
            ["POST"],
            "Método não permitido"
        )
