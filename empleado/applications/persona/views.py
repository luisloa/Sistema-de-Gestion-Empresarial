from django import forms
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
    )
from .models import (
    Empleado, 
    Habilidades,
    )



# Requerimientos
# 1. Listar todos los empleados de la empresa
# 2. Listar todos los empleados que pertenecen a un area de la empresa
# 3. Listar empleados por trabajo
# 4. Listar los empleados por palabra clave
# 5. Listar habilidades de un empleado


class InicioView(TemplateView):
    '''Vista que carga la pagina de inicio'''
    template_name = "inicio/inicio.html"


class ListarTodosEmpleados(ListView):
    template_name = 'persona/listar_todos_empleados.html'
    model = Empleado
    paginate_by = 30
    ordering = 'first_name'
    context_object_name = 'lista_todos_empleados'

    def get_queryset(self):
        valor = self.request.GET.get("kword", '').strip()
        if valor:
            print('*********', valor)
            return Empleado.objects.filter(
                Q(first_name__icontains = valor) |
                Q(last_name__icontains = valor) |
                Q(id__icontains = valor)
            )
        return Empleado.objects.all()
    
    
class ListarPorArea(ListView):
    '''Lista Empleados Por Area'''
    template_name = 'persona/listar_por_departamento.html'
    
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__name = area
        )
        return lista
    
class ListarPorTrabajo(ListView):
    '''Lista Empleados Por Trabajo'''
    template_name = 'persona/listar_por_trabajo.html'
    context_object_name = 'empleados'
    model = Empleado  # Se fija el modelo
    paginate_by = 5  # Paginacion max. 20
    ordering = 'name'
    
    def get_queryset(self):
        trabajo = self.request.GET.get("kword", '').strip()
        if trabajo:
            print('*********', trabajo)
            return Empleado.objects.filter(job__icontains = trabajo)
        return Empleado.objects.none()
    
class ListarHabilidadesEmpleado(ListView):
    """ Lista de Habilidades de un Empleado"""
    template_name = 'persona/listar_persona_habilidades.html'
    context_object_name = 'listar_habilidades_persona'
    model = Empleado
    
    def get_queryset(self):
        empleado = self.request.GET.get('kword', '').strip()
        if empleado:
            print(f'******** {empleado}')
            return Empleado.objects.filter(first_name__icontains = empleado).prefetch_related('habilidades')
        return Empleado.objects.none()

class MODEL_NAMEDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    context_object_name = 'detalles'
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class EmpleadoCreateView(CreateView):
    model = Empleado 
    template_name = "persona/add_empleado.html" # Indica el template que debe ser ejecutado al enlazar con la url
    fields = ('__all__') # Aqui se muestran en nuestra vista todos los campos del modelo Empleado
    success_url = reverse_lazy('persona_app:add-empleado')
    
    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = f'{empleado.first_name} {empleado.last_name}'
        empleado.save()
        messages.success(self.request, f'Registro del empleado {empleado.full_name}, exitoso.')
        return super().form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update_empleado.html"
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:listar_empleados')
    
    

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete_empleado.html"
    context_object_name = 'empleado'
    success_url = reverse_lazy('persona_app:listar_empleados')

    
    

    
    
 
    
    

    
    
    
    
    

    



