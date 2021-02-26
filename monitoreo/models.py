from django.urls import reverse #Used to generate URLs by reversing the URL patterns
class Codigo(models.Model):
    """
    Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.).
    """
    cod_usuario = models.CharField(max_length=200, help_text="Leer codigo")
    cod_salon = models.CharField(max_length=200, help_text="Leer codigo")
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return '%s, %s' % (self.cod_usuario, self.cod_salon)

class Tipo(models.Model):
    """
    Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.).
    """
    admi = models.CharField(max_length=200, help_text="tipo")
    est = models.CharField(max_length=200, help_text="tipo")
    maes = models.CharField(max_length=200, help_text="tipo")
    
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return '%s, %s, %s' % (self.admi, self.est, self.maes)

class Salones(models.Model):
    """
    Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.).
    """
    nom_salon = models.CharField(max_length=200, help_text="Leer codigo")
    cod_salo = models.ForeignKey('cod_salon', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return '%s, %s' % (self.nom_salon, self.cod_salo)
class Historico(models.Model):
    """
    Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.).
    """
    nom_salon = models.ForeignKey('cod_salon', on_delete=models.SET_NULL, null=True)
    nom_usu = models.ForeignKey('cod_usuario', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return '%s, %s, %s' % (self.nom_salon, self.cod_salo, self.date)

class Usuario(models.Model):
    """
    Modelo que representa un usuario 
    """

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)

    codigo = models.ForeignKey('cod_usuario', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
    # 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.
    boleta = models.CharField(max_length=200)
    nom_usuario = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    tipo_us=models.ManyToManyField(Tipo, help_text="Seleccione el tipo de usuario que eres.")
    date_of_birth = models.DateField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        """
        String que representa al objeto Book
        """
        return '%s, %s' % (self.cod_usuario, self.tipo_us)

class Monitoreo(models.Model):
    """
    Modelo que representa un usuario 
    """
    codigo_usu = models.CharField(max_length=200)
    codigo = models.ForeignKey('cod_usuario', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
    # 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.
    temperatura = models.CharField(max_length=200)
    oxigenacion = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    def __str__(self):
        """
        String que representa al objeto Book
        """
        return '%s, %s' % (self.cod_usuario, self.tipo_us)
        