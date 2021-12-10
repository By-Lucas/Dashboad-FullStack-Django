#parte de criar formulario em django
from django import forms
from django.db import models
from django.db.models import fields
from visitantes.models import Visitantes

class VisitantesForm(forms.ModelForm):
    class Meta:
        model = Visitantes #variavel nao pode estar errada, 
        #esse de baixo exibe apenas o que eu quero mostrar
        fields = [
            "nome_completo", "cpf", "plava_veiculo",
            "numero_casa", "hoaraio_autorizacao",
        ]
        #fields = "__all__" #Representa todos os campos da classe que quero exibir
        
        #mensagens de erro
        error_messagens = {
            "nome_completo": {
                "required": "O nome completo do visitante e obrigatorio para o resgistro."
            },
            "cpf": {
                "required": "O nome CPF do visitante e obrigatorio para o resgistro."
            },
            "data_nascimento": {
                "required": "A data de nascimento completo do visitante e obrigatorio para o resgistro.",
                "invalid": "Por favor, informa um formato valido para a data de nascimento (DD/MM/AAA)"
            },
            "numero_casa": {
                "required": "Por favor, informe o numero da casa a ser visitada."
            },

        }


class AutorizaClienteForm(forms.ModelForm):
    morador_responsavel = forms.CharField(required=True)

    class Meta():
        model = Visitantes
        fields = [
            "morador_responsavel"
        ]
        error_messagens = {
            "morador_responsavel": {
                "required": "Por favor, informe o nome do morador responsável por autorizar a entrada do visitante:"
            }
        }

