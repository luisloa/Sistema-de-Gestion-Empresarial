from django.db import models

from ckeditor.fields import RichTextField

from applications.departamento.models import Departamento

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField(("Habilidades"), max_length=50, unique=True)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
        ordering = ['habilidad']
        
    def __str__(self):
        return f'ID: {self.id}, {self.habilidad}'

class Empleado(models.Model):
    """ Modelo para tabla Empleado """
    
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Aadministrador'),
        ('2', 'Economista'),
        ('3', 'Desarrollador'),
        ('4', 'Jefe de turno'),
        ('5', 'Jefe de plaza'),
        ('6', 'Cajero'),
        ('7', 'Director de tramo'),
        ('8', 'Analista liquidador'),
        ('9', 'Monitorista'),
        ('10', 'Otro')
    )
    first_name = models.CharField("Nombre", max_length=30, null=False)
    last_name = models.CharField('Apellido', max_length=30, null=False)
    full_name = models.CharField('Nombre completo', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=2, null=False, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField('', upload_to='media/persona', blank= True, null= True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField('Hoja de vida', max_length=500)
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['first_name']
    
    def __str__(self):
        return f'{self.id}, {self.first_name} {self.last_name}, {self.departamento}'
