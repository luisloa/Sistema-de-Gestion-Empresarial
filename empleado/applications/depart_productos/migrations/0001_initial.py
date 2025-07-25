# Generated by Django 5.2.1 on 2025-07-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartamentoProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('budget', models.FloatField(verbose_name='Presupuesto')),
                ('description', models.TextField(max_length=500, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Departamento de productoa',
                'verbose_name_plural': 'Depatatamentos de productos',
            },
        ),
    ]
