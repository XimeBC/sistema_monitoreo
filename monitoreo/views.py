from django.shortcuts import render, redirect
from .models import Usuarios, Control_usuarios, Historial_ubicaciones
from .forms import UserRegisterForm
from django.contrib import messages

def usuario(request):
    usuarios = Usuarios.objects.all()
    return render(request,'monitoreo/usuario/usuario.html',
    {'usuarios' : usuarios})

def control_sintomas(request):
    control_sintomas = Control_usuarios.objects.all()
    return render(request,'monitoreo/usuario/control.html',
    {'control_sintomas' : control_sintomas})

def historial_ubicaciones(request):
    historial_ubicaciones = Historial_ubicaciones.objects.all()
    return render(request,'monitoreo/usuario/ubicaciones.html',
    {'Historial_ubicaciones' : historial_ubicaciones})


def inicio(request):
    return render(request,'monitoreo/home.html')


def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"Usuario{username}creado")
             messages.success(request, f"Usuario{form.g}creado")
            return redirect('inicio')
    else:
        form=UserRegisterForm()

    context = { 'form':form }    
    return render(request,'monitoreo/registro.html',context)

def inicio_sesion(request):
    return render(request,'monitoreo/inicio_sesion.html')