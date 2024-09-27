from django.db import models

# Create your models here.
class Task (models.Model):
    title = models.TextField(max_length=20, verbose_name='Titulo')
    description = models.TextField(max_length=100, verbose_name='Descripción')
    active=models.BooleanField(verbose_name= 'Activa',default=False, blank=True)
    class Meta:

        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"