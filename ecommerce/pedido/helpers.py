from .models import Pedido, Item

class PedidoHelper:

    def __init__(self, pedido):
        self.pedido = pedido
        self.valor_total = 0
        self.itens = []
        self.detalhes_pedido = {'informacoes': [], 'itens': [], 'total': 0}

    def verifica_pedido(self):
        self.itens = Pedido.objects.filter(pedido=self.pedido)
        
        if not self.itens:
            return False
        
        self.calcula_valor_total()
        self.prepara_detalhes_pedido()

        return self.detalhes_pedido

    def calcula_valor_total(self):
        for item in self.itens:
            self.valor_total += item.produto.preco * item.quantidade

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
        self.detalhes_pedido['informacoes'].append(
            {
                'pedido': self.pedido.id,
                'cliente': self.pedido.cliente.nome,
                'descricao': self.pedido.descricao,
                'criado_em': self.pedido.criado_em
            }
        )
        self.detalhes_pedido['total'] = self.valor_total
        
