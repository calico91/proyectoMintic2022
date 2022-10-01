import json
from django.shortcuts import render,redirect
from django.views import View
from .models import Empleados, Usuarios, Empresa
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class EmpleadosViews(View):

    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    # def get(self,request): #metodo para consultar get para traer los datos en un json
    #     empresa=list(Empresa.objects.values())
    #     datos={'listadoempresa':empresa}
    #     return JsonResponse(datos)

    # metodo para consultar por el ID, si no envio ningun parametro hace la consulta
    # general
    # def get(self, request, id_empleado=0):
    #     if id_empleado > 0:
    #         empleados = list(Empleados.objects.filter(
    #             id_empleado=id_empleado).values())
    #         if len(empleados) > 0:
    #             empleadoRespuesta = empleados[0]
    #             datos = {"Empleado": empleadoRespuesta}
    #         else:
    #             datos = {"Respuesta": "Dato no encontrado"}
    #     else:
    #         empleados = list(Empleados.objects.values())
    #         datos = {'listado empleados': empleados}
    #     return JsonResponse(datos)

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

    def formularioRegistroEmpleado(request):
        usuario=Usuarios.objects.all()
        empresa=Empresa.objects.all()
        datos={
            "usuario":usuario,
            "empresa":empresa
        }

        return render(request,"registroEmpleado.html",datos)

    def formularioActualizarEmpleado(request,id_usuario):
        usuario=Empleados.objects.get(id_usuarios=id_usuario)
        datos={"usuario":usuario}
        return render(request,"actualizarMisDatos.html",datos)

    def post(self, request):  # metodo para enviar los datos por medio de post
        idUsuario=Usuarios.objects.get(id_usuarios=request.POST["id_usuarios"])
        idempresa=Empresa.objects.get(id_empresa=request.POST["id_empresa"])
        Empleados.objects.create(id_empleado=request.POST["id_empleado"],
                                nombre=request.POST["nombre"],
                                apellidos=request.POST["apellidos"],
                                email=request.POST["email"],
                                telefono=request.POST["telefono"],
                                empresa=request.POST["empresa"],
                                id_usuarios=idUsuario,
                                id_empresa=idempresa,)

        return redirect('/consultarEmpleado/')

    def get(self, request, id_empleado=0):
        if id_empleado > 0:
            empleado = list(Empleados.objects.filter(
                id_empleados=id_empleado).values())
            if len(empleado) > 0:
                empleadoRespuesta = empleado[0]
                datos = {"empleado": empleadoRespuesta}
            else:
                datos = {"Respuesta": "Dato no encontrado"}
        else:
            templeteName="consultarEmpleado.html"
            empleado = Empleados.objects.all()
            datos = {'listadoEmpleado': empleado}
        return render(request,templeteName,datos)

    def formularioActualizarEmpleados(request,id_empleado):
        empleado=Empleados.objects.get(id_empleado=id_empleado)
        usuario=Usuarios.objects.all()
        empresa=Empresa.objects.all()
        datos={
            "empleado":empleado,
            "usuario":usuario,
            "empresa":empresa
        }

        return render(request,"actualizarEmpleado.html",datos)
    
    def actualizarEmpleado(request):#actualizar 
        id_empleado=request.POST['id_empleado']
        nombre=request.POST['nombre']
        apellidos=request.POST['apellidos']
        email=request.POST['email']
        telefono=request.POST['telefono']
        empresa=request.POST['empresa']
        # id_usuarios=request.POST['id_usuarios']
        # id_empresa=request.POST['id_empresa']

        empleados=Empleados.objects.get(id_empleado=id_empleado,)
        empleados.nombre=nombre
        empleados.apellidos=apellidos
        empleados.email=email
        empleados.telefono=telefono
        empleados.empresa=empresa
        empleados.save()

        if(request.POST['empresa']=='admin'):
            return redirect ('/consultarEmpleado/')
        else:
            detalleUsuario=Usuarios.objects.get(nombre_usuario=request.POST["id_usuarios"])
            datos={"empleado":detalleUsuario,
                "datosEmpleados":empleados,
                "mensaje":{1:"Datos Actualizados"}}
            
            return render(request,"registroMovimientos.html", context=datos)


    def eliminarEmpleado(request,id_empleado):
        #usuario=Usuarios.objects.filter(id_usuarios=id_usuarios).values()
        Empleados.objects.filter(id_empleado=id_empleado).delete()
        return redirect ('/consultarEmpleado/')