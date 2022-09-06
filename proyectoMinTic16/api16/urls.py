from django.urls import path
from .views import EmpresaViews

urlpatterns=[
    path('empresa/',EmpresaViews.as_view(), name="listar")
]