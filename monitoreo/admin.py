from django.contrib import admin
from .models import Control_usuarios, Usuarios, Restringidos, Qrs, Tipos_usuario
# Register your models here.
 
admin.site.register(Control_usuarios)
admin.site.register(Tipos_usuario)
admin.site.register(Restringidos)
admin.site.register(Qrs)
admin.site.register(Usuarios)