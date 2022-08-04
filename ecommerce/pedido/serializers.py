from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Pedido, Item

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
    
    """
    A função a seguir evita que o usuário insira somente números como descrição.
    """    
    def validate_descricao(self, descricao):
        so_numero = descricao.isnumeric()
        if so_numero == True:
            raise serializers.ValidationError("Descrição do produto não pode conter só números. Forneça uma nova descrição.")
        return descricao


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'