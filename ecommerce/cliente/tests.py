from django.test import TestCase
from . models import Cliente

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from unittest.mock import ANY
import json

# Create your tests here.

class TestEndpointsCliente(APITestCase):
    '''Criação de função para uso nos testes'''
    def adiciona_cliente_test(self):
        c = Cliente(nome="Martin Leandro Peixoto", cpf="93882779969", endereco="Rua Mário Pasqual Casella, 508, São Dimas, Guaratinguetá/SP", telefone="1237744781", email="martin.peixoto@caesar.com")
        c.save()
