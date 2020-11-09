from django.db import models

# Create your models here.
class Equipo(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Titulo del Equipo")
    descripcion = models.TextField(verbose_name="Detalle del Equipo")
    imagen = models.URLField(max_length=200, verbose_name="URL de la imagen")
    estado = models.BooleanField(verbose_name="Disponible ?",default=False)
    ingresado = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de ingreso")
    prestamo = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de prestamo")

    def __str__(self):
        return self.titulo 
