from django.urls import path

from .viewsEmpleado import EmpleadosViews
from .viewsEmpresa import EmpresaViews
from .viewsUsuario import UsuarioViews
from .viewsMovimiento import MovimientosViews

urlpatterns=[#se crea este archivo para dar rutas 
    path('empresa/',EmpresaViews.as_view(), name="listar"),
    path('empresa/<int:id_empr>',EmpresaViews.as_view(), name="actualizar"),

    path('usuario/',UsuarioViews.as_view(), name="listar"),
    path('usuario/<int:id_usua>',UsuarioViews.as_view(), name="actualizar"),

    path('empleado/',EmpleadosViews.as_view(), name="listar"),
    path('empleado/<int:id_empleado>',EmpleadosViews.as_view(), name="actualizar"),

    path('movimientos/',MovimientosViews.as_view(), name="listar"),
    path('movimientos/<int:id_movimiento>',MovimientosViews.as_view(), name="actualizar"),

    path('login/',UsuarioViews.login, name="login usuario")
]
