from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import ANY
from ecommerce.pedido.models import Pedido
from ecommerce.cliente.models import Cliente
import json

class TestEndpointsPedido(APITestCase):
    
    # SETUP
    def cria_cliente(self):
        cliente = Cliente.objects.create(
            cpf="43963020962",
            )
        return cliente

    def cria_pedido(self):
        cliente = self.cria_cliente()
        pedido = Pedido.objects.create(cliente=cliente, descricao="Compra de 1 mat de ioga")
        return pedido

    """
    OPERAÇÕES POST
    Aqui validamos um request inválida e em seguida uma request válida.
    """
    def test_post_request_pedido_invalido(self):
        request_pedido = {
            "descricao": "123",
            "cliente": None
            }
        """
        Usamos None na request e depois json.dumps, para o None seja substuído por null na criação da request.
        """
        response = self.client.post('/pedidos/', json.dumps(request_pedido), format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      
    def test_post_request_pedido_valido(self):
        cliente = self.cria_cliente()
        request_pedido = {
            "descricao": "1 bola de pilates",
            "cliente": cliente.cpf
            }
        
        response = self.client.post('/pedidos/', request_pedido, format='json')
 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            "id": ANY,
            "descricao": "1 bola de pilates",
            "criado_em": ANY,
            "atualizado_em": ANY,
            "cliente": cliente.cpf}
            )


    """
    OPERAÇÕES GET
    Aqui validamos a operação retorno (get) da lista de instâncias de Pedido e de uma instância específica a partir de seu id.
    """
    def test_get_lista_de_pedidos(self):
        self.cria_pedido()
        response = self.client.get('/pedidos/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
    
    def test_get_pedido(self):
        pedido = self.cria_pedido()
        response = self.client.get(f'/pedidos/{pedido.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "pedido": {
                "id": str(pedido.id),
                "descricao": "Compra de 1 mat de ioga",
                "criado_em": ANY,
                "atualizado_em": ANY,
                "cliente": ANY
                },
            "mensagem": "Pedido vazio. Adicione itens."
            })


    """
    OPERAÇÃO PUT
    Aqui validamos a alteração total (put) dos dados, enviando todo o dicionário dos dados de uma instância de Pedido.
    """
    def test_put_pedido(self):
        pedido = self.cria_pedido()
        self.assertEqual(pedido.descricao, "Compra de 1 mat de ioga")

        request_pedido = {
            "id": str(pedido.id),
            "descricao": "Compra de 1 bola de pilates", # Aqui está a mudança.
            "criado_em": str(pedido.criado_em),
            "atualizado_em": str(pedido.atualizado_em),
            "cliente": pedido.cliente.cpf
            }
        response = self.client.put(f'/pedidos/{pedido.id}/', request_pedido, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pedido_alterado = Pedido.objects.get()
        self.assertEqual(pedido_alterado.descricao, "Compra de 1 bola de pilates")


    """
    OPERAÇÃO PATCH
    Aqui validamos a alteração parcial (patch) dos dados, enviando apenas uma das chaves do dicionário de dados de uma instância de Pedido.
    """

    def test_patch_pedido(self):
        pedido = self.cria_pedido()
        self.assertEqual(pedido.descricao, "Compra de 1 mat de ioga")

        request_pedido = {
            "descricao": "Compra de 1 par de caneleiras",
            }
        response = self.client.patch(f'/pedidos/{pedido.id}/', request_pedido, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pedido_alterado = Pedido.objects.get()
        self.assertEqual(pedido_alterado.descricao, "Compra de 1 par de caneleiras")


    """
    OPERAÇÃO DELETE
    Aqui validamos a operação de exclusão de uma instância do modelo Pedido
    """
    def test_delete_pedido(self):
        pedido = self.cria_pedido()
        response = self.client.delete(f'/pedidos/{pedido.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
