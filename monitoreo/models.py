from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    boleta = models.CharField(max_length=200)
    nombre_usuario = models.CharField(max_length=200)
    clave = models.CharField(max_length=200 )
    fecha_nacimiento = models.DateField(max_length=200)
    def __str__(self):
        return '%s, %s, %s, %s, %s, %s' % (self.nombre, self.apellido, self.boleta, self.nombre_usuario, self.fecha_nacimiento, self.clave)
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
    fecha_hora_caducidad=models.CharField(max_length=200)
    codigo_barras= models.ImageField(upload_to='qr_codes', blank=True)
    def __str__(self):
        return str( self.fecha_hora_caducidad )
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.fecha_hora_caducidad)
        canvas = Image.new('RGB',(290,290),'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname=f'codigo_barras-{self.fecha_hora_caducidad}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.codigo_barras.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

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

