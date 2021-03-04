from django.forms import ModelForm
from .models import Usuarios

class RegistroUsuario(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre' , 'apellido' , 'boleta' , 'nombre_usuario', 'clave', 'fecha_nacimiento']
   