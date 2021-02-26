from django.db import models

class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    boleta = models.CharField(max_length=200)
    nombre_usuario = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s, %s' % (self.nombre, self.apellido)
