from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuarios, Qrs, Tipos_usuario, Control_usuarios


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


class AdmiForms(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = '__all__'

class UserForm(UserCreationForm):
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


class formControlUsuarios(forms.ModelForm):
    class Meta:
        model = Control_usuarios
        fields = ['user', 'temperatura' , 'oxigeno' , 'fecha_hora_registro']
        help_texts = {k:"" for k in fields}