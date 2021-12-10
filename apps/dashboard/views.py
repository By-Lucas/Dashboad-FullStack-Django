from django.shortcuts import render
from visitantes.models import Visitantes
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Criar as views do servidor aqui


@login_required
def index(request):
    #Buscat todos os registros dos visitantes e armazenando nesta variave
    #A forma abaixo ordena os visiatnates(USUARIOS) de forma decrescente por data
    # a forma abaixo tem que ter o traço de "-"  -horario_chegada"
    todos_visitantes = Visitantes.objects.order_by(
        "-horario_chegada"
    )

    # Esta forma mostra a quantidade visitantes aguardando e os demais
    visitantes_aguardando = todos_visitantes.filter(
        STATUS="AGUARDANDO"
    )

    visitantes_em_visita = todos_visitantes.filter(
        STATUS="ATIVO"
    )

    visitantes_finalizado = todos_visitantes.filter(
        STATUS="FINALIZADO"
    )

    hora_atual = timezone.now() #hora atual
    mes_atual = hora_atual.month #mÊs atual

    # pegar visitantes das data colocando o __date para data toda, month pega o mês
    visitantes_mes = todos_visitantes.filter(
        horario_chegada__month = mes_atual
    )


    #colocar nome da s funcoes criadas aqui da mesma forma
    context = {
        "nome_pagina": "Início Dashboard",
        "todos_visitantes": todos_visitantes,
        "visitantes_aguardando": visitantes_aguardando.count(),
        "visitantes_em_visita": visitantes_em_visita.count(),
        "visitantes_finalizado": visitantes_finalizado.count(),
        "visitantes_mes": visitantes_mes.count(),
    }

    return render(request, "index.html", context) #selecionar template