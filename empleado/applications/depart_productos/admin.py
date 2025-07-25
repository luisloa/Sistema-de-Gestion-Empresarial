from django.contrib import admin
from .models import DepartamentoProductos

# Register your models here.

@admin.register(DepartamentoProductos)
class DepartamentoProductos(admin.ModelAdmin):
    list_display = (
        'name',
        'budget',
        'description'
    )

    search_fields = ('id', 'name',)