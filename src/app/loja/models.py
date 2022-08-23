from distutils.command import upload
from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Produto(models.Model):
    nome = models.CharField(max_length=200, null=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=False)
    descricao = models.TextField(null=True, blank=True)
    image = models.ImageField("image", null=True, blank=True, upload_to='produtos')
   

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'produto'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    

    def __str__(self):
        return self.nome

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/static/img/placeholder.png'
        return url

    class Meta:
        db_table = 'produto'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
 
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    data_pedido = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transacao_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'pedido'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    @property
    def get_cart_total(self):
        itemspedidos = self.itempedido_set.all()
        total = sum([item.get_total for item in itemspedidos])
        return total

    @property
    def get_cart_items(self):
        itemspedidos = self.itempedido_set.all()
        total = sum([item.quantidade for item in itemspedidos])
        return total

    @property
    def envio(self):
        envio = False
        itemspedidos = self.itempedido_set.all()
        for i in itemspedidos:
            if i.produto.digital == False:
                envio = True
        return envio


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True, blank=True)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    data_adicionada = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.produto.preco * self.quantidade



class Endereco_de_Entrega(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True)
    cidade = models.CharField(max_length=200, null=True)
    estado = models.CharField(max_length=200, null=True)
    cep = models.CharField(max_length=200, null=True)
    data_adicionada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.endereco
        
    class Meta:
        db_table = 'endereco_de_entrega'
        verbose_name = 'Endereco de Entrega'
        verbose_name_plural = 'Enderecos de Entrega'
        ordering = ['cliente']
