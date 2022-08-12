from django.urls import path
from . import views
from django.contrib.auth import authenticate




urlpatterns = [
   # Caminhos para a dashboard de gerência
   path('dasboard/', views.dashboard, name='dasboard'),


   #Crud de Clientes
   path("cliente/listCliente/", views.ClienteList.as_view(), name="listCliente"),
   path("cliente/createCliente/", views.ClienteCreate.as_view(), name="createCliente"),
   path("cliente/updateCliente/<int:pk>/", views.ClienteUpdate.as_view(), name="updateCliente"),
   path("cliente/deleteCliente/<int:pk>/", views.ClienteDelete.as_view(), name="deleteCliente"),


   #Crud Produtos 
   path("produto/listProduto/", views.ProdutoList.as_view(), name="listProduto"),
   path("produto/createProduto/", views.ProdutoCreate.as_view(), name="createProduto"),
   path("produto/updateProduto/<int:pk>/", views.ProdutoUpdate.as_view(), name="updateProduto"),	
   path("produto/deleteProduto/<int:pk>/", views.ProdutoDelete.as_view(), name="deleteProduto"),
]