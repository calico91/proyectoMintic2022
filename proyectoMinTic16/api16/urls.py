from django.urls import path
from django.contrib.auth.views import redirect_to_login,logout_then_login

from api16.models import Usuarios

from .viewsEmpleado import EmpleadosViews
from .viewsEmpresa import EmpresaViews
from .viewsUsuario import UsuarioViews
from .viewsMovimiento import MovimientosViews

urlpatterns=[#se crea este archivo para dar rutas 

    #empresa    
    path('formularioRegistroEmpresa/',EmpresaViews.formularioRegistroEmpresa, 
            name="Ingresar Empresa"),    
    path('actualizarEmpresa/<int:id_empresa>',EmpresaViews.formularioActualizarEmpresa, 
            name="Formulario Actualizar empresa"),
    path('actualizarEmpresa/',EmpresaViews.actualizarEmpresa, 
            name="Actualizar Empresa"), 
    path('eliminarEmpresa/<int:id_empresa>',EmpresaViews.eliminarEmpresa, name="EliminarEmpresa"),
    path('consultarEmpresa/',EmpresaViews.as_view(), name="listar empresas"),
    path('empresa/<int:id_empr>',EmpresaViews.as_view(), name="actualizar"),

    # datos empleado

    path('empleado/',EmpleadosViews.as_view(), name="listar"),
    path('empleado/<int:id_usuario>',EmpleadosViews.
        formularioActualizarEmpleado, name="frmActEmpleado"),
    path('formularioRegistroEmpleado/',EmpleadosViews.formularioRegistroEmpleado, name="listar"), 
    path('consultarEmpleado/',EmpleadosViews.as_view(), name="listar"),   

    #movimientos    
    path('movimientos/',MovimientosViews.as_view(), name="listar"),

    path('movimientos/<int:id_usuarios>',MovimientosViews.as_view(), name="actualizar"),

    #usuario Admin 
    path('consultarUsuario/',UsuarioViews.as_view(), name="listar Usuarios"),
    path('usuario/<int:id_usua>',UsuarioViews.as_view(), name="actualizar"),

    path('',UsuarioViews.login, name="login usuario"),
    path('formularioRegistro/',UsuarioViews.formularioRegistro, 
            name="Ingresar Usuario"),

    

    path('actualizarUsuario/<int:id_usuarios>',UsuarioViews.formularioActualizar, 
            name="Formulario Actualizar"),

    path('actualizarUsuario/',UsuarioViews.actualizarUsuario, name="Actualizar"),

    path('eliminarUsuario/<int:id_usuarios>',UsuarioViews.eliminar, name="Eliminar"),

    #usuario empleado
    path('consultarMovimientos/',MovimientosViews.as_view(), name="listar"),

    path('formularioRegistroMovimientos/',
        MovimientosViews.formularioRegistroMovimientos, name ='Ingrear Movimientos'),
        
    path('consultarEmpleadosUsuarios/<int:id_usuarios>',UsuarioViews.consultarInnerJoin, name="consultarInner"),
]
