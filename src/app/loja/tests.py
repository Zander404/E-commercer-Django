from unicodedata import digit
from django.test import TestCase
from .models import *

# Create your tests here.

class ClienteTestCase(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome="Cliente 1",
            email="example@example.com"
        )
        
    def test_cliente(self):
        self.assertEqual(self.cliente.nome, "Cliente 1")
        self.assertEqual(self.cliente.email, "example#example.com")                   
        
class ProdutoTestCase(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(
            nome="Produto 1",
            preco=10.00,
            descricao="yes",
            digital = False
            
        )
        
    def test_produto(self):
        self.assertEqual(self.produto.nome, "Produto 1")
        self.assertEqual(self.produto.preco, 10.00)
        self.assertEqual(self.produto.descricao, "yes")
        self.assertEqual(self.produto.digital, False)
        
        
        
class PedidoTestCase(TestCase):
    def setUp(self):
        self.pedido = Pedido.objects.create(
            cliente=Cliente.objects.create(
                nome="Cliente 1",
                email="example@example.com"),
            
            produto=Produto.objects.create(
                nome="Produto 1",
                preco=10.00,
                descricao="yes",
                digital = False),

            quantidade=1,
            preco=10.00,
            status="Aguardando Pagamento",
            endereco="Rua 1",
            cidade="Cidade 1",
            estado="Estado 1",
            cep="12345678",
            digital=False,
            pedido_id="1234567890",
        )
            
    def test_pedido(self):
        self.assertEqual(self.pedido.cliente.nome, "Cliente 1")
        self.assertEqual(self.pedido.cliente.email, "example@example.com")
        self.assertEqual(self.pedido.produto.nome, "Produto 1")
        self.assertEqual(self.pedido.produto.preco, 10.00)
        self.assertEqual(self.pedido.produto.descricao, "yes")
        self.assertEqual(self.pedido.produto.digital, False)
        self.assertEqual(self.pedido.quantidade, 1)
        self.assertEqual(self.pedido.preco, 10.00)
        self.assertEqual(self.pedido.status, "Aguardando Pagamento")
        self.assertEqual(self.pedido.endereco, "Rua 1")
        self.assertEqual(self.pedido.cidade, "Cidade 1")
        self.assertEqual(self.pedido.estado, "Estado 1")
        self.assertEqual(self.pedido.cep, "12345678")
        self.assertEqual(self.pedido.digital, False)
        self.assertEqual(self.pedido.pedido_id, "1234567890")
        
        