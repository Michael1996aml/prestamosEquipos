from django.db import models

# Create your models here.
class Equipo(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Titulo del Equipo")
    descripcion = models.TextField(verbose_name="Detalle del Equipo")
    imagen = models.URLField(max_length=200, verbose_name="URL de la imagen")
    estado = models.BooleanField(verbose_name="Disponible ?",default=False)
    ingresado = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de ingreso")

    def __str__(self):
        return self.titulo 

class Prestamos(models.Model):
    Nombre = models.CharField(max_length=70,verbose_name="Nombre Completo")
    Equipoo = models.ForeignKey(Equipo, null=False, blank=False, on_delete=models.CASCADE)
    Fechae = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de entrega")
    fechad = models.DateField(verbose_name="Decha de Devolucion")
    OperadorE = models.CharField(max_length=70,verbose_name="Operador Que Entrega")
    OperadorR = models.CharField(max_length=70,verbose_name="Operador Que Recibe")
    Observaciones = models.TextField(verbose_name="Observacion Del Equipo")
    tipos = [
        ('E','Estudiante'),
        ('P','Profesor')
    ]
    tipo = models.CharField(max_length=1,choices=tipos,default='E')

    def __str__(self):
        return self.Nombre

