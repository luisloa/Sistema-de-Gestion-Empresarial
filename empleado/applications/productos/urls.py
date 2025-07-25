from django.urls import path
from . import views

app_name = 'producto_app'

urlpatterns = [
    path('listar_todos_productos/', 
         views.ListarTodosProductos.as_view(), 
         name='listar_todos_productos'),
]
