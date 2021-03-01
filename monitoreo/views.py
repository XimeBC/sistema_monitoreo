from django.shortcuts import render
from .models import Usuarios, Control_usuarios, Historial_ubicaciones
from .forms import Nuevo

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
    # Creamos un formulario vacío
    form = Nuevo()
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = Nuevo(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            # Después de guardar redireccionamos a la lista
            return render(request,'monitoreo/home.html')

    # Si llegamos al final renderizamos el formulario
    return render(request, "monitoreo/registro.html", {'form': form})
   
def inicio_sesion(request):
    return render(request,'monitoreo/inicio_sesion.html')