from django.db import models

# Create your models here.
class Prueba_DB(models.Model):
    titulo = models.CharField( max_length=30)
    subtitulo = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f'{self.titulo} {self.subtitulo}'

    

