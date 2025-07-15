from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import (
    FormView
)
from .forms import NewDepartForm
from django import forms
from ..persona.models import Empleado
from .models import Departamento

# Create your views here.
class NewDepartView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartForm
    success_url = '/'
    
    
    
    def form_valid(self, form):
        
        departamento = Departamento(
            name = form.cleaned_data.get('dpto'),
            shor_name = form.cleaned_data.get('short_dpto')
        )
        departamento.save()
        
        
        nombre = form.cleaned_data.get('first_name')
        apellido = form.cleaned_data.get('last_name')
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job='1',
            departamento= departamento
        )
        return super(NewDepartView, self).form_valid(form)