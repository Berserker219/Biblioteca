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
    devuelto = models.BooleanField(default=False)

    objects = PrestamoManager()


    # directamente en el modelo, lo sobreescribimos, para cuando no tenemos admnistrador de usuario y no creemos una interfaz
    """
    def save(self, *args, **kwargs):
        self.libro.stok = self.libro.stok - 1
        self.libro.save()
        super(Prestamo, self).save(*args, **kwargs)
    """
    def __str__(self):
        return str(self.id) + '-' +self.libro.titulo