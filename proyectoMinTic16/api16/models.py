from pickle import TRUE
from django.db import models


class Empresa (models.Model):
    id_empresa=models.AutoField(primary_key=True);
    nombre=models.CharField(max_length=30);
    nit=models.CharField(max_length=30, unique=True);
    ciudad=models.CharField(max_length=30);
    direccion=models.CharField(max_length=30);
    telefono=models.CharField(max_length=30);
    sector_productivo=models.CharField(max_length=31);
    fecha_creacion=models.DateField(auto_now_add=True,null=True);

    #metodo para mostrar el nombre en el admin de django
    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    id_usuarios=models.IntegerField(primary_key=True);
    email=models.CharField(max_length=30,unique=True);
    imagen=models.CharField(max_length=30, null=True);
    nombre_usuario=models.CharField(max_length=30,unique=True);
    password=models.CharField(max_length=30);
    rol=models.CharField(max_length=30);
    fecha_creacion=models.DateField(auto_now_add=True,null=True);

    # def __str__(self):
    #     return '%s %s %s %s %s %s %s %s %s' %(
    #         self.id_usuarios, self.email, self.imagen, self.nombre_usuario, self.password, self.rol, self.fecha_creacion)
    
    def __str__(self):
        return self.nombre_usuario

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

    # def __str__(self):
    #     return self.empresa
    
    # def __str__(self):
    #     return '%s %s %s %s %s %s %s %s %s' %(
    #         self.id_empleado, self.nombre, self.apellidos, self.email, self.telefono, self.empresa, self.fecha_creacion, self.id_usuarios,self.id_empresa)

    

class Movimientos (models.Model):#entidad pendiente por completar 
    id_movimientos=models.AutoField(primary_key=True);
    fecha_creacion=models.DateField(auto_now_add=True,null=True);
    concepto=models.CharField(max_length=50, null=True);
    monto=models.FloatField(max_length=10, null=True);
    id_usuarios=models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True);
    tipo=models.CharField(max_length=30, null=True);

    # def __int__(self):
    #     return self.id_movimientos,self.id_usuarios


