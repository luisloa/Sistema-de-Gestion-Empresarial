from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from applications.proveedor.models import Proveedor
from applications.depart_productos.models import DepartamentoProductos

class Producto(models.Model):
    '''Modulo pata tabla Producto'''

    sku = models.CharField('SKU', max_length=20, null=False)
    name = models.CharField(("Nombre"), max_length=50, null=False)
    cost = models.FloatField(("Precio"), null=False)
    expiration_date = models.DateField(("Fecha de caducidad"), auto_now=False, auto_now_add=False)
    description = models.TextField(("Descripcion"), max_length=500, null=True)
    
    proveedor = models.ForeignKey(Proveedor, verbose_name=_("Proveedor"), on_delete=models.CASCADE)
    departamento = models.ForeignKey(DepartamentoProductos, verbose_name=_("Departamento productos"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.name

    
