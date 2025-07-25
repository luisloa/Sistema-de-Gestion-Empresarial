from django.shortcuts import render
from .models import(
    Producto,
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
    )

class ListarTodosProductos(ListView):
    model = Producto
    template_name = "producto/listar_todos_productos.html"
    ordering = 'name'
    context_object_name = 'obj_producto'



