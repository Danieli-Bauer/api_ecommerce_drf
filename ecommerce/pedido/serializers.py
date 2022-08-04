from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Pedido, Item

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'