from django.urls import path
from django.contrib.auth.views import redirect_to_login,logout_then_login

from .viewsEmpleado import EmpleadosViews
from .viewsEmpresa import EmpresaViews
from .viewsUsuario import UsuarioViews
from .viewsMovimiento import MovimientosViews

urlpatterns=[#se crea este archivo para dar rutas 
    path('empresa/',EmpresaViews.as_view(), name="listar"),
    path('empresa/<int:id_empr>',EmpresaViews.as_view(), name="actualizar"),

    path('empleado/',EmpleadosViews.as_view(), name="listar"),
    path('empleado/<int:id_empleado>',EmpleadosViews.as_view(), name="actualizar"),

    path('movimientos/',MovimientosViews.as_view(), name="listar"),
    path('movimientos/<int:id_movimiento>',MovimientosViews.as_view(), name="actualizar"),

    #usuario Admin 
    path('usuario/',UsuarioViews.as_view(), name="listar"),
    path('usuario/<int:id_usua>',UsuarioViews.as_view(), name="actualizar"),

    path('',UsuarioViews.login, name="login usuario"),
    path('formularioRegistro/',UsuarioViews.formularioRegistro, 
            name="Ingresar Usuario"),

    path('formularioRegistroEmpresa/',EmpresaViews.formularioRegistroEmpresa, 
            name="Ingresar Empresa"),    

    path('actualizarUsuario/<int:id_usuarios>',UsuarioViews.formularioActualizar, 
            name="Formulario Actualizar"),
    path('actualizarUsuario/',UsuarioViews.actualizar, name="Actualizar"),

    #usuario empleado
    path('consultarMovimientos/',MovimientosViews.as_view(), name="listar"),
    path('formularioRegistroMovimientos/',
        MovimientosViews.formularioRegistroformularioRegistroMovimientos, name ='Ingrear Movimientos'),

]
