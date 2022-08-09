from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponseRedirect
import json
from .utils import cookieCart, cartData, guestOrder
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


#import para generic da view
from  django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def loja(request):

    data = cartData(request)
    itemsCarrinho = data['itemsCarrinho']

        
    produtos = Produto.objects.all()

    context = {'produtos': produtos, 'itemsCarrinho': itemsCarrinho}
    return render(request, 'loja/loja.html', context)


def view (request, id):
    data = cartData(request)
    itemsCarrinho = data['itemsCarrinho']

        
    produto = Produto.objects.get(id = id)
    print(produto)
   

    context = {'produto': produto, 'itemsCarrinho': itemsCarrinho}
    return render(request, 'loja/view.html', context)


def cart(request):

    data = cartData(request)
    items = data['items']
    pedido = data['pedido']
    itemsCarrinho = data['itemsCarrinho']
    
    context = {'items': items, 'pedido': pedido, 'itemsCarrinho': itemsCarrinho}
    return render(request, 'loja/cart.html', context)

     
def checkout(request):

    data = cartData(request)
    items = data['items']
    pedido = data['pedido']
    itemsCarrinho = data['itemsCarrinho']


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

    else:
        cliente, pedido = guestOrder(request, data)

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
  
    return JsonResponse('Pedido processado com sucesso!', safe=False)

#Views da Dashboard

def dashboard(request):
    return render(request, 'loja/dashboard.html')
    



#Produtos
class ProdutoCreate(CreateView):
    model  = Produto
    queryset = Produto.objects.all()
    success_url = reverse_lazy('listProduto')


class ProdutoList(ListView):
    model = Produto
    queryset = Produto.objects.all()
    ordering = ['id']
    paginate_by = 10


class ProdutoUpdate(UpdateView):
    model = Produto
    fields = "__all__"
    success_url = reverse_lazy('listProduto')


class ProdutoDelete(DeleteView):
    model = Produto
    queryset = Produto.objects.all()
    success_url = reverse_lazy('listProduto')




#CRUD de Clientes

class ClienteCreate(CreateView):
    model = Cliente
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('listCliente')


class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    ordering = ['id']
    paginate_by = 10


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = "__all__"
    success_url = reverse_lazy('listCliente')


class ClienteDelete(DeleteView):
    model = Cliente
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('listCliente')



