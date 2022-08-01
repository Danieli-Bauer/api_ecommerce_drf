from django.db import models
from localflavor.br.models import BRCPFField
from django.core.validators import RegexValidator

"""
O modelo Cliente é composto por dados pessoais e de contato:
Dados pessoais: Nome completo, CPF, endereço
Dados de contato: Telefone e e-mail

Nenhum dos campos pode ser deixado em branco.

O telefone é validado com uso de uma expressão regular que só permite a criação de uma instância do modelo cliente se o número tiver um formato compatível com o padrão brasileiro. 
"""

REGEX_TELEFONE = RegexValidator(r'^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$', 'Insira um número de telefone válido. Telefones móveis: (XX) 9XXXX-XXXX Telefones fixos: (XX) XXXX-XXXX')

class Cliente(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name="Nome completo",
        blank=False)
    cpf = models.BRCPFField(
        "CPF",
        max_length=11,
        primary_key=True,
        verbose_name="CPF",
        help_text="Digite seu CPF no formato 11122233344")
    endereco = models.TextField(verbose_name="Endereço", blank=False)
    telefone = models.CharField(
        max_length=15,
        help_text="Digite o telefone nos formatos: (XX) XXXX-XXXX ou (XX) 9XXXX-XXXX",
        validators=[REGEX_TELEFONE],
        unique=True,
        blank=False
    )
    email = models.EmailField(max_length=255, unique=True, blank=False)
    criado_em = models.DateTimeField(auto_add_now=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Nome: {self.nome} - CPF: {self.cpf}'
    
    
