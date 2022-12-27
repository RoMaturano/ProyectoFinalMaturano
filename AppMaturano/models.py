from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=40)
    precio=models.IntegerField()
    fecha_de_ingreso=models.CharField(max_length=40)
    

class Comprador(models.Model):
    nombre=models.CharField(max_length=40)
    direccion=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    
    
class Ventas(models.Model):
    cantidad_ventas=models.CharField(max_length=40)
    monto_recaudado=models.IntegerField()
    fecha_de_venta=models.CharField(max_length=40)
    
    