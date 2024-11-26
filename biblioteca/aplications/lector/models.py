from django.db import models
# from local apps
from aplications.libro.models import Libro
from aplications.autor.models import Persona
# Managers
from .managers import PrestamoManager
# Create your models here.


class Lector(Persona):
    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'

class Prestamo(models.Model):
    lector = models.ForeignKey(Lector,on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True,null=True)
    edad = models.PositiveIntegerField(default=0)

    objects = PrestamoManager()

    def __str__(self):
        return self.libro.titulo