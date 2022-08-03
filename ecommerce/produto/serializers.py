from rest_framework import serializers
from .models import Produto

#Validações extra para que não seja possível cadastrar os campos NOME e DESCRIÇÃO apenas com números.

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        
    def validate_nome(self, nome):
        so_numero = nome.isnumeric()
        if so_numero == True:
            raise serializers.ValidationError("Nome do produto não pode conter só números. Forneça um novo nome.")
        return nome
    
    def validate_descricao(self, descricao):
        so_numero = descricao.isnumeric()
        if so_numero == True:
            raise serializers.ValidationError("Descrição do produto não pode conter só números. Forneça uma nova descrição.")
        return descricao
