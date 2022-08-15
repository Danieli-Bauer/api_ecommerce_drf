from .models import Item

"""
A classe a seguir contém uma série de funções que ajudarão a viewset de Pedido a retornar no método retrieve (verbo HTTP get) as informações de Pedido customizadas.

As informações de pedido customizadas incluirão:
1. as informação básicas do modelo de Pedido
2. as informações de cada item adicionado à instância de Pedido
3. o valor total produto da quantidade de produtos adicionados ao item pelo preço de cada produto. 
"""

class PedidoHelper:

    """
    A classe que auxiliará Pedido se inicializará recebendo uma instância de Pedido.
    Os outros atributos são:
    1. o self.valor_total do pedido, incializado como 0;
    2. uma lista vazia chamada self.itens correspondente aos itens que serão adicionados ao pedido;
    3. um dicionário vazio (self.detalhes_pedido) onde serão preenchidos os dados do pedido (em forma de dicionário), a lista de itens do pedido, e o valor total do pedido.
    """
    def __init__(self, pedido):
        self.pedido = pedido
        self.valor_total = 0
        self.itens = []
        self.detalhes_pedido = {'pedido': {}, 'itens': [], 'total': 0}

    """
    O método a seguir é a função principal do helper. 
    Este método verifica quais itens estão relacionados ao pedido em questão e chama os métodos que calculam um valor para o atributo self.valor_total do pedido e que atualizam o atributo self.detalhes_pedido, para retornar o atributo self.detalhes_pedido.
    """
    def retorna_detalhes_pedido(self):

        """
        Verifica-se aqui quais itens estão relacionados ao pedido em questão.
        """
        self.itens = Item.objects.filter(pedido=self.pedido)
        
        if not self.itens:
            return False

        """
        Caso haja itens relacionados ao pedido, chama-se os métodos self.calcula_valor_total() e self.prepara_detalhes_pedido(), para depois buscar o retorno do atributo self.detalhes_pedido.
        """
        self.calcula_valor_total()
        self.prepara_detalhes_pedido()

        return self.detalhes_pedido

    """
    O método a seguir calcula o valor total do pedido.
    """
    def calcula_valor_total(self):
        for item in self.itens:
            self.valor_total += item.produto.preco * item.quantidade

    """
    O método a seguir preenche os valores para cada chave do dicionário do atributo self.detalhes_pedido.
    """
    def prepara_detalhes_pedido(self):
        for item in self.itens:
            self.detalhes_pedido['itens'].append(
                {
                    'id_item': item.id,
                    'produto': item.produto.nome,
                    'quantidade': item.quantidade,
                    'preco_unidade': item.produto.preco,
                }
            )
        self.detalhes_pedido['pedido'] = {
                'id': self.pedido.id,
                'descricao': self.pedido.descricao,
                'criado_em': self.pedido.criado_em,
                'atualizado_em': self.pedido.atualizado_em,
                'cliente': self.pedido.cliente.cpf,
            }
        self.detalhes_pedido['total'] = self.valor_total
        
