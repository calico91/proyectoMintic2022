from pickle import TRUE
from django.db import models

class Empresa (models.Model):
    id_empresa=models.IntegerField(primary_key=True);
    nombre=models.CharField(max_length=30);
    nit=models.CharField(max_length=30, unique=True);
    ciudad=models.CharField(max_length=30);
    direccion=models.CharField(max_length=30);
    telefono=models.CharField(max_length=30);
    sector_productivo=models.CharField(max_length=31);
    fecha_creacion=models.DateField(auto_now_add=True,null=True);

class Usuarios(models.Model):
    id_usuarios=models.IntegerField(primary_key=True);
    email=models.CharField(max_length=30,unique=True);
    imagen=models.CharField(max_length=30);
    nombre_usuario=models.CharField(max_length=30,unique=True);
    password=models.CharField(max_length=30);
    rol=models.CharField(max_length=30);
    fecha_creacion=models.DateField(auto_now_add=True,null=True);

class Empleados (models.Model):
    id_empleado=models.IntegerField(primary_key=True);
    nombre=models.CharField(max_length=30);
    apellidos=models.CharField(max_length=30);
    email=models.CharField(max_length=30,unique=True);
    telefono=models.CharField(max_length=30);
    empresa=models.CharField(max_length=30);
    fecha_creacion=models.DateField(auto_now_add=True,null=True);
    id_usuarios=models.ForeignKey(Usuarios, on_delete=models.CASCADE);
    id_empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE);

class Movimientos (models.Model):#entidad pendiente por completar 
    id_movimientos=models.IntegerField(primary_key=True);
    fecha_creacion=models.DateField(auto_now_add=True,null=True);
    gastos=models.FloatField(max_length=30);
    ingresos=models.FloatField(max_length=30);
    id_empleado=models.ForeignKey(Empleados, on_delete=models.CASCADE);


