var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var produtoId = this.dataset.produto
        var action = this.dataset.action
        console.log('produtoId:', produtoId, 'action:', action)

        console.log('USER:', user)
        if (user == 'AnonymousUser') {
            console.log('Não está logado')
            alert('Faça login para adicionar produtos ao carrinho')
            } else {
                updatePedidoUsuario(produtoId, action)
            }
        }) 

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
