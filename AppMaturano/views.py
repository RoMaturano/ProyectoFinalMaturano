from django.shortcuts import render
from django.http import HttpResponse
from AppMaturano.models import *
from django.core import serializers
from AppMaturano.forms import *


# Create your views here.
def buscar(request):
    if request.GET["nombre"]:
       nombre_buscado=request.GET["nombre"]
       productos_todos = Producto.objects.filter(nombre=nombre_buscado)
       return render(request,"AppMaturano/resultadobusqueda.html", {"nombre":nombre_buscado, "precio":productos_todos})
    else:
        respuesta = "No has enviado ningun dato."
    return HttpResponse(respuesta)

def buscarVen(request):
    if request.GET["fecha_de_venta"]:
       fecha_buscada=request.GET["fecha_de_venta"]
       fechas_todas = Ventas.objects.filter(fecha_de_venta=fecha_buscada)
       return render(request,"AppMaturano/reultadobusquedaV.html", {"fecha_de_venta":fecha_buscada, "monto_recaudado":fechas_todas})
    else:
        respuesta = "No has enviado ningun dato de alguna venta."
    return HttpResponse(respuesta)

def buscarCom(request):
    if request.GET["nombre"]:
       comprador_buscado=request.GET["nombre"]
       compradores_todos = Comprador.objects.filter(nombre=comprador_buscado)
       return render(request,"AppMaturano/resultadobusquedaC.html", {"nombre":comprador_buscado, "direccion":compradores_todos, "email" :compradores_todos })
    else:
        respuesta = "No has enviado ningun dato de algun comprador."
    return HttpResponse(respuesta)

def buscarproducto(request):
    return render(request,"AppMaturano/busquedaProducto.html")

def buscarventas(request):
    return render(request,"AppMaturano/busquedaVentas.html")

def buscarcompradores(request):
    return render(request,"AppMaturano/busquedaComprador.html")



def inicio(request):
    return render(request,"AppMaturano/inicio.html")



def productosApi (request):
    productos_todos = Producto.objects.all()
    
    return HttpResponse(serializers.serialize('json',productos_todos))


def carrito (request):
    if request.method == "POST":
 
            miFormulario = ProductoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data
                  print(informacion)

                  productoos = Producto(nombre=informacion["nombre"], precio=informacion["precio"], fecha_de_ingreso=informacion["fecha_de_ingreso"])

                  productoos.save()

                  return render(request, "AppMaturano/inicio.html")
    else:
        miFormulario = ProductoFormulario()
 
    return render(request, "AppMaturano/carrito.html", {"miFormulario": miFormulario})


def compradores (request):
    if request.method == "POST":
 
            miFormulariocomprador = CompradorFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulariocomprador)
            
            if miFormulariocomprador.is_valid:

                  informacion = miFormulariocomprador.cleaned_data
                  print(informacion)

                  compradooor = Comprador (nombre=informacion["nombre"], direccion=informacion["direccion"], email=["email"])

                  compradooor.save()

                  return render(request, "AppMaturano/inicio.html")
    else:
        miFormulariocomprador = CompradorFormulario()
 
    return render(request, "AppMaturano/comprador.html", {"miFormulariocomprador": miFormulariocomprador})
    
    
def ventas (request):
    if request.method == "POST":
 
            miFormulariovendedor = VentasFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulariovendedor)
            
            if miFormulariovendedor.is_valid:

                  informacion = miFormulariovendedor.cleaned_data
                  print(informacion)

                  ventaas = Ventas(cantidad_ventas=informacion["cantidad_ventas"], monto_recaudado=informacion["monto_recaudado"], fecha_de_venta=informacion["fecha_de_venta"])

                  ventaas.save()

                  return render(request, "AppMaturano/inicio.html")
              
    else:
        miFormulariovendedor  = VentasFormulario()
 
    return render(request, "AppMaturano/ventas.html", {"miFormulariovendedor": miFormulariovendedor})
    
    
def leer_productos(request):
    producto_all = Producto.objects.all()
    return HttpResponse(serializers.serialize("json", producto_all))
    
def crear_producto(request):
    pro = Producto(nombre="ProductoVario", precio = 25000, fecha_de_ingreso= "14/05/2020")
    pro.save()
    return HttpResponse(f"Producto {pro.nombre} ha sido creado")
    
def editar_producto(request):
    nombre_consulta= "ProductoVario"
    nombre= "NuevoProductoVario"
    Producto.objects.filter(nombre=nombre).update(nombre_consulta = nombre)
    return HttpResponse(f"Producto {nombre_consulta} ha sido actualizado")
    
def eliminar_producto(request):
    nombre_nuevo="nombrenuevoahsidocreado"
    pro = Producto.objects.get(nombre=nombre_nuevo)
    pro.delete()
    return HttpResponse(f"Producto {nombre_nuevo} ha sido eliminado")



def leer_ventas(request):
    ventas_all = Ventas.objects.all()
    return HttpResponse(serializers.serialize("json", ventas_all))
    
def crear_ventas(request):
    ven = ventas(fecha_de_ingreso="05/11/2022", cantidad_ventas = 25,  monto_recaudado = 150000)
    ven.save()
    return HttpResponse(f"Producto {ven.fecha_de_ingreso} ha sido creado")
    
def editar_ventas(request):
    ventas_consulta= "05/11/2022"
    fecha_de_ingreso= "10/11/2022"
    Ventas.objects.filter(fecha_de_ingreso= fecha_de_ingreso).update(ventas_consulta= fecha_de_ingreso)
    return HttpResponse(f"venta {ventas_consulta} ha sido actualizado")
    
def eliminar_producto(request):
    venta_nueva="14/11/2022"
    ven = Ventas.objects.get(fecha_de_ingreso=venta_nueva)
    ven.delete()
    return HttpResponse(f"Venta {venta_nueva} ha sido eliminada")



def leer_comprador(request):
    comprador_all = Comprador.objects.all()
    return HttpResponse(serializers.serialize("json", comprador_all))
    
def crear_comprador(request):
    pro = Comprador(nombre="comprador FFF", direccion = "juen b justo 2000", email= "FFF@gmail.com")
    pro.save()
    return HttpResponse(f"Producto {pro.nombre} ha sido creado")
    
def editar_comprador(request):
    nombre_consulta= "comprador FFF"
    nombre="Nuevocomprador LLL"
    Comprador.objects.filter(nombre=nombre).update(nombre_consulta = nombre)
    return HttpResponse(f"Comprador {nombre_consulta} ha sido actualizado")
    
def eliminar_comprador(request):
    nombre_nuevo="NOMCOMPRADORNUEVO"
    pro = Comprador.objects.get(nombre=nombre_nuevo)
    pro.delete()
    return HttpResponse(f"Comprador {nombre_nuevo} ha sido eliminado")
   
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.detail import DetailView

class Productolist(ListView):
    model= Producto
    template_name = "AppMaturano/producto_list.html"

class Ventalist(ListView):
    model= Ventas
    template_name = "AppMaturano/ventas_list.html"
    
class Compradorlist(ListView):
    model= Comprador
    template_name = "AppMaturano/comprador_list.html"
    
class Productocreate(CreateView):
    model= Producto
    fields = '__all__'
    success_url = '/AppMaturano/producto/list/'
    
class Ventacreate(CreateView):
    model= Ventas
    fields = '__all__'
    success_url = '/AppMaturano/ventas/list/'
    
class Compradorcreate(CreateView):
    model= Comprador
    fields = '__all__'
    success_url = '/AppMaturano/comprador/list/'
    
class Productoedit(UpdateView):
    model= Producto
    fields = '__all__'
    success_url = '/AppMaturano/producto/list/'
    
class Ventaedit(UpdateView):
    model= Ventas
    fields = '__all__'
    success_url = '/AppMaturano/ventas/list/'
    
class Compradoredit(UpdateView):
    model= Comprador
    fields = '__all__'
    success_url = '/AppMaturano/comprador/list/'
    
class Productodetail(DetailView):
    model= Producto
    template_name = "AppMaturano/productos_detail.html"
    
class Ventadetail(DetailView):
    model= Ventas
    template_name = "AppMaturano/ventas_detail.html"
    
class Compradordetail(DetailView):
    model= Comprador
    template_name = "AppMaturano/comprador_detail.html"

class Productodelete(DeleteView):
    model= Producto
   
    success_url = '/AppMaturano/producto/list/'
    
class Ventadelete(DeleteView):
    model= Ventas
   
    success_url = '/AppMaturano/ventas/list/'
    
class Compradordelete(DeleteView):
    model= Comprador
   
    success_url = '/AppMaturano/comprador/list/'