from django.db import models

# Create your models here.

class Proveedor(models.Model):
    '''Modelo para la tabla proveedor'''

    name = models.CharField(("Nombre"), max_length=50, null=False)
    address = models.CharField(("Dirección"), max_length=300, null=False)
    telephone_number = models.CharField(("Numero telefonico"), max_length=10, null=False)
    email = models.CharField(("Email"), max_length=50)
    start_date = models.DateField(("Fecha de inicio"), auto_now=False, auto_now_add=False)
    description = models.TextField(("Descripcion"), max_length=500, null=True)
    

    class Meta:
        verbose_name = ("Proveedor")
        verbose_name_plural = ("Proveedores")

    def __str__(self):
        return self.name

    
