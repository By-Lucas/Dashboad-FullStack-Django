from django.db import models

# Criar os moedlos aqui.
# opcoes onde os semi usuarios vao ter acesso e dados de cada um cadastrado

class Porteiro(models.Model):
    #um porteiro sempre sem um porteiro apenas
    usuario = models.OneToOneField(
        "usuarios.Usuario",
        verbose_name="Usuário",
        on_delete=models.PROTECT
    )

    nome_completo = models.CharField(
        verbose_name="Nome completo",
        max_length=194, #tamanho total do campo
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    telefone = models.CharField(
        verbose_name="Telefone de contato",
        max_length= 11,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,  #necessario atualizar o valor sempre que for salvo, mas ta false
        auto_now_add= False, # para a data naos er setada com a hora atual, se colocar tru é ativado
    )

    
    class Meta:
        verbose_name = "Adm Junior"
        verbose_name_plural = "Porteiros"
        db_table = "porteiro" #banco de dados
    
    def __str__(self):
        return self.nome_completo

