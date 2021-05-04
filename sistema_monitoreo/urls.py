"""sistema_monitoreo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from monitoreo import views as monitoreo_views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('monitoreo/usuario', monitoreo_views.usuario, name="usuario"),
    path('monitoreo/inicio', monitoreo_views.inicio, name="inicio"),
    path('monitoreo/registro/', monitoreo_views.registro, name='registro'),
    path('monitoreo/control', monitoreo_views.control_sintomas, name="control"),
    path('monitoreo/login/', LoginView.as_view(template_name='monitoreo/login.html'), name='login'),    
    path('monitoreo/logout/', LogoutView.as_view(template_name='monitoreo/logout.html'), name='logout'),
    path('monitoreo/lista_usuarios', monitoreo_views.lista_usuarios, name="lista_usuarios"),
    path('monitoreo/admi_edit_usuarios/<int:usuario_id>/', monitoreo_views.admi_edit_usuarios, name="admi_edit_usuarios"),
    path("monitoreo/monitoreoUsuario/<int:usuario_id>/", monitoreo_views.monitoreoUsuario, name="monitoreoUsuario"),
    path("monitoreo/eliminarUsuario/<int:usuario_id>/", monitoreo_views.eliminarUsuario, name="eliminarUsuario"),   
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)