import json
from django.shortcuts import render
from django.views import View
from .models import Empresa
from django.http.response import JsonResponse

class EmpresaViews(View):

    def get(self,request): #metodo get para traer los datos en un json 
        empresa=list(Empresa.objects.values())
        datos={'listadoempresa':empresa}
        return JsonResponse(datos)
    
    def post(self,request):
        datos=json.loads(request.body)
        Empresa.objects.create(id_empresa=datos["id_empresa"],nombre=datos["nombre"],
        nit=datos["nit"],ciudad=datos["ciudad"],direccion=datos["direccion"],
        telefono=datos["telefono"],sector_productivo=datos["sector_productivo"],
        fecha_creacion=datos["fecha_creacion"])
        return JsonResponse(datos)