from django.contrib import admin

from .models import Departamento

# Register your models here.

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'shor_name'
    )
    search_fields = ('name',) 
admin.site.register(Departamento, DepartamentoAdmin)


