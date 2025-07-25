from django.contrib import admin

# Register your models here.
from .models import Producto

@admin.register(Producto)
class Producto(admin.ModelAdmin):
    list_display=(
       'id',
       'sku',
       'name',
       'cost',
       'expiration_date',
       'proveedor',
       'departamento', 
    )

    search_fields = ('id', 'sku', 'name',)