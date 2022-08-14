from django.test import TestCase
from . models import Cliente

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from unittest.mock import ANY
import json

# Create your tests here.

class TestEndpointsCliente(APITestCase):
    """Criação de função para uso nos testes"""
    def adiciona_cliente_test(self):
        c = Cliente(nome="Martin Leandro Peixoto", cpf="93882779969", endereco="Rua Mário Pasqual Casella, 508, São Dimas, Guaratinguetá/SP", telefone="1237744781", email="martin.peixoto@caesar.com")
        c.save()


"""Criação de test com POST
Teste de Cadastro de Cliente válido e iválido."""

    def test_cadastro_cliente_invalido(self):
        request_cliente = {
            "nome": "Bruna",
            "cpf": "11122233344"
        }
        response = self.client.post('/clientes/', request_cliente, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
    def test_cadastro_cliente_valido(self):
        request_cliente = {
            "nome": "Isabel Sophia Mendes",
            "cpf": "89524609797",
            "endereco": "Rua Campina Grande, 482, Ponta D'Areia, Niterói/RJ",
            "telefone": "21989633223",
            "email": "isabel98@clic.com.br",
        }
        response = self.client.post('/clientes/', request_cliente, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 1)
        
"""Criação de test com GET,
Teste de lista de clientes, endpoints e endpoints de cliente inválidos"""
        
    def test_lista_de_clientes(self):
        self.adiciona_cliente_test()
        response = self.client.get('/clientes/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
    
    
    def test_endpoint_cliente(self):
        self.adiciona_cliente_test()
        response = self.client.get('/clientes/93882779969/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_endpoint_cliente_invalido(self):
        response = self.client.get('/clientes/93882779969/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    

"""Criação de test DELETE, teste para deletar cliente"""   
  
    def test_delete_cliente(self):
        self.adiciona_cliente_test()
        response = self.client.delete('/clientes/93882779969/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
"""
Teste para atualizar variavel, primeiro a função busca a outra função adiciona_cliente_test que tem armazenado um cliente, e através do PUT é possível fazer alteração dessas variáveis.
"""        
        
    def test_update_cliente(self):
        self.adiciona_cliente_test()
        request_cliente = {            
            "nome" : "Martin Luther King",
            "cpf" : "93882779969",
            "endereco" : "Rua Mário Pasqual Casella, 508, São Dimas, Guaratinguetá/SP",
            "telefone" : "1237744781",
            "email" : "martin.peixoto@caesar.com"
        }
        response = self.client.put('/clientes/93882779969/', request_cliente, format='json')
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        c = Cliente.objects.get()
        self.assertEqual(c.nome, "Martin Luther King")
        
        