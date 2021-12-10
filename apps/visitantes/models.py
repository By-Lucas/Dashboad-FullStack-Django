from django.db import models

# Create your models here.

class Visitantes(models.Model):
    #colocar status no adm do django para ver as informacoes de finalizacoes e as demais mostradaas abaixo
    STATUS_VISITANTES = [
        ("AGUARDANDO", "Aguardando autorização"),
        ("EM_VISITA", "Em visita"),
        ("FINALIZADO", "Visita finalizada")
    ]


    STATUS = models.CharField(
        verbose_name="Status",
        max_length=10,
        choices=STATUS_VISITANTES,
        default="AGUARDANDO", #VALOR DA ESTUTURA STATUS
    )


    #Nome completo
    nome_completo = models.CharField(
        verbose_name = "Nome completo",
        max_length = 194
    )


    #CPF
    cpf = models.CharField(
        verbose_name="CPF",
        max_length= 11,
        blank=True,
    )


    #modelos usado para datas
    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=True, #adicionar automaticamente
        blank=False,
       
    )


    #Modelo usado para numeros de casa , pesquisar depois sobre
    numero_casa = models.PositiveBigIntegerField(
        verbose_name="Numeração do cliente",
    )


    #placa do veiculo, codigo o cliente ou email
    plava_veiculo = models.CharField(
        verbose_name="Email do cliente", #Veiculo
        max_length=150,
        blank=False, #essa funcao serve para o campo ter prioridade como NAO obrigatorio se estiver TRUE
        null=True,
    )


    #modelo usado para tempos ou Horario do cadastro
    horario_chegada = models.DateTimeField(
        verbose_name="Horario do cadastro",
        auto_now_add=True,
    )


    #Horário de saida do condomínio
    horario_saida = models.DateTimeField(
        verbose_name= "Horário da finalização",
        auto_now=False,
        blank=True, #essa funcao serve para o campo ter prioridade como NAO obrigatorio se estiver TRUE
        null=True, 
    )


    #Horario de autorização de entrada
    hoaraio_autorizacao = models.DateTimeField(
        verbose_name="Horário da autorização cadastral",
        auto_now=False,
        blank=True, #essa funcao serve para o campo ter prioridade como NAO obrigatorio se estiver TRUE
        null=True
    )


    #Nome do morados responsável por autorizar
    morador_responsavel = models.CharField(
        verbose_name="Nome responsável por autorizar",
        max_length=194,
        blank=True #essa funcao serve para o campo ter prioridade como NAO obrigatorio se estiver TRUE
    )


    #Porteiro responsável pelo registro
    registrador_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Administrador responsável pelo registro",
        on_delete=models.PROTECT
    )


    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida

        return "Horario de finalização não resgistrada"

    def get_horario_autorizacao(self):
        if self.hoaraio_autorizacao:
            return self.hoaraio_autorizacao

        return "Cliente aguardando autorização"

    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel

        return "Cliente aguardando autorização"

    def get_placa_veiculo(self): #veiculo, email ou código
        if self.plava_veiculo:
            return self.plava_veiculo

        return "E-mail não cadastrado" #Veiculo
    
    def get_status_display(self):
        if self.STATUS:
            status_vis = self.STATUS
            return status_vis

    #colocar pontos e traços no CPF
    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)

            cpf_parte_1 = cpf[0:3]
            cpf_parte_2 = cpf[3:6]
            cpf_parte_3 = cpf[6:9]
            cpf_parte_4 = cpf[9:]

            cpf_formatado = f"{cpf_parte_1}.{cpf_parte_2}.{cpf_parte_3}-{cpf_parte_4}"

            return cpf_formatado

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitantes" #tudo minusculo


    def __str__(self):
        return self.nome_completo



