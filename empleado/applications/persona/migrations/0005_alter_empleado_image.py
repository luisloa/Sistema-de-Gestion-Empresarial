# Generated by Django 5.2.1 on 2025-07-21 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_alter_empleado_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='persona', verbose_name=''),
        ),
    ]
