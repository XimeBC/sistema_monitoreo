from django.shortcuts import render, redirect
from .models import Usuarios, Control_usuarios, Historial_ubicaciones, Qrs
from .forms import UserRegisterForm
from django.contrib import messages
from websites.models import Website

def usuario(request):
    nombre_usuario= Usuarios.objects.filter(nombre_usuario= 'nombre_usuario')
 
    return render(request,'monitoreo/usuario/usuario.html')

def control_sintomas(request):
    control_sintomas = Control_usuarios.objects.all()
    return render(request,'monitoreo/usuario/control.html',
    {'control_sintomas' : control_sintomas})

def historial_ubicaciones(request):
    historial_ubicaciones = Historial_ubicaciones.objects.all()
    return render(request,'monitoreo/usuario/ubicaciones.html',
    {'Historial_ubicaciones' : historial_ubicaciones})


def inicio(request):
    return render(request,'monitoreo/usuario/usuario.html')


def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            u = Usuarios(nombre=request.POST['first_name'],apellido=request.POST['last_name'],boleta=request.POST['boleta'],nombre_usuario=request.POST['username'],clave=request.POST['password1'],fecha_nacimiento=request.POST['fecha_nacimiento'])
            u.save()
            cod= Qrs(fecha_hora_caducidad=request.POST['username'])
            cod.save()
            username = form.cleaned_data['username']
            messages.success(request, f"Usuario{username}creado")
            return redirect('login')
            

    else:
        form=UserRegisterForm()

    context = { 'form':form }    
    return render(request,'monitoreo/registro.html',context)

def Qr(request):
    fecha_hora_caducidad = "Welcome to"
    obj = Qrs.objects.get(id=2)
    context = {
        'fecha_hora_caducidad': fecha_hora_caducidad,
        'obj' : obj,
    }
    return render(request,'monitoreo/usuario/Qr.html', context)