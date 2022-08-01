from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

    """
    Validações
    As funções a seguir realizam duas validações:
    1. valida se o nome fornecido tem duas palvras (nome e sobrenome)
    2. valida se o endereço fornecido é composto por pelo menos uma letra
    """
    def validate_nome(self, nome):
        nome_completo = nome.split(" ")
        if len(nome_completo) == 1:
            raise serializers.ValidationError("Forneça pelo menos um nome e um sobrenome.")
        return nome
    
    def validate_endereco(self, endereco):
        existe_letra = any(letra.isalpha() for letra in endereco)
        if existe_letra == False:
            raise serializers.ValidationError("Forneça um endereço com letras.")
        return endereco
