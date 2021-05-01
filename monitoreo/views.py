from django.shortcuts import render, redirect
from .models import Usuarios, Control_usuarios, Qrs
from .forms import UserRegisterForm, AdmiForms, UserForm
from django.contrib import messages
from websites.models import Website
from django.contrib.auth.models import User

def usuario(request):
    usuario = Usuarios.objects.get(user_id=request.user.id)
    qr = Qrs.objects.get(user_id=request.user.id)
    context = {
        'usuario' : usuario,
        'qr' : qr,
    }
    return render(request,'monitoreo/usuario/usuario.html', context)

def control_sintomas(request):
    control_sintomas = Control_usuarios.objects.all()
    return render(request,'monitoreo/usuario/control.html',
    {'control_sintomas' : control_sintomas})

def inicio(request):
    return render(request,'monitoreo/home.html')

def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username']).pk
            if request.POST['id_tipo'] == '4':
                u = Usuarios(nombre=request.POST['first_name'],apellido=request.POST['last_name'],boleta='Invitado',nombre_usuario=request.POST['username'],clave=request.POST['password1'],fecha_nacimiento=request.POST['fecha_nacimiento'],id_tipo=request.POST['id_tipo'],user_id=user)
                u.save()
            else:
                u = Usuarios(nombre=request.POST['first_name'],apellido=request.POST['last_name'],boleta=request.POST['boleta'],nombre_usuario=request.POST['username'],clave=request.POST['password1'],fecha_nacimiento=request.POST['fecha_nacimiento'],id_tipo=request.POST['id_tipo'],user_id=user)
                u.save()
            cod= Qrs(nombre_usuario=request.POST['username'],user_id=user)
            cod.save()
            username = form.cleaned_data['username']
            messages.success(request,  "Usuario creado")
            return redirect('login')
    else:
        form=UserRegisterForm()

    context = { 'form':form }    
    return render(request,'monitoreo/registro.html',context)

def lista_usuarios(request):
    usuarios = Usuarios.objects.all()
    context = {
        'usuarios' : usuarios
    }
    return render(request,'monitoreo/listausuarios.html', context)

def admi_edit_usuarios(request, id):
    form = UserForm(request.POST,instance=admi_edit_usuarios)
    if form.is_valid():
        form.save()
        user = User.objects.get(id=id).pk
        if request.POST['id_tipo'] == '4':
            u = Usuarios(nombre=request.POST['first_name'],apellido=request.POST['last_name'],boleta='Invitado',nombre_usuario=request.POST['username'],clave=request.POST['password1'],fecha_nacimiento=request.POST['fecha_nacimiento'],id_tipo=request.POST['id_tipo'],user_id=user)
            u.save()
        else:
            u = Usuarios(nombre=request.POST['first_name'],apellido=request.POST['last_name'],boleta=request.POST['boleta'],nombre_usuario=request.POST['username'],clave=request.POST['password1'],fecha_nacimiento=request.POST['fecha_nacimiento'],id_tipo=request.POST['id_tipo'],user_id=user)
            u.save()
        cod= Qrs(nombre_usuario=request.POST['username'],user_id=user)
        cod.save()
        messages.success(request,  "Guardado")
        return redirect('admin_edit_usuarios')
    else:
        form=UserForm()

    context = { 'User':form }    
    return render(request,'monitoreo/listausuarios.html',context)
