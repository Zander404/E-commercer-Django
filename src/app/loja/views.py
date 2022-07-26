from django.shortcuts import render
from .models import *

# Create your views here.

def loja(request):
    context = {'produtos': Produto.objects.all()}
    return render(request, 'loja/loja.html', context)

def cart(request):

    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, complete=False)
        items = pedido.itempedido_set.all()
    else:
        items = []
        pedido = {"get_cart_total": 0, "get_cart_items": 0}
    context = {'items': items, 'pedido': pedido}
    return render(request, 'loja/cart.html', context)
     
def checkout(request):

    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, complete=False)
        items = pedido.itempedido_set.all()
    else:
        items = []
        pedido = {"get_cart_total": 0, "get_cart_items": 0}
    context = {'items': items, 'pedido': pedido}
    return render(request, 'loja/checkout.html', context)