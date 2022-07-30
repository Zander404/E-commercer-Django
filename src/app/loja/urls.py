from django.urls import path 
from . import views

urlpatterns = [
   path('', views.loja, name='loja'),
   path('cart/', views.cart, name='cart'),
   path('checkout/', views.checkout, name='checkout'),

   path('update_item/', views.update_item, name='update_item'),
   path('process_pedido/', views.process_pedido, name='process_pedido'),
   ]
