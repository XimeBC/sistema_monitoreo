from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    boleta = models.CharField(max_length=200)
    nom_usuario = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)
