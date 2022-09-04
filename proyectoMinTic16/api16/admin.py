from django.contrib import admin
from django.contrib import admin
from .models import Empresa,Usuarios,Empleados,Movimientos
# Register your models here.

admin.site.register(Empresa)
admin.site.register(Usuarios)
admin.site.register(Empleados)
admin.site.register(Movimientos)