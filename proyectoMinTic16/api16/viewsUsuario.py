import email
from email import message
import json
from sqlite3 import DateFromTicks
from django.shortcuts import render,redirect
from django.views import View
from .models import  Empleados, Usuarios
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class UsuarioViews(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    

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


    #metodo para consultar 
    def get (self,request, id_usua=0):
        if id_usua>0:
            usuario=list(Usuarios.objects.filter(id_usuarios=id_usua).values())
            if len(usuario)>0:
                usuariorespuesta=usuario[0]
                datos={"Usuarios":usuariorespuesta}
            else:
                datos={"Respuesta":"Dato no encontrado"}
        else:
            templeteName="consultarUsuario.html"
            usuario=Usuarios.objects.all()
            datos={'listadoUsuario':usuario}
        return render(request,templeteName,datos)

     #metodo para cargar el formulario de registro
    def formularioRegistro(request):
        return render(request,"registroUsuario.html")

    #metodo para ingresar 
    def post(self,request):

        Usuarios.objects.create(id_usuarios=request.POST["id_usuarios"],
                                email=request.POST["email"],
                                imagen=request.POST["imagen"],
                                nombre_usuario=request.POST["nombre_usuario"],
                                password=request.POST["password"],
                                rol=request.POST["rol"])

        return redirect('/usuario/')

    #metodo para loguear usuarios
    def login(request):

        if request.method=='POST':

            try:

                detalleUsuario=Usuarios.objects.get(
                    nombre_usuario=request.POST['nombre_usuario'],
                    password=request.POST['password'],
                    )
                

                if detalleUsuario.rol=="administrador":
                    request.session['nombre_usuario']=detalleUsuario.nombre_usuario
                    datos={"usuarios":detalleUsuario}
                    return render(request,'admin.html',context=datos)

                elif detalleUsuario.rol=="empleado":
                    request.session['nombre_usuario']=detalleUsuario.nombre_usuario
                    datos={"empleado":detalleUsuario}
                    return render(request,'registroMovimientos.html', context=datos)
            
            except Usuarios.DoesNotExist as e:
                error={"inicioFallido":{1:"usuario o contraseña Incorrecta"}}
                return render(request,'login.html',context=error)
                #message.success(request,"usuario o contraseña incorrecta")
                
                
        return render(request,'login.html')

    # metodo para cargar datos que se desean actualizar al formulario 
    def formularioActualizar(request,id_usuarios):
        usuarios=Usuarios.objects.get(id_usuarios=id_usuarios)
        datos={
            'usuarios':usuarios
        }

        return render(request,"actualizarUsuario.html",datos)


    def actualizar(request):
        id_usuarios=request.POST['id_usuarios']
        email=request.POST['email']
        imagen=request.POST['imagen']
        nombre_usuario=request.POST['nombre_usuario']
        password=request.POST['password']
        rol=request.POST['rol']

        usuarios=Usuarios.objects.get(id_usuarios=id_usuarios)
        #id_usuarios=usuarios
        usuarios.email=email
        usuarios.imagen=imagen
        usuarios.nombre_usuario=nombre_usuario
        usuarios.password=password
        usuarios.rol=rol
        usuarios.save()
        return redirect ('/consultarUsuario/')


    def eliminar(request,id_usuarios):
        #usuario=Usuarios.objects.filter(id_usuarios=id_usuarios).values()
        Usuarios.objects.filter(id_usuarios=id_usuarios).delete()
        return redirect ('/consultarUsuario/')

    def consultarInnerJoin(request,id_usuarios):
        consulta=Empleados.objects.select_related('id_usuarios').filter(id_usuarios=id_usuarios)
        templateName="consultarEmpleadosUsuarios.html"
        datos={"lista":consulta}
        return render(request,templateName,datos)