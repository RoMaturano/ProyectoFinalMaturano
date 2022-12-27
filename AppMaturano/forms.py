from django import forms 

class ProductoFormulario(forms.Form):
    nombre=forms.CharField()
    precio=forms.IntegerField()
    fecha_de_ingreso=forms.CharField()

class CompradorFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    direccion=forms.CharField(max_length=40)
    email=forms.CharField(max_length=40)
    
    
class VentasFormulario(forms.Form):
    cantidad_ventas=forms.CharField(max_length=40)
    monto_recaudado=forms.IntegerField()
    fecha_de_venta=forms.CharField(max_length=40)
        