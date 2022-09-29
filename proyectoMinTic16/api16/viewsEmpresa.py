import json
from operator import attrgetter
from django.shortcuts import render,redirect
from django.views import View
from .models import Empresa
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class EmpresaViews(View):

    #codigo para un tema de seguridad y cookies 
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

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
                #empresarespuesta=empresa[0]
                datos={"Empresa":empresa.len}
            else:
                datos={"Respuesta":"Dato no encontrado"}
        else:
            empresa=Empresa.objects.all()
            datos={'listadoEmpresa': empresa}
        return render (request,"consultarEmpresa.html",datos)

    
    
    def post(self,request): # metodo para enviar los datos por medio de post
        Empresa.objects.create(
            nombre=request.POST["nombre"],
            nit=request.POST["nit"],
            ciudad=request.POST["ciudad"],
            direccion=request.POST["direccion"],
            telefono=request.POST["telefono"],
            sector_productivo=request.POST["sector_productivo"])
        #fecha_creacion=datos["fecha_creacion"]
        return redirect ('/consultarEmpresa/')

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
            #emp.fecha_creacion=datos['fecha_creacion']
            emp.save()
            mensaje={"Respuesta":"Datos Actualizados"}
        else:
            mensaje={"Respuesta":"Datos no encontrados"}
        return JsonResponse(mensaje)
    
    def delete(self,request,id_empr): #metodo para eliminar 
        empresa=list(Empresa.objects.filter(id_empresa=id_empr).values())
        if len(empresa)>0:
            Empresa.objects.filter(id_empresa=id_empr).delete()
            
            mensaje={"Empresas Eliminadas":len(empresa),
                     "Id empresa":empresa[0].get('id_empresa'),
                     "Nombre empresa":empresa[0].get('nombre')}
        else:
            mensaje={"Respuesta":"Dato no encontrado"}
        return JsonResponse(mensaje)

    #################################

    #metodo para cargar el formulario de registro
    def formularioRegistroEmpresa(request):
        return render(request,"registroEmpresa.html")

    def formularioActualizarEmpresa(request,id_empresa):
        empresa=Empresa.objects.get(id_empresa=id_empresa)
        datos={'empresa':empresa}

        return render(request,"actualizarEmpresa.html",datos)

    def actualizarEmpresa(request):
        id_empresa=request.POST['id_empresa']
        nombre=request.POST['nombre']
        nit=request.POST['nit']
        ciudad=request.POST['ciudad']
        direccion=request.POST['direccion']
        telefono=request.POST['telefono']
        sector_productivo=request.POST['sector_productivo']

        empresa=Empresa.objects.get(id_empresa=id_empresa)
        #id_usuarios=usuarios
        empresa.nombre=nombre
        empresa.nit=nit
        empresa.ciudad=ciudad
        empresa.direccion=direccion
        empresa.telefono=telefono
        empresa.sector_productivo=sector_productivo
        empresa.save()
        return redirect ('/consultarEmpresa/')

    def eliminarEmpresa(request,id_empresa):
        #usuario=Usuarios.objects.filter(id_usuarios=id_usuarios).values()
        Empresa.objects.filter(id_empresa=id_empresa).delete()
        return redirect ('/consultarEmpresa/')
