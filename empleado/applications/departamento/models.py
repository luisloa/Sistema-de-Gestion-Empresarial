from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, unique=True)
    shor_name = models.CharField('Nombre corto', max_length=15, blank=True , null=True) # Blank indica que se puede deja el registro en blanco
                                                                                        # Null 
    anulate = models.BooleanField('Anulado', default=False)
    
    class Meta: 
        verbose_name = 'Area'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        unique_together = ('name', 'shor_name')
    
    def __str__(self):
        return f'{self.id}, {self.name}'