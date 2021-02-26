from django.shortcuts import render
from .models import Usuarios

# Create your views here.
def usuario(request):
    usuarios = Usuarios.objects.all()
    return render(request,'monitoreo/usuario/usuario.html',
    {'usuarios' : usuarios})