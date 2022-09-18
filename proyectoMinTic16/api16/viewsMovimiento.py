import json
from django.shortcuts import render
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

    # metodo para consultar por el ID, si no envio ningun parametro hace la consulta
    # general
    def get(self, request, id_movimiento=0):
        if id_movimiento > 0:
            movimientos = list(Movimientos.objects.filter(
                id_movimientos=id_movimiento).values())
            if len(movimientos) > 0:
                movimientoRespuesta = movimientos[0]
                datos = {"Movimientos": movimientoRespuesta}
            else:
                datos = {"Respuesta": "Dato no encontrado"}
        else:
            movimientos = list(Movimientos.objects.values())
            datos = {'listado movimientos': movimientos}
        return JsonResponse(datos)

    def post(self, request):  # metodo para enviar los datos por medio de post
        datos = json.loads(request.body)
        idUsuario=Usuarios.objects.get(id_usuarios=datos["id_usuarios"])
        crear=Movimientos.objects.create(id_movimientos=datos["id_movimientos"], 
                                 concepto=datos["concepto"], 
                                 monto=datos["monto"],
                                 tipo=datos["tipo"], 
                                 id_usuarios=idUsuario)
        crear.save();
        # fecha_creacion=datos["fecha_creacion"]
        return JsonResponse(datos)

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