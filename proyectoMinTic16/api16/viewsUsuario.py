import email
from email import message
import json
from sqlite3 import DateFromTicks
from django.shortcuts import render
from django.views import View
from .models import  Usuarios
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class UsuarioViews(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get (self,request, id_usua=0):
        if id_usua>0:
            usuario=list(Usuarios.objects.filter(id_usuarios=id_usua).values())
            if len(usuario)>0:
                usuariorespuesta=usuario[0]
                datos={"Usuarios":usuariorespuesta}
            else:
                datos={"Respuesta":"Dato no encontrado"}
        else:
            usuario=list(Usuarios.objects.values())
            datos={'listado usuario':usuario}
        return JsonResponse(datos)

    def post(self,request):
        datos=json.loads(request.body)
        Usuarios.objects.create(id_usuarios=datos["id_usuarios"],
                                email=datos["email"],
                                imagen=datos["imagen"],
                                nombre_usuario=datos["nombre_usuario"],
                                password=datos["password"],
                                rol=datos["rol"])
        return JsonResponse(datos)

    def put (self,request,id_usua):
        dato=json.loads(request.body)
        usuario=list(Usuarios.objects.filter(id_usuarios=id_usua).values())
        if len(usuario)>0:
            usu=Usuarios.objects.get(id_usuarios=id_usua)
            usu.email=dato['email']
            usu.imagen=dato['imagen']
            usu.nombre_usuario=dato['nombre_usuario']
            usu.password=dato['password']
            usu.rol=dato['rol']
            usu.save()
            mensaje={"Respuesta":"Datos Actualizados"}
        else:
            mensaje={"Respuesta":"Datos no Actualizados"}
        return JsonResponse(mensaje)

    def delete(self,request,id_usua):
        usuario=list(Usuarios.objects.filter(id_usuarios=id_usua).values())
        if len(usuario)>0:
            Usuarios.objects.filter(id_usuarios=id_usua).delete()
            mensaje={"Usuario Eliminado":len(usuario),
                    "Id Usuario":usuario[0].get('id_usuarios','nombre_usuario'),
                    "Nombre del usuario":usuario[0].get('nombre_usuario')}
        else:
            mensaje={"Respuesta":"Dato no encontrado"}
        return JsonResponse(mensaje)        

    #metodo para loguear usuarios
    def login(request):

        if request.method=='POST':

            try:

                detalleUsuario=Usuarios.objects.get(
                    nombre_usuario=request.POST['nombre_usuario'],
                    password=request.POST['password'])
                

                if detalleUsuario.rol=="administrador":
                    request.session['nombre_usuario']=detalleUsuario.nombre_usuario
                    return render(request,'admin.html')

                elif detalleUsuario.rol=="empleado":
                    request.session['nombre_usuario']=detalleUsuario.nombre_usuario
                    return render(request,'empleado.html')

                elif detalleUsuario.rol=="cliente":
                    request.session['nombre_usuario']=detalleUsuario.nombre_usuario
                    return render(request,'cliente.html')
            
            except Usuarios.DoesNotExist as e:
                message.success(request,"usuario o contraseña incorrecta")
                
        return render(request,'login.html')


            