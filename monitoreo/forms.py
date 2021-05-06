from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Usuarios, Qrs, Tipos_usuario, Control_usuarios, Restringidos


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Correo electronico')
    last_name = forms.CharField(label='Apellidos')
    first_name = forms.CharField(label='Nombres')
    boleta = forms.CharField(label='Boleta')
    username = forms.CharField(label='Nombre de usuario')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirma contraseña', widget=forms.PasswordInput)
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento (yyyy-mm-dd)',input_formats=["%Y-%m-%d"])
    curp = forms.CharField(label='CURP')
    opciones = [
        (1, 'Estudiante'),
        (2, 'Docente'),
        (3, 'Administrador'),
        (4, 'Invitado'),
    ]
    id_tipo = forms.ChoiceField(label="Tipo de Usuario", widget=forms.Select(), choices=opciones)

    class Meta:
        model = User
        fields = ['username' , 'password1' , 'password2' , 'first_name' , 'last_name', 'email', 'boleta', 'fecha_nacimiento', 'id_tipo', 'curp']
        help_texts = {k:"" for k in fields}

class AdmiForms(forms.ModelForm):
    email = forms.EmailField(label='Correo electronico')
    apellido = forms.CharField(label='Apellidos')
    nombre = forms.CharField(label='Nombre(s)')
    boleta = forms.CharField(label='Boleta')
    nombre_usuario = forms.CharField(label='Nombre de usuario')
    clave = forms.CharField(label='contraseña', widget=forms.PasswordInput,required=False)
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento (yyyy-mm-dd)',input_formats=["%Y-%m-%d"])
    curp = forms.CharField(label='CURP')
    opciones = [
        (1, 'Estudiante'),
        (2, 'Docente'),
        (3, 'Administrador'),
        (4, 'Invitado'),
    ]
    id_tipo = forms.ChoiceField(label="Tipo de Usuario", widget=forms.Select(), choices=opciones)
    estados = [
        (1, 'Activo'),
        (0, 'Inactivo'),
    ]
    estado = forms.ChoiceField(label="Estado", widget=forms.Select(), choices=estados)

    class Meta:
        model = Usuarios
        fields = ['nombre_usuario' , 'clave' , 'nombre' , 'apellido', 'email', 'boleta', 'fecha_nacimiento', 'id_tipo', 'estado','curp']
        help_texts = {k:"" for k in fields}

class formControlUsuarios(forms.ModelForm):
    temperatura = forms.CharField(max_length=200)
    oxigenacion = forms.CharField(max_length=200)
    nombre_usuario=forms.CharField(max_length=200,disabled=True)
    fecha_hora_registro = forms.DateField(label='Fecha de(yyyy-mm-dd)',input_formats=["%Y-%m-%d"])
    class Meta:
        model = Control_usuarios
        fields = [ 'nombre_usuario','temperatura' , 'oxigenacion' , 'fecha_hora_registro']
        help_texts = {k:"" for k in fields}

class formEstado(forms.ModelForm):
    nombre_usuario = forms.CharField(max_length=200,disabled=True)
    fecha_sintomas = forms.DateField(label='Fecha de(yyyy-mm-dd)',input_formats=["%Y-%m-%d"])
    casos = [
        (1, 'Sospechoso'),
        (2, 'Confirmado'),
        (3, 'Negativo'),
    ]
    estado_condicion = forms.ChoiceField(label="Estado", widget=forms.Select(), choices=casos)
    fecha_prueba = forms.DateField(label='Fecha de(yyyy-mm-dd)',input_formats=["%Y-%m-%d"])
    tipo_prueba = forms.CharField(max_length=200)
    class Meta:
        model = Restringidos
        fields = ['nombre_usuario','fecha_sintomas','estado_condicion','fecha_prueba','tipo_prueba']
        help_texts = {k:"" for k in fields}

