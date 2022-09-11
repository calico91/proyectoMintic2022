from django.urls import path
from .viewsEmpresa import EmpresaViews
from .viewsUsuario import UsuarioViews

urlpatterns=[#se crea este archivo para dar rutas 
    path('empresa/',EmpresaViews.as_view(), name="listar"),
    path('empresa/<int:id_empr>',EmpresaViews.as_view(), name="actualizar"),

    path('usuario/',UsuarioViews.as_view(), name="listar"),
    path('usuario/<int:id_usua>',UsuarioViews.as_view(), name="actualizar")

    

]