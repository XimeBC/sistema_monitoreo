from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuarios, Control_usuarios, Historial_ubicaciones, Qrs,Tipos_usuario


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField()
    first_name = forms.CharField()
    boleta = forms.CharField()
    username = forms.CharField()
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirma contraseña', widget=forms.PasswordInput)
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento (yyyy-mm-dd)',input_formats=["%Y-%m-%d"])
    opciones = [
        (1, 'Estudiante'),
        (2, 'Docente'),
        (3, 'Administrador'),
        (4, 'Invitado'),
    ]
    id_tipo = forms.ChoiceField(label="Tipo de Usuario", widget=forms.Select(), choices=opciones)

    class Meta:
        model = User
        fields = ['username' , 'password1' , 'password2' , 'first_name' , 'last_name', 'email', 'boleta', 'fecha_nacimiento', 'id_tipo']
        help_texts = {k:"" for k in fields}

