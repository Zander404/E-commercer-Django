import json
from .models import *

def cookieCart(request):
        try: 
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        print('Carrinho:', cart)
        items = []
        pedido = {"get_cart_total": 0, "get_cart_items": 0, 'envio': False}
        itemsCarrinho = pedido['get_cart_items']

        for i in cart:
            try:
                itemsCarrinho += cart[i]['quantidade']
                produto = Produto.objects.get(id=i)
                total = (produto.preco * cart[i]['quantidade'])
                pedido['get_cart_total'] += total
                pedido['get_cart_items'] += cart[i]['quantidade']

                item = {
                        'produto':{
                            'id': produto.id,
                            'nome': produto.nome,
                            'preco': produto.preco,
                            'imageURL': produto.imageURL,
                            'digital': produto.digital,
                        },
                        'quantidade': cart[i]['quantidade'],
                        'get_total': total,
                }
                items.append(item)

                if produto.digital == False:
                    pedido['envio'] = True
            except:
                pass
        return {'pedido': pedido, 'items': items, 'itemsCarrinho': itemsCarrinho}


def cartData(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, complete=False)
        items = pedido.itempedido_set.all()
        itemsCarrinho = pedido.get_cart_items
    else:
        cookieData = cookieCart(request)
        items = cookieData['items']
        pedido = cookieData['pedido']
        itemsCarrinho = cookieData['itemsCarrinho']

    return {'items': items, 'pedido': pedido, 'itemsCarrinho': itemsCarrinho}


def guestOrder(request, data):
    print('User is not logged in')
    print("COOKIES:", request.COOKIES)
    nome = data['form']['nome']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    cliente, criado = Cliente.objects.get_or_create(email=email)
    cliente.nome = nome
    cliente.save()

    pedido = Pedido.objects.create(cliente=cliente, complete=False)

    for item in items:
        produto = Produto.objects.get(id=item['produto']['id'])
        itemPedido = ItemPedido.objects.create(pedido=pedido, produto=produto, quantidade=item['quantidade'])

    return cliente, pedido


