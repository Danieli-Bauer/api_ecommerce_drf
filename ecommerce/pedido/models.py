from django.db import models
from ecommerce.cliente.models import Cliente
from ecommerce.produto.models import Produto
import uuid
from django.core.validators import MinValueValidator

class Pedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.TextField(blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Pedido: {self.id} - Descrição: {self.descricao}"

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, blank=False)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=False)
    quantidade = models.IntegerField(
        blank=False,
        validators=[MinValueValidator(0)])
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id} - Pedido: {self.pedido} - Produto: {self.produto} - Quantidade: {self.quantidade}"

