from django.urls import path
from AppMaturano import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    
    path('productosApi/', views.productosApi),
    path('carrito/', views.carrito,name="carrito"),
    path('comprador/', views.compradores,name="comprador"),
    path('ventas/', views.ventas,name="ventas"),
    path('busquedaProducto/', views.buscarproducto),
    path('busquedaVentas/', views.buscarventas),
    path('busquedaCompradores/', views.buscarcompradores),
    path('buscar/', views.buscar),
    path('buscarV/', views.buscarVen),
    path('buscarC/', views.buscarCom),
    path('leerproducto/', views.leer_productos),
    path('crearproducto/', views.crear_producto),
    path('editarproducto/', views.editar_producto),
    path('eliminarproducto/', views.eliminar_producto),
    path('producto/list/', views.Productolist.as_view(), name= "Lista"),
    path('ventas/list/', views.Ventalist.as_view(), name= "Listaventa"),
    path('comprador/list/', views.Compradorlist.as_view(), name= "Listacomprador"),
    path('producto/create/', views.Productocreate.as_view(), name = "New"),
    path('Venta/create/', views.Ventacreate.as_view(), name = "Newventa"),
    path('comprador/create/', views.Compradorcreate.as_view(), name = "Newcomprador"),
    path('producto/edit/<pk>', views.Productoedit.as_view(), name = "Edit"),
    path('venta/edit/<pk>', views.Ventaedit.as_view(), name = "Editventa"),
    path('comprador/edit/<pk>', views.Compradoredit.as_view(), name = "Editcomprador"),
    path('producto/detail/<pk>', views.Productodetail.as_view(), name = "Detail"),
    path('venta/detail/<pk>', views.Ventadetail.as_view(), name = "Detailventa"),
    path('comprador/detail/<pk>', views.Compradordetail.as_view(), name = "Detailcomprador"),
    path('producto/delete/<pk>', views.Productodelete.as_view(), name = "Delete"),
    path('venta/delete/<pk>', views.Ventadelete.as_view(), name = "Deleteventa"),
    path('comprador/delete/<pk>', views.Compradordelete.as_view(), name = "Deletecomprador")
]