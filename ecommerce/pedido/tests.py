from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import ANY
from ecommerce.pedido.models import Pedido, Item
from ecommerce.cliente.models import Cliente
from ecommerce.produto.models import Produto
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

class TestEndpointsItem(APITestCase):

    # SETUP
    def cria_cliente(self):
        cliente = Cliente.objects.create(cpf="43963020962")
        return cliente

    def cria_produto_quant_10(self):
        produto = Produto.objects.create(quantidade=10, preco=5.0)
        return produto

    def cria_pedido(self):
        cliente = self.cria_cliente()
        pedido = Pedido.objects.create(cliente=cliente)
        return pedido

    def cria_item_quant_1(self):
        pedido = self.cria_pedido()
        produto = self.cria_produto_quant_10()
        item = Item.objects.create(quantidade=1, pedido=pedido, produto=produto)
        return item


    """
    OPERAÇÕES POST
    Aqui validamos três requests inválidas e em seguida uma request válida.
    A primeira request inválida contém dados inválidos (exceto pela quantidade), a segunda contém como quantidade um valor negativo, e a terceira tenta criar um item quando não há produtos em estoque (o que também provocará um erro, pois um item que remete a um produto só pode ser criado se há quantidade suficiente do produto em estoque).
    """
    def test_post_request_item_invalido(self):
        request_item = {
            "quantidade": 1,
            "pedido": "",
            "produto": None
            }
        """
        Usamos None na request e depois json.dumps, para o None seja substuído por null na criação da request.
        """
        response = self.client.post('/itens/', json.dumps(request_item), format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {
            "status": "Erro", 
            "mensagem": "Dados inválidos."
            })

    def test_post_request_item_invalido_quant_negativa(self):
        pedido = self.cria_pedido()
        produto = self.cria_produto_quant_10()
        request_item = {
            "quantidade": -1,
            "pedido": str(pedido.id),
            "produto": str(produto.id)
            }

        response = self.client.post('/itens/', json.dumps(request_item), format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {
            "status": "Erro", 
            "mensagem": "Dados inválidos."
            })

    def test_post_valida_request_item_quando_nao_ha_estoque(self):
        produto = self.cria_produto_quant_10() # Instância de produto com quantidade (estoque) de 10.
        pedido = self.cria_pedido()
        """
        A request a seguir tenta criar um item com quantidade superior à disponível em estoque.
        """
        request_item = {
            "quantidade": produto.quantidade + 1,
            "pedido": pedido.id,
            "produto": produto.id
            }
        response = self.client.post('/itens/', request_item)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {
            "status": "Erro", 
            "mensagem": "Este produto não está disponível em estoque ou você deve tentar uma quantidade menor."})

    def test_post_request_item_valido(self):
        produto = self.cria_produto_quant_10()
        pedido = self.cria_pedido()
        request_item = {
            "quantidade": 1,
            "pedido": pedido.id,
            "produto": produto.id
            }
        response = self.client.post('/itens/', request_item, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['data'], {
                "id": ANY,
                "quantidade": 1,
                "criado_em": ANY,
                "atualizado_em": ANY,
                "pedido": str(pedido.id),
                "produto": str(produto.id)
            })
        """
        Quando um item é criado com uma quantidade (nesse caso, 1), sua quantidade é reduzida do atributo quantidade do produto (nesse caso, o novo valor para quantidade do produto seria 10 - 1 = 9)
        """
        produto_atualizado = Produto.objects.get()
        self.assertEqual(produto_atualizado.quantidade, 9)

        """
        Um item só pode ser criado se ligado via primary_key a um pedido.
        Quando fazemos a operação get no pedido, devemos receber um dicionário com a seguinte estrutura:
        {
            "pedido": {
                "pedido": {dados do pedido},
                "items": [{item}, {item1}, {item2}],
                "total": produto.preco * item.quantidade
            }
        }
        
        Nas asserções a seguir, vamos validar se o total do pedido está certo. O nosso produto teste tem o preço de 5.00, e a quantidade do item adicionado é 1.
        O valor total do pedido deve ser 5.00 * 1 = 5.00.
        """
        item = Item.objects.get()
        response_pedido = self.client.get(f'/pedidos/{pedido.id}/', format="json")
        self.assertEqual(response_pedido.json()['pedido']['total'], item.quantidade * produto.preco)
        self.assertEqual(response_pedido.json()['pedido']['total'], 5.00)


    """
    OPERAÇÕES GET
    Aqui validamos a operação retorno (get) da lista de instâncias de Item e de uma instância específica a partir de seu id.
    """
    def test_get_lista_de_itens(self):
        item = self.cria_item_quant_1()

        response = self.client.get('/itens/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
    
    def test_get_item(self):
        item = self.cria_item_quant_1()
        response = self.client.get(f'/itens/{item.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
                "id": str(item.id),
                "quantidade": 1,
                "criado_em": ANY,
                "atualizado_em": ANY,
                "pedido": ANY,
                "produto": ANY
            })


    """
    OPERAÇÃO PUT
    Aqui validamos a alteração total (put) dos dados, enviando todo o dicionário dos dados de uma instância de Item.
    """
    def test_put_item(self):
        item = self.cria_item_quant_1()
        self.assertEqual(item.quantidade, 1)

        request_item = {
            "id": str(item.id),
            "quantidade": 2, # Aqui está a mudança
            "criado_em": str(item.criado_em),
            "atualizado_em": str(item.atualizado_em),
            "pedido": str(item.pedido.id),
            "produto": str(item.produto.id)
            }
        response = self.client.put(f'/itens/{item.id}/', request_item, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item_alterado = Item.objects.get()
        self.assertEqual(item_alterado.quantidade, 2)


    """
    OPERAÇÃO PATCH
    Aqui validamos a alteração parcial (patch) dos dados, enviando apenas uma das chaves do dicionário de dados de uma instância de Item.
    """
    def test_patch_item(self):
        item = self.cria_item_quant_1()
        self.assertEqual(item.quantidade, 1)

        request_item = {
            "quantidade": 2, 
            }
        response = self.client.patch(f'/itens/{item.id}/', request_item, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item_alterado = Item.objects.get()
        self.assertEqual(item_alterado.quantidade, 2)


    """
    OPERAÇÃO DELETE
    Aqui validamos a operação de exclusão de uma instância do modelo Item
    """
    def test_delete_item(self):
        item = self.cria_item_quant_1()
        response = self.client.delete(f'/itens/{item.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

