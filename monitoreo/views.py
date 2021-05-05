from django.shortcuts import render, redirect
from .models import Usuarios, Qrs, Restringidos, Control_usuarios
from .forms import UserRegisterForm, AdmiForms, formControlUsuarios, formEstado
from django.contrib import messages
from websites.models import Website
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def usuario(request):
    usuario = Usuarios.objects.get(user_id=request.user.id)
    qr = Qrs.objects.get(user_id=request.user.id)
    context = {
        'usuario' : usuario,
        'qr' : qr,
    }
    return render(request,'monitoreo/usuario/usuario.html', context)

def control_sintomas(request):
    control = Control_usuarios.objects.filter(user_id=request.user.id)
    context={
        'historicos' : control
        }
    return render(request,'monitoreo/usuario/control.html',context)

def inicio(request):
    return render(request,'monitoreo/home.html')

def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username']).pk
            if request.POST['id_tipo'] == '4':
                u = Usuarios(nombre=request.POST['first_name'],apellido=request.POST['last_name'],boleta='Invitado',nombre_usuario=request.POST['username'],clave=request.POST['password1'],fecha_nacimiento=request.POST['fecha_nacimiento'],id_tipo=request.POST['id_tipo'],user_id=user,curp=request.POST['curp'],email=request.POST['email'])
                u.save()
            else:
                u = Usuarios(nombre=request.POST['first_name'],apellido=request.POST['last_name'],boleta=request.POST['boleta'],nombre_usuario=request.POST['username'],clave=request.POST['password1'],fecha_nacimiento=request.POST['fecha_nacimiento'],id_tipo=request.POST['id_tipo'],user_id=user, curp=request.POST['curp'],email=request.POST['email'])
                u.save()
            cod= Qrs(nombre_usuario=request.POST['username'],user_id=user)
            cod.save()
            username = form.cleaned_data['username']
            messages.success(request,  "Usuario creado")
        
            if request.user.is_authenticated == True:
                usuario_logeado = User.objects.get(id=request.user.id) 
                if usuario_logeado.is_superuser == 1:
                    return redirect('lista_usuarios')
                else:
                    return redirect('login')
            else:
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

def usuariosrestringidos(request):
    usuario = Usuarios.objects.all()
    context = {
        'usuarios' : usuario
    }
    return render(request,'monitoreo/usuariosrestringidos.html', context)

def admi_edit_usuarios(request, usuario_id):
    editar = Usuarios.objects.get(id=usuario_id)
    if request.method == "POST":
        form = AdmiForms(request.POST,instance=editar)
        if form.is_valid():
            editar.nombre = request.POST['nombre']
            editar.apellido = request.POST['apellido']
            editar.boleta = request.POST['boleta']
            if editar.clave != "":
                editar.clave = request.POST['clave']
            editar.nombre_usuario = request.POST['nombre_usuario']
            editar.fecha_nacimiento = request.POST['fecha_nacimiento']
            editar.id_tipo = request.POST['id_tipo']
            editar.curp = request.POST['curp']
            editar.email = request.POST['email']
            editar.estado = request.POST['estado']
            editar.save()
            user = User.objects.get(id=editar.user_id)
            if user.username != request.POST['nombre_usuario']:
                user.username=request.POST['nombre_usuario']
            user.first_name=request.POST['nombre']
            user.last_name=request.POST['apellido']
            if editar.clave != "":
                user.set_password(request.POST['clave'])
            #if editar.estado != request.POST['estado']:
            #    user.is_active=request.POST['estado']
            user.email=request.POST['email']
            user.save()
            messages.success(request,  "Usuario editado correctamente.")
            return redirect('lista_usuarios')
    else:
        form=AdmiForms(instance=editar)
    context = {
        'form' : form
        }
    return render(request,'monitoreo/admi_edit_usuarios.html', context)

def monitoreoUsuario(request, usuario_id):
    usuario = Usuarios.objects.get(id=usuario_id)
    if request.method == "POST":
        formulario = formControlUsuarios(request.POST, instance=usuario)  
        user = User.objects.get(id=usuario.user_id)
        if formulario.is_valid():
            if (request.POST['temperatura'] < '39') and (request.POST['oxigenacion'] > '85'):
                usuario.estado = 1
                usuario.save()   
                user.is_active = 1
                user.save()
            else:
                usuario.estado = 0
                usuario.save()
                user.is_active = 0
                user.save()
            monitoreo= Control_usuarios(nombre_usuario=usuario.nombre_usuario,temperatura=request.POST['temperatura'],oxigenacion=request.POST['oxigenacion'],fecha_hora_registro=request.POST['fecha_hora_registro'],user_id=user.id)
            monitoreo.save() 
            messages.success(request,  "Guardado")
            return redirect('lista_usuarios')
    else:
        formulario=formControlUsuarios(instance=usuario)
        context = {
             'formulario':formulario
            }
        return render(request,'monitoreo/Monitoreo.html', context)

def eliminarUsuario(request, usuario_id):
    usuario = Usuarios.objects.get(id=usuario_id).delete
    usuar=User.objects.get(id=user_id)
    usuario.delete()
    usuar.delete()
    return redirect('Admi_listas')
