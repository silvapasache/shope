from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from .models import Cliente
from .form import ClienteForm
# Create your views here.


class ClienteListView(ListView):
    template_name = "cliente/list.html"
    model = Cliente
    context_object_name="Clientes"
    ordering=("id",)


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "cliente/add.html"
    form_class=ClienteForm
    success_url=reverse_lazy('cliente_app:list_cliente')



