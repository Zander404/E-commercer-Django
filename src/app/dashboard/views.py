from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from loja.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from . import decorators

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard/index.html')
    
#Produtos

class ProdutoList(ListView):
    model = Produto
    template_name = 'dashboard/produto/list.html'
    login_url = 'login'
    raise_exceptions = True

class ProdutoCreate(CreateView, GroupRequiredMixin):
    model = Produto
    template_name = 'dashboard/produto_form.html'
    login_url = 'login'
    raise_exceptions = True
    group_required = [u'Administrador']
    fields = ['nome', 'preco', 'digital', 'image', 'descricao']
    success_url = reverse_lazy('listProduto')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['botao'] = 'Cadastrar'
        return context


class ProdutoList(ListView, GroupRequiredMixin ):
    group_required = [u"Administrador"]
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
    group_required = [u"Gerente"]


class ClienteList(ListView, LoginRequiredMixin, ):
    model = Cliente
    queryset = Cliente.objects.all()
    ordering = ['id']
    paginate_by = 10
    template_name = 'dashboard/cliente_list.html'


class ClienteUpdate(UpdateView, LoginRequiredMixin ):
    group_required = [u"gerente"]
    model = Cliente
    fields = "__all__"
    success_url = reverse_lazy('listCliente')
    template_name = 'dashboard/cliente_form.html'
  


class ClienteDelete(DeleteView, LoginRequiredMixin, ):
    model = Cliente
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('listCliente')
    template_name = 'dashboard/cliente_confirm_delete.html'
    group_required = [u"gerente"]


#Crud de Pedidos
class PedidoCreate(CreateView, LoginRequiredMixin):
    login_url: reverse_lazy('login')
    model = Pedido
    fields = "__all__"
    queryset = Pedido.objects.all()
    success_url = reverse_lazy('listPedido')
    template_name = 'dashboard/pedido_form.html'
    group_required = [u"gerente"]

class PedidoList(ListView, LoginRequiredMixin):
    model = Pedido
    queryset = Pedido.objects.all()
    ordering =['id']
    paginated_by = 10
    template_name = 'dashboard/pedido_list.html'
    group_required = [u"gerente"]

class PedidoUpdate(UpdateView, LoginRequiredMixin):
    model = Pedido
    fields = '__all__'
    success_url = reverse_lazy('listPedido')
    template_name = 'dashboard/pedido_form.html'
    group_required = [u"gerente"]


class PedidoDelete(DeleteView, LoginRequiredMixin):
    model = Pedido
    queryset = Pedido.objects.all()
    success_url = reverse_lazy('listPedido')
    template_name = 'dashboard/pedido_confirm_delete.html'
    group_required = [u"gerente"]





