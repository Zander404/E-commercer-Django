from django.urls import path 
from . import views
from . import models 

urlpatterns = [

   
   path('', views.loja, name='loja'),
   path('cart/', views.cart, name='cart'),
   path('checkout/', views.checkout, name='checkout'),
   path('view/<int:id>', views.view, name='view'),


   path('update_item/', views.update_item, name='update_item'),
   path('process_pedido/', views.process_pedido, name='process_pedido'),



   # Caminhos para a dashboard de gerência
   path('dasboard/', views.dashboard, name='dasboard'),


   #Crud de Clientes 
   path("dasboard/cliente/listCliente/", views.ClienteList.as_view(), name="listCliente"),
   path("dasboard/cliente/createCliente/", views.ClienteCreate.as_view(), name="createCliente"),
   path("dasboard/cliente/updateCliente/<int:pk>/", views.ClienteUpdate.as_view(), name="updateCliente"),
   path("dasboard/cliente/deleteCliente/<int:pk>/", views.ClienteDelete.as_view(), name="deleteCliente"),


   #Crud Produtos 
   path("dasboard/produto/listProduto/", views.ProdutoList.as_view(), name="listProduto"),
   path("dasboard/produto/createProduto/", views.ProdutoCreate.as_view(), name="createProduto"),
   path("dasboard/produto/updateProduto/<int:pk>/", views.ProdutoUpdate.as_view(), name="updateProduto"),	
   path("dasboard/produto/deleteProduto/<int:pk>/", views.ProdutoDelete.as_view(), name="deleteProduto"),


   # # Crud Pedido 
   # path("dasboard/pedido/listPedido/")


   ]
