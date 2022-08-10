from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from loja.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard/index.html')
    
#Produtos

class ProdutoCreate(CreateView, LoginRequiredMixin, GroupRequiredMixin ):
    login_url: reverse_lazy('login')
    group_required = u"Administrador"
    model  = Produto
    fields = "__all__"
    template_name = 'dashboard/produto_form.html'
    success_url = reverse_lazy('listProduto')
    


class ProdutoList(ListView, LoginRequiredMixin, ):
    model = Produto
    queryset = Produto.objects.all()
    ordering = ['id']
    paginate_by = 10
    template_name = 'dashboard/produto_list.html'


class ProdutoUpdate(UpdateView, LoginRequiredMixin):
    model = Produto
    fields = "__all__"
    success_url = reverse_lazy('listProduto')
    template_name = 'dashboard/produto_form.html'


class ProdutoDelete(DeleteView, LoginRequiredMixin):
    model = Produto
    queryset = Produto.objects.all()
    success_url = reverse_lazy('listProduto')
    template_name = 'dashboard/produto_confirm_delete.html'
    

#CRUD de Clientes

class ClienteCreate(CreateView, LoginRequiredMixin):
    login_url: reverse_lazy('login')
    model = Cliente
    fields = "__all__"
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('listCliente')
    template_name = 'dashboard/cliente_form.html'
    group_required = [u"Administrador"]


class ClienteList(ListView, LoginRequiredMixin, ):
    model = Cliente
    queryset = Cliente.objects.all()
    ordering = ['id']
    paginate_by = 10
    template_name = 'dashboard/cliente_list.html'


class ClienteUpdate(UpdateView, LoginRequiredMixin, ):
    model = Cliente
    fields = "__all__"
    success_url = reverse_lazy('listCliente')
    template_name = 'dashboard/cliente_form.html'
    group_required = [u"gerente"]


class ClienteDelete(DeleteView, LoginRequiredMixin, ):
    model = Cliente
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('listCliente')
    template_name = 'dashboard/cliente_confirm_delete.html'
    group_required = [u"gerente"]

