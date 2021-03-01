from django.db import models

class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    boleta = models.CharField(max_length=200)
    nombre_usuario = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(max_length=200)

class Control_usuarios(models.Model):
    temperatura = models.CharField(max_length=200)
    oxigeno = models.CharField(max_length=200)
    fecha_hora_registro = models.CharField(max_length=200)
    def __str__(self):
        return '%s, %s' % (self.oxigeno, self.temperatura)

class Historial_ubicaciones(models.Model):
    fecha_hora_entrada = models.CharField(max_length=200)
    def __str__(self):
        return '%s, %s' % (self.fecha_hora_entrada)

class Qrs(models.Model):
    codigo_barras = models.ImageField(upload_to='barcodes/', blank=True)
    fecha_hora_caducidad = models.CharField(max_length=200)
    def __str__(self):
        return '%s, %s' % (self.codigo_barras, self.fecha_hora_caducidad)

class Tipos_usuario(models.Model):
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    def __str__(self):
        return '%s, %s' % (self.descripcion, self.estado)

class Salones(models.Model):
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    def __str__(self):
        return '%s, %s' % (self.descripcion, self.estado)

