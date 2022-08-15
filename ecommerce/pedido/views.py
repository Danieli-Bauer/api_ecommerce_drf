from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import PedidoSerializer, ItemSerializer
from .models import Pedido, Item
from .helpers import PedidoHelper
from ecommerce.produto.models import Produto
from django_filters.rest_framework import DjangoFilterBackend
from django.db import transaction

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cliente', ]
    
    """
    A função a seguir sobrescreve a função retrieve (verbo HTTP get) para que retorne todas as informações do pedido configuradas em helpers.py
    """
    def retrieve(self, request, pk='id'):
        """
        A seguir tentamos encontrar a instância de Pedido em questão pelo seu id.
        """
        try:
            pedido = self.get_object()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Não encontrado."})

        """
        Caso a instância seja encontrada, invoca-se o helper de Pedido, para retornar os detalhes do pedido.
        """
        pedido_helper = PedidoHelper(pedido)
        pedido_detalhes = pedido_helper.retorna_detalhes_pedido()
        
        """
        Se ao pedido não tiver sido adicionado nenhum item, retorna-se uma resposta HTTP 200 junto com os dados básicos do pedido e uma mensagem de que o pedido está vazio.
        """
        if not pedido_detalhes:
            pedido_serializer = self.get_serializer(pedido)
            return Response(data={"pedido": pedido_serializer.data, "mensagem": "Pedido vazio. Adicione itens."}, status=status.HTTP_200_OK)

        """
        Caso tenham sido adicionados itens ao pedido, retorna-se o conjunto de informações organizadas pelo helper.
        """
        return Response(status=status.HTTP_200_OK, data={"pedido": pedido_detalhes})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    """
    A função a seguir sobrescreve a função create (verbo HTTP post) para que, em caso de fornecimento de dados válidos de criação de item, a quantidade de produtos do item altere a quantidade de produtos em estoque. 
    
    Os produtos em estoque são as instâncias do modelo Produto (da aplicação ecommerce.produto). Se a quantidade de um determinado produto é maior que 0, então há quantidade positiva desse produto em estoque, e o item que adiciona esse produto poderá ser criado, deduzindo da quantidade daquele produto em estoque a exata quantidade do produto fornecida no item. 
    
    Se não houver quantidade suficiente do produto em estoque, o item não poderá ser criado e a operação post retornará um erro HTTP 400.
    """

    def create(self, request):
        item = self.serializer_class(data=request.data)
        if item.is_valid():
            """
            Guarda-se na variável quantidade_item a quantidade de items do pedido.
            """
            quantidade_item = request.data['quantidade']
            """
            Guarda-se na variável produto o produto relacionado ao item do pedido.
            """
            produto = Produto.objects.get(id=request.data['produto'])
            """
            Guarda-se na variável quantidade_produto a quantidade de produtos em estoque.
            """
            quantidade_produto = produto.quantidade
            """
            Se a quantidade de produtos fornecida na criação do item for maior do que a quantidade de produtos em estoque, então retorna-se um erro HTTP 400.
            """
            if int(quantidade_item) > int(quantidade_produto):
                return Response({"status": "Erro", "mensagem": "Este produto não está disponível em estoque ou você deve tentar uma quantidade menor."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                """
                Se a quantidade de produtos fornecida na criação do item for menor ou igual à quantidade de produtos em estoque, então se deduz da quantidade em estoque a quantidade de produtos do item.
                """
                produto.quantidade = produto.quantidade - int(request.data['quantidade'])
                with transaction.atomic():
                    produto.save()
                    item.save()
                return Response({"data": item.data}, status=status.HTTP_201_CREATED)    
        """
        Se os dados fornecidos não forem válidos, retorna-se um erro HTTP 400.
        """
        return Response({"status": "Erro", "mensagem": "Dados inválidos."}, status=status.HTTP_400_BAD_REQUEST) 

