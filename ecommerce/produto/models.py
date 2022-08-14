from django.db import models
import uuid
from django.core.validators import MinValueValidator

"""
Nome fiel usada padrão, porém editada para cada nome cadastrado ser único
Descrição foi utilizado text fiel para uma melhor autonomia das especificações do produto, aceita que campo não seja preenchido
Preço fiel foi escolhido para melhor utilização das casas decimais, e para que junto com outros produtos, como a soma, por exemplo, o sistema não se confunda e tenha dificuldade de executar. Feito validação para que não seja aceito valores negativos. 
Quantidade field utilizada para que recebeçe valores inteiros e positivos. Feito validação para que não seja aceito valores negativos. 
Criado em utiliza horario da criação e não é possível editar.
Atualizado em utiliza exato horario em que arquivo voi primeiramente criado, depois editado. (todas as vezes)
"""

class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100 , unique=True)
    descricao = models.TextField(verbose_name='Descrição')
    preco = models.DecimalField(
        max_digits=7, decimal_places=2,
        verbose_name='Preço (R$)',
        validators = [MinValueValidator(0)],
        help_text='Por favor, caso haja centavos, utilize "." Ex: R$100.50')
    quantidade = models.PositiveIntegerField(default=0, validators = [MinValueValidator(0)])
    criado_em = models.DateTimeField(auto_now_add=True, editable=False)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        