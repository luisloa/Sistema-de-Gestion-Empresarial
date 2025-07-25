from django.db import models

# Create your models here.
class DepartamentoProductos(models.Model):
    '''Modelos para la tabla Departamento Producto'''

    name = models.CharField(("Nombre"), max_length=50, null=False)
    budget = models.FloatField(("Presupuesto"))
    description = models.TextField(("Descripcion"), max_length=500, null=True)

    class Meta:
        verbose_name = ("Departamento de productoa")
        verbose_name_plural = ("Depatatamentos de productos")

    def __str__(self):
        return f'{self.id} - {self.name}'

    
