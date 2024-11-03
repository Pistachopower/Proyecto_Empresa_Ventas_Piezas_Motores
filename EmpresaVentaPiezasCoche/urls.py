from django.urls import path, re_path #importamos re_path para usar expresiones regulares
from .import views #aqui le estamos diciendo que de mi carpeta 
#principal me importe las vistas en el fichero view

urlpatterns = [
    path('', views.index, name='index'),
    path('todosclientes', views.mostrar_clientes, name='mostrar_clientes'),
    path('pedidocliente', views.mostrar_pedidocliente, name='mostrar_pedidocliente'),
    path('todoslosdatos', views.mostrartodosdatos, name= 'mostrartodosdatos'),
    path('empleadoatiendecliente/<int:id_empleado>', views.empleadoatiendecliente, name='empleadoatiendecliente'),
    path('pedidospendientespagados/<str:estado>/<str:pag>', views.pedidos_enviados_pagados, name='pedidosPendientesPagados'),
    path('proveedorpiezas/<str:proveedor_p>', views.proveedor_piezamotor, name='mostrar_proveedorpiezamotor'),
    #guia de re_path: index/proveedor/caracter en mayusculas
    re_path(r'^proveedor/(?P<proveedor_nombre>[A-Z])$', views.proveedor_detalle, name='detalle_proveedor'), #captura sólo los caracteres en mayúsculas del proveedor. Se filtra de esa manera porque el nombre del proveedor debe estar en mayusculas
    path('aniomesempleado/<int:anio>/<int:mes>', views.cliente_empleado_anio_mes, name='anioMes_empleado'),
    path('estadopedido/<str:estado_P1>', views.pedidos_enviados_O_entregados, name='pedidos_estados'), 
    path('mediamaxminpedidos', views.mediamaxminpedidos, name='mediamaxminpedidos'), #name= hace referencia al nombre de mi funcion 
    path('clientepedidoinverso/<int:id_cliente>', views.clientepedidoinverso, name='clientepedidoinverso'),
    path('metodopagolimite', views.limite_metodo_pago, name='limite_metodoP'),
    path('piezasMotor_pedidos_nulo', views.piezasMotor_pedidos_nulo, name='piezasMotor_pedidos_nulo')
    
    
]
