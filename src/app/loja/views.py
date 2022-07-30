from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json 
import datetime

# Create your views here.

def loja(request):

    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, complete=False)
        items = pedido.itempedido_set.all()
        itemsCarrinho = pedido.get_cart_items

    else:
        items = []
        pedido = {"get_cart_total": 0, "get_cart_items": 0, 'envio': False}
        itemsCarrinho = pedido['get_cart_items']

    produtos = Produto.objects.all()
    context = {'produtos': produtos, 'itemsCarrinho': itemsCarrinho}
    return render(request, 'loja/loja.html', context)


def cart(request):

    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, complete=False)
        items = pedido.itempedido_set.all()
        itemsCarrinho = pedido.get_cart_items
    else:
        items = []
        pedido = {"get_cart_total": 0, "get_cart_items": 0, 'envio': False}
        itemsCarrinho = pedido['get_cart_items']
    
    context = {'items': items, 'pedido': pedido, 'itemsCarrinho': itemsCarrinho}
    return render(request, 'loja/cart.html', context)

     
def checkout(request):

    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, complete=False)
        items = pedido.itempedido_set.all()
        itemsCarrinho = pedido.get_cart_items

    else:
        items = []
        pedido = {"get_cart_total": 0, "get_cart_items": 0, 'envio': False}
        itemsCarrinho = pedido['get_cart_items']

    context = {'items': items, 'pedido': pedido, 'itemsCarrinho': itemsCarrinho}
    return render(request, 'loja/checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    produtoId = data['produtoId']
    action = data['action']

    print("ProdutoId:", produtoId)
    print('Action:', action)

    cliente = request.user.cliente
    produto = Produto.objects.get(id=produtoId)
    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, complete=False)
    pedidoItem, criado = ItemPedido.objects.get_or_create(pedido=pedido, produto=produto)


    if action == 'add':
        pedidoItem.quantidade = (pedidoItem.quantidade + 1)
        
    elif action == 'remove':
        pedidoItem.quantidade = (pedidoItem.quantidade - 1)

    pedidoItem.save()

    if pedidoItem.quantidade <= 0:
        pedidoItem.delete()


    return JsonResponse('Item atualizado com sucesso!', safe=False)


def process_pedido(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, complete=False)
        total = float(data['form']['total'])
        pedido.transaction_id = transaction_id

        if total == pedido.get_cart_total:
            pedido.complete = True
        pedido.save()

        if pedido.envio == True:
            Endereco_de_Entrega.objects.create(
                cliente=cliente,
                pedido=pedido,
                endereco=data['envio']['endereco'],
                cidade=data['envio']['cidade'],
                estado=data['envio']['estado'],
                cep=data['envio']['cep'],
                )

    else:
        print('Usuário não está logado')
    return JsonResponse('Pedido processado com sucesso!', safe=False)