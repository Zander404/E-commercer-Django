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

   ]
