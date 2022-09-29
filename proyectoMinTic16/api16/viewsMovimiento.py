import json
from django.shortcuts import render,redirect
from django.views import View
from .models import  Movimientos, Usuarios 
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class MovimientosViews(View):

    # codigo para un tema de seguridad y cookies
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    # def get(self,request): #metodo para consultar get para traer los datos en un json
    #     empresa=list(Empresa.objects.values())
    #     datos={'listadoempresa':empresa}
    #     return JsonResponse(datos)

    
    
    # def post(self, request):  # metodo para enviar los datos por medio de post
    #     datos = json.loads(request.body)
    #     idUsuario=Usuarios.objects.get(id_usuarios=datos["id_usuarios"])
    #     crear=Movimientos.objects.create( 
    #                              concepto=datos["concepto"], 
    #                              monto=datos["monto"],
    #                              tipo=datos["tipo"], 
    #                              id_usuarios=idUsuario)
    #     crear.save();
    #     # fecha_creacion=datos["fecha_creacion"]
    #     return JsonResponse(datos)

    def put(self, request, id_movimiento):  # metodo para actualizar datos
        datos = json.loads(request.body)
        idUsuario=Usuarios.objects.get(id_usuarios=datos["id_usuarios"])
        movimiento = list(Movimientos.objects.filter(
            id_movimientos=id_movimiento).values())
        if len(movimiento) > 0:
            mov = Movimientos.objects.get(id_movimientos=id_movimiento)
            mov.concepto = datos['concepto']
            mov.monto = datos['monto']
            mov.tipo = datos['tipo']
            mov.id_usuarios=idUsuario

            # emp.fecha_creacion=datos['fecha_creacion']
            mov.save()
            mensaje = {"Respuesta": "Datos Actualizados"}
        else:
            mensaje = {"Respuesta": "Datos no encontrados"}
        return JsonResponse(mensaje)
        

    def delete(self, request, id_movimiento):  # metodo para eliminar
        movimientos = list(Movimientos.objects.filter(
            id_movimientos=id_movimiento).values())
        if len(movimientos) > 0:
            Movimientos.objects.filter(id_movimientos=id_movimiento).delete()

            mensaje = {"respuesta": "datos eliminados" }
        else:
            mensaje = {"Respuesta": "Dato no encontrado"}
        return JsonResponse(mensaje)

    # metodo para consultar por el ID, si no envio ningun parametro hace la consulta
    # general

    def get(self, request, id_usuarios=0):
        if id_usuarios > 0:
            movimientos = Movimientos.objects.filter(
                id_usuarios=id_usuarios)
            datos = {"listadoMovimientos": movimientos}
            return render(request,"consultarMovimientos.html",datos)
        else:
            movimientos = Movimientos.objects.all()
            datos = {'listadoMovimientos': movimientos}
            return render(request,"consultarMovimientos.html",datos)
        
    #carga vista de formulario
    def formularioRegistroMovimientos(request):
        return render(request,"registroMovimientos.html")

    def post(self, request):  # metodo para enviar los datos por medio de post
        idUsuario=Usuarios.objects.get(id_usuarios=request.POST["id_usuarios"])
        Movimientos.objects.create(
                                concepto=request.POST["concepto"],
                                monto=request.POST["monto"],
                                id_usuarios=idUsuario,
                                tipo=request.POST["tipo"])

        return redirect('/consultarMovimientos/')