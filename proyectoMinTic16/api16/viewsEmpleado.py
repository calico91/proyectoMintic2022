import json
from django.shortcuts import render
from django.views import View
from .models import Empleados, Usuarios, Empresa
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class EmpleadosViews(View):

    # codigo para un tema de seguridad y cookies
    # @method_decorator(csrf_exempt)
    # def dispatch(self,request,args,*kwargs):
    #     return super().dispatch(request,args,**kwargs)

    # def get(self,request): #metodo para consultar get para traer los datos en un json
    #     empresa=list(Empresa.objects.values())
    #     datos={'listadoempresa':empresa}
    #     return JsonResponse(datos)

    # metodo para consultar por el ID, si no envio ningun parametro hace la consulta
    # general
    def get(self, request, id_empleado=0):
        if id_empleado > 0:
            empleados = list(Empleados.objects.filter(
                id_empleado=id_empleado).values())
            if len(empleados) > 0:
                empleadoRespuesta = empleados[0]
                datos = {"Empleado": empleadoRespuesta}
            else:
                datos = {"Respuesta": "Dato no encontrado"}
        else:
            empleados = list(Empleados.objects.values())
            datos = {'listado empleados': empleados}
        return JsonResponse(datos)

    def post(self, request):  # metodo para enviar los datos por medio de post
        datos = json.loads(request.body)
        idUsuario=Usuarios.objects.get(id_usuarios=datos["id_usuarios"])
        idEmpresa=Empresa.objects.get(id_empresa=datos["id_empresa"])
        crear=Empleados.objects.create(id_empleado=datos["id_empleado"], 
                                 nombre=datos["nombre"], 
                                 apellidos=datos["apellidos"],
                                 email=datos["email"], 
                                 telefono=datos["telefono"], 
                                 empresa=datos["empresa"], 
                                 id_usuarios=idUsuario, 
                                 id_empresa=idEmpresa)
        crear.save();
        # fecha_creacion=datos["fecha_creacion"]
        return JsonResponse(datos)

    def put(self, request, id_empleado):  # metodo para actualizar datos
        datos = json.loads(request.body)
        idUsuario=Usuarios.objects.get(id_usuarios=datos["id_usuarios"])
        idEmpresa=Empresa.objects.get(id_empresa=datos["id_empresa"])
        empleado = list(Empleados.objects.filter(
            id_empleado=id_empleado).values())
        if len(empleado) > 0:
            empl = Empleados.objects.get(id_empleado=id_empleado)
            empl.nombre = datos['nombre']
            empl.apellidos = datos['apellidos']
            empl.email = datos['email']
            empl.telefono = datos['telefono']
            empl.empresa = datos['empresa']
            empl.id_usuarios=idUsuario
            empl.id_empresa=idEmpresa

            # emp.fecha_creacion=datos['fecha_creacion']
            empl.save()
            mensaje = {"Respuesta": "Datos Actualizados"}
        else:
            mensaje = {"Respuesta": "Datos no encontrados"}
        return JsonResponse(mensaje)

    def delete(self, request, id_empleado):  # metodo para eliminar
        empleados = list(Empleados.objects.filter(
            id_empleado=id_empleado).values())
        if len(empleados) > 0:
            Empleados.objects.filter(id_empleado=id_empleado).delete()

            mensaje = {"Empleados Eliminadaos": len(empleados),
                       "Id Empleado": empleados[0].get('id_empleado', 'nombre'),
                       "Nombre empleado": empleados[0].get('nombre')}
        else:
            mensaje = {"Respuesta": "Dato no encontrado"}
        return JsonResponse(mensaje)