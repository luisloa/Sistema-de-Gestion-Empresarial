from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba_DB
from .forms import PruebaForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html' # Le indica donde se va a mostrar las informacion
    queryset = ['Luis', 'Enrique', 'Jimenez', 'Loa', 'Hola']
    context_object_name = 'lista_prueba'
    
class ModeloPruebaListView(ListView):
    model = Prueba_DB
    template_name = 'home/lista.html'
    context_object_name = 'data_base'
    

class PruebaCreateView(CreateView):
    model = Prueba_DB
    template_name = "home/prueba.html"
    form_class = PruebaForm
    success_url = '/'
    
    
    

    
