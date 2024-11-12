from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(max_length=2000, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
