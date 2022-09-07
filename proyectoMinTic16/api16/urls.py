from django.urls import path
from .views import EmpresaViews

urlpatterns=[#se crea este archivo para dar rutas 
    path('empresa/',EmpresaViews.as_view(), name="listar"),
    path('empresa/<int:id_empr>',EmpresaViews.as_view(), name="actualizar")

]