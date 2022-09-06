from django.db import models

class Empresa (models.Model):
    id_empresa=models.IntegerField(primary_key=True);
    nombre=models.CharField(max_length=30);
    nit=models.CharField(max_length=30);
    ciudad=models.CharField(max_length=30);
    direccion=models.CharField(max_length=30);
    telefono=models.CharField(max_length=30);
    sector_productivo=models.CharField(max_length=31);
    fecha_creacion=models.DateField(max_length=30);

class Usuarios(models.Model):
    id_usuarios=models.IntegerField(primary_key=True);
    email=models.CharField(max_length=30);
    imagen=models.CharField(max_length=30);
    nombre_usuario=models.CharField(max_length=30);
    password=models.CharField(max_length=30);
    rol=models.CharField(max_length=30);
    fecha_creacion=models.DateField(max_length=30);

class Empleados (models.Model):
    id_empleado=models.IntegerField(primary_key=True);
    nombre=models.CharField(max_length=30);
    apellidos=models.CharField(max_length=30);
    email=models.CharField(max_length=30);
    telefono=models.CharField(max_length=30);
    empresa=models.CharField(max_length=30);
    fecha_creacion=models.CharField(max_length=30);
    id_usuarios=models.ForeignKey(Usuarios, on_delete=models.CASCADE);
    id_empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE);

class Movimientos (models.Model):
    id_movimientos=models.IntegerField(primary_key=True);
    gastos=models.FloatField(max_length=30);
    ingresos=models.FloatField(max_length=30);
    id_empleado=models.ForeignKey(Empleados, on_delete=models.CASCADE);


