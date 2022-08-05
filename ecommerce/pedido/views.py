from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import PedidoSerializer, ItemSerializer
from .models import Pedido, Item
from .helpers import PedidoHelper
from ecommerce.produto.models import Produto


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    
    """
    A função a seguir sobrescreve a função retrieve (verbo HTTP get) para que retorne todas as informações do pedido configuradas em helpers.py
    """
    def retrieve(self, request, pk='id'):
        try:
            pedido = self.get_object()
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"Erro": "Pedido não encontrado."})

        pedido_helper = PedidoHelper(pedido)
        pedido_detalhes = pedido_helper.verifica_pedido()

        if not pedido_detalhes:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'Pedido': 'Pedido vazio. Adicione itens.'})

        return Response(status=status.HTTP_200_OK, data={"Detalhes_do_pedido": pedido_detalhes})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
