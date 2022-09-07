import json
from django.shortcuts import render
from django.views import View
from .models import Empresa
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class EmpresaViews(View):

    #codigo para un tema de seguridad y cookies 
    # @method_decorator(csrf_exempt)
    # def dispatch(self,request,*args,**kwargs):
    #     return super().dispatch(request,args,**kwargs)

    # def get(self,request): #metodo para consultar get para traer los datos en un json 
    #     empresa=list(Empresa.objects.values())
    #     datos={'listadoempresa':empresa}
    #     return JsonResponse(datos)

    #metodo para consultar por el ID, si no envio ningun parametro hace la consulta 
    #general
    def get(self,request,id_empr=0): 
        if id_empr>0:
            empresa=list(Empresa.objects.filter(id_empresa=id_empr).values())
            if len(empresa)>0:
                empresares=empresa[0]
                datos={"Empresa":empresares}
            else:
                datos={"Respuesta":"Dato no encontrado"}
        else:
            empresa=list(Empresa.objects.values())
            datos={'listadoempresa':empresa}
        return JsonResponse(datos)

    
    
    def post(self,request): # metodo para enviar los datos por medio de post
        datos=json.loads(request.body)
        Empresa.objects.create(id_empresa=datos["id_empresa"],nombre=datos["nombre"],
        nit=datos["nit"],ciudad=datos["ciudad"],direccion=datos["direccion"],
        telefono=datos["telefono"],sector_productivo=datos["sector_productivo"],
        fecha_creacion=datos["fecha_creacion"])
        return JsonResponse(datos)

    def put(self,request,id_empr):#metodo para actualizar datos 
        datos=json.loads(request.body)
        empresa=list(Empresa.objects.filter(id_empresa=id_empr).values())
        if len(empresa)>0:
            emp=Empresa.objects.get(id_empresa=id_empr)
            emp.nombre=datos['nombre']
            emp.nit=datos['nit']
            emp.ciudad=datos['ciudad']
            emp.direccion=datos['direccion']
            emp.telefono=datos['telefono']
            emp.sector_productivo=datos['sector_productivo']
            emp.fecha_creacion=datos['fecha_creacion']
            emp.save()
            mensaje={"Respuesta":"Datos Actualizados"}
        else:
            mensaje={"Respuesta":"Datos no encontrados"}
        return JsonResponse(mensaje)
    
    def delete(self,request,id_empr): #metodo para eliminar 
        empresa=list(Empresa.objects.filter(id_empresa=id_empr).values())
        if len(empresa)>0:
            Empresa.objects.filter(id_empresa=id_empr).delete()
            mensaje={"Respuesta":"El registro se elimino"}
        else:
            mensaje={"Respuesta":"Dato no encontrado"}
        return JsonResponse(mensaje)