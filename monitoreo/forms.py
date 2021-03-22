from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField()
    first_name = forms.CharField()
    boleta = forms.CharField()
    username = forms.CharField()
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirma contraseña', widget=forms.PasswordInput)
    fecha_nacimiento = forms.DateField(label='yyyy/mm/dd',input_formats=["%Y-%m-%d"])
    class Meta:
        model = User
        fields = ['username' , 'password1' , 'password2' , 'first_name' , 'last_name', 'email', 'boleta', 'fecha_nacimiento']
        help_texts = {k:"" for k in fields}