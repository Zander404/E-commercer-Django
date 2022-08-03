var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var produtoId = this.dataset.produto
        var action = this.dataset.action
        console.log('produtoId:', produtoId, 'action:', action)

        console.log('USER:', user)
        if (user == 'AnonymousUser') {
            adicionarCookieItem( produtoId, action)
            } else {
                updatePedidoUsuario(produtoId, action)
            }
        }) 

}

function adicionarCookieItem(produtoId, action){
    console.log('Usuario não logado, adicionando item no cookie')
    if (action == 'add') {
        if (cart[produtoId] == undefined) {
            cart[produtoId] = {'quantidade': 1}
        } else {
            cart[produtoId]['quantidade'] += 1
        }
    }

    if (action == 'remove') {
        cart[produtoId]['quantidade'] -= 1
        if (cart[produtoId]['quantidade'] <= 0) {
            console.log("Removendo produto do carrinho")
            delete cart[produtoId]
        }
    }
    console.log('Cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function updatePedidoUsuario(produtoId, action){
    console.log('Usuario logado, atualizando pedido')

    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'produtoId': produtoId,
            'action': action
        })
    }).then(response =>
        response.json()
    ).then(data => {
        console.log('data:', data);
        location.reload()
    })

}
