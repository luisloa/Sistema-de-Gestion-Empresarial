from django.contrib import admin
from .models import Proveedor

# Register your models here.

@admin.register(Proveedor)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'address', 
        'telephone_number',
        'email',
        'start_date'
    )
 
    search_fields=('name', 'id',)
