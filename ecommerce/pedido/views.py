from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PedidoSerializer, ItemSerializer
from .models import Pedido, Item

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
