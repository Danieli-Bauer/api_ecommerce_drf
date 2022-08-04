from django.db import models
from ecommerce.cliente.models import Cliente
import uuid

class Pedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.TextField(blank=False)
    client = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Pedido: {self.id} - Descrição: {self.descricao}"

