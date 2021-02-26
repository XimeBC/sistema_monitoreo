from django.db import models

class Qrs(models.Model):
    cod_usuario = models.CharField(max_length=200, help_text="Leer codigo")
    cod_salon = models.CharField(max_length=200, help_text="Leer codigo")
    def create(cod_usuario, cod_salon):
       return cod_usuario, cod_salon

class Tipos_usuarios(models.Model):
    tipo = models.CharField(max_length=200, help_text="tipo")
    def create(tipo):
        return tipo

class Salones(models.Model):
    nom_salone = models.CharField(max_length=200, help_text="Leer codigo")
    cod_salones = models.ForeignKey('cod_salon', on_delete=models.SET_NULL, null=True)
    def create(nom_salone, cod_salones):
        return nom_salone, cod_salones

class Historico_ubicaciones(models.Model):
    nom_sal = models.ForeignKey('cod_salones', on_delete=models.SET_NULL, null=True)
    nom_usua = models.ForeignKey('codigo', on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(auto_now=True)
    def create(nom_salon, nom_usuario):
        return nom_sal, nom_usua

class Usuario(models.Model):
    
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    codigo = models.ForeignKey('cod_usuario', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
    # 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.
    boleta = models.CharField(max_length=200)
    nom_usuario = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    tipo_us = models.ForeignKey('tipo', on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(auto_now_add=True)
    def create(nombre, apellido, codigo, boleta, nom_usuario, password, tipo_us, fecha):
        return nombre, apellido,codigo, boleta, nom_usuario, password, tipo_us, fecha

class Monitoreo_usuarios(models.Model):
    nom_usuario =  models.ForeignKey('nom_usuario', on_delete=models.SET_NULL, null=True)
    codi = models.ForeignKey('codigo', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
    # 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.
    temperatura = models.CharField(max_length=200)
    oxigenacion = models.CharField(max_length=200)
   # fecha = models.DateField(auto_now=True)
    def create(nom_usuario, codi, temperatura, oxigenacion):
        return nom_usuario, codi, temperatura, oxigenacion
        