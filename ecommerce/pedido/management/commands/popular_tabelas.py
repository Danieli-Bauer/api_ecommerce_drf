from django.core.management import BaseCommand
from ecommerce.cliente.models import Cliente
from ecommerce.produto.models import Produto
from ecommerce.pedido.models import Pedido
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Cria instâncias dos modelos"

    def handle(self, *args, **options):
        logger.info("Criando três instâncias do modelo Cliente...")
        cliente1 = Cliente.objects.create(
            nome="Tiago Pereira da Silva",
            cpf="77632899707",
            telefone="21991029516",
            endereco="Rua Minho, 294, Várzea das Moças, Niterói/RJ",
            email="tiago.dasilva@nipbr.com"
        )
        cliente2 = Cliente.objects.create(
            nome="Barbara Silveira dos Santos",
            cpf="06458284080",
            telefone="51999021844",
            endereco="Rua Principal, 865, Quatro Distrito, Bonito/RS",
            email="barbara.silveira@patrilarm.com"
        )
        cliente3 = Cliente.objects.create(
            nome="Paulo das Neves",
            cpf="26102326679",
            telefone="34997847744",
            endereco="Rua Ursa, 807, Jardim Andrades, Patos de Minas/MG",
            email="paulo_santos@comp.net"
        )

        logger.info("Criando cinco instâncias do modelo Produto...")
        Produto.objects.create(
            nome="Bola Suíça Gym Ball 55cm",
            descricao="Cor: Cinza. Indicado para Yoga, Pilates, Abdominal. Bomba Grátis. Peso de suporte máximo recomendado: até 200kg.",
            preco=50.90,
            quantidade=458
        )
        Produto.objects.create(
            nome="Faixa Elastica Miniband",
            descricao="Colorido: azul, vermelho, amarelo. Elástico de Tensão Exercícios Fitness Yoga - 3 tensões: forte, medio, fraco",
            preco=25.49,
            quantidade=380
        )
        Produto.objects.create(
            nome="Meia Antiderrapante Unissex Par",
            descricao="Cor: Branco. Uso indicado para Pilates, Yoga ou hidroginástica.",
            preco=21.16,
            quantidade=549
        )
        Produto.objects.create(
            nome="Corda de Pular Rolamento Duplo",
            descricao="Cor: Preto. Comprimento: 3 metros. Comprimento da manopla: 14,5 cm. Material: Cabos de aço revestido de polímero especial de plástico e manoplas de plástico reforçado.",
            preco=49.99,
            quantidade=455
        )
        Produto.objects.create(
            nome="Colchonete Alta Densidade",
            descricao="Cor: Preto. Bivolt. Para academia e ginástica. Impermeável",
            preco=20.51,
            quantidade=1000
        )

        logger.info("Criando três instâncias do modelo Pedido...")
        Pedido.objects.create(
            cliente=cliente1,
            descricao="Compra de 2 bolas suíças"
        )

        Pedido.objects.create(
            cliente=cliente2,
            descricao="Compra de 1 colchonete e 2 cordas de pular"
        )

        Pedido.objects.create(
            cliente=cliente3,
            descricao="Compra de 1 par de meias antiderrapantes"
        )