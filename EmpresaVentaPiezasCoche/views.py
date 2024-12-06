from django.shortcuts import render, redirect
from django.db.models import Q  #Q: para trabajar con condiciones OR
from django.db.models import Avg, Max, Min, Prefetch
from django.views.defaults import page_not_found
from .models import Pedido, MetodoPago, Cliente, Empleado, PiezaMotor_Pedido, PiezaMotor, Proveedor
from .forms import BusquedaAvanzadaProveedorForm

# Importamos las clases necesarias de Django
from django.views.generic.edit import CreateView
from .models import Proveedor  # Asegúrate de que el modelo Proveedor esté importado
from .forms import ProveedorModelForm  # Importamos el formulario que hemos creado
from django.urls import reverse_lazy  # Importamos reverse_lazy para redirigir después de crear el proveedor


#esta sera la vista principal que muestra 
#todas las url o informacion de los modelos
def index(request):
    return render(request, 'index.html')

#una vista que muestra la informacion de todos los clientes
def mostrar_clientes(request):
    clientes= Cliente.objects.all()
    return render(request, 'cliente/todosClientes.html', {'mostrar_clientes':clientes})


#una vista que muestre los pedidos que han realizado los clientes
def mostrar_pedidocliente(request):
    pedidoCliente= Pedido.objects.select_related('cliente').all() #el parametro select_related: es la clave foránea de cliente
    return render(request, 'pedidocliente/pedidoCliente.html', {'mostrar_pedido_cliente':pedidoCliente})

#una vista que me muestre al menos un atributo de cada modelo
def mostrartodosdatos(request):
    #unimos las relaciones many to one desde una relacion de muchoc a muchos (PiezaMotor_Pedido)
    piezamotorpedido_pedido= PiezaMotor_Pedido.objects.select_related(
        #Recordar lo que va despues de __claveForánea es la guia o toponimo para acceder a la otra tabla
        'pedido', # Relación de PiezaMotor_Pedido con Pedido
        'pedido__metodo_pago', # Relación de Pedido con MetodoPago
        'pedido__cliente',  # Relación de pedido a Cliente
        'pedido__cliente__empleado' #Relación de Cliente con Empleado
        )
    
    #ahora tomamos la otra parte de PiezaMotor_Pedido a proveedor
    todoslosdatos= piezamotorpedido_pedido.prefetch_related(
        'pieza', #Relación de PiezaMotor_Pedido con PiezaMotor
        'pieza__proveedor' #Relación de PiezaMotor con Proveedor (ManyToMany)   
        )
    todoslosdatos= todoslosdatos.all()  # Traemos todos los datos
    
    return render(request, 'muestratodos/muestraTodos.html', {'mostrartodosdatos':todoslosdatos})

#una vista que me filtre y muestre los pedidos que están pendiente (Pedido estado=P) y que estén pagados (MetodoPago pago=1)
#requisito: una vista con dos parametros
def pedidos_enviados_pagados(request, estado, pag):
    # Filtramos pedidos con estado "P" y con pag
    pedidosPendientesPagados = Pedido.objects.filter(estado=estado, metodo_pago__pagado__contains=pag).select_related('metodo_pago')
    return render(request, 'pedidos_pendientes_pagados/Pedidos_pendientes_pagados.html', {'pedidosPendientesPagados': pedidosPendientesPagados})


#una vista que me muestre los nombre de los clientes que han sido atendido por un empleado en particular
#requisito: un parametro con un entero
def empleadoatiendecliente(request, id_empleado):
    #empleado__id=: empleado es clave foranea que esta en Cliente y con esta clave puedes acceder a el id de la tabla empleado
    empleadoCliente= Cliente.objects.filter(empleado__id=id_empleado).select_related('empleado')
    return render(request, 'empleadoatiendecliente/Empleadoatiendecliente.html', {'empleadoatiendecliente':empleadoCliente})


#una vista que me muestre las piezas suministradas por un proveedor
#requisito: un parametro con un str
def proveedor_piezamotor(request,proveedor_p):
    # Filtramos las piezas de motor que contienen el nombre del proveedor en su relación. 
    proveedor_piezas = PiezaMotor.objects.filter(proveedor__proveedor__icontains=proveedor_p).prefetch_related('proveedor')
    return render(request, 'proveedor_piezamotor/Proveedorpiezamotor.html', {'mostrar_proveedorpiezamotor': proveedor_piezas,  'proveedor_p': proveedor_p }) # Pasamos el proveedor para mostrarlo en el template


#una vista que filtre a los proveedores por su nombre
#requisito: re_path
def proveedor_detalle(request, proveedor_nombre):
    # Filtramos los proveedores que contienen el nombre especificado que comiencen por mayusculas entre los caracteres A-Z
    proveedores = Proveedor.objects.filter(proveedor__icontains=proveedor_nombre)
    return render(request, 're_path_proveedor/Detalle_proveedor.html', {'proveedores': proveedores, 'proveedor_nombre':proveedor_nombre}) # Pasamos el proveedor_nombre para mostrarlo en el template

#una vista que filtra los clientes basándose en el año y mes de contratación del empleado
#requisito: usando and 
def cliente_empleado_anio_mes(request, anio, mes):
    anioMes_empleado= Cliente.objects.select_related('empleado').filter(empleado__fecha_contratacion__year=anio, empleado__fecha_contratacion__month=mes)
    return render(request, 'clienteEmpleado_anio_mes/ClienteEmpleado_anio_mes.html', {'anioMes_empleado':anioMes_empleado})

#una vista que me muestre los pedidos que estén enviados, pendientes o entregados ordenados por fecha descendente
#requisito or y order by
def pedidos_enviados_O_entregados(request, estado_P1): 
    pedidos_estados= Pedido.objects.filter(Q(estado= estado_P1) | Q(estado='P') | Q(estado='ENTR')).order_by('-fecha_pedido')
    return render(request, 'pedidos_enviados_O_entregados/Pedidos_enviados_O_entregados.html', { 'pedidos_estados': pedidos_estados})

#una vista que me muestre la media de los pedidos, el máximo  y el minimo de pedido
#requisito: aggregate
def mediamaxminpedidos(request):
    #hacemos el calculo con el campo total_importe 
    calculo_pedidos= Pedido.objects.aggregate(Avg('total_importe'), Max('total_importe'), Min('total_importe'))
    
    #luego guardamos en variables las operaciones
    media= calculo_pedidos['total_importe__avg']
    maximo= calculo_pedidos['total_importe__max']
    minimo= calculo_pedidos['total_importe__min']
    
    #devolvemos el resultado en varios diccionarios para mostrar en la template
    return render(request, 'calculospedidos/Calculospedidos.html', {'media':media, 'maximo': maximo, 'minimo':minimo})

#una vista que me muestre cliente el cliente con sus pedidos
#requisito: relacion inversa 
def clientepedidoinverso(request, id_cliente):
    #creamos la relacion reversa importando Prefetch y usando el related_name de la vista cliente llamada: pedido_cliente
    cliente= Cliente.objects.prefetch_related(Prefetch('pedido_cliente')).get(id= id_cliente)
    return render(request, 'clientepedidoinverso/clientepedidoinverso.html', {'clientepedidoinverso':cliente})


#una vista que me muestre dos registros de metodo de pago
#requisito: limit
def limite_metodo_pago(request):
    limite_metodoP=  MetodoPago.objects.all()[:2]
    return render(request, 'limite_metodopago/limite_metodopago.html', {'limite_metodoP': limite_metodoP})
    
#una vista de los pedidos y las piezas que la cantidad es nula
def piezasMotor_pedidos_nulo(request):
	# Prefetch PiezaMotor y Pedido a través de la tabla intermedia PiezaMotor_Pedido
	piezasMotor_pedidos_nulo = PiezaMotor_Pedido.objects.prefetch_related('pieza', 'pedido').filter(cantidad= None)
	return render(request, 'piezasMotor_pedidosnulo/PiezasMotor_pedidos.html', {'piezasMotor_pedidos_nulo': piezasMotor_pedidos_nulo})


#vista de error
def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_400(request, exception=None):
    return render(request, 'errores/400.html', status=400)

def mi_error_403(request, exception=None):
    return render(request, 'errores/403.html', status=403)

def mi_error_500(request):
    return render(request, 'errores/500.html', status=500)




# Definimos una vista basada en clase para crear un nuevo proveedor
class ProveedorCreateView(CreateView):
    model = Proveedor  # Especificamos que esta vista está asociada al modelo Proveedor
    form_class = ProveedorModelForm  # Indicamos que usaremos el formulario ProveedorModelForm para manejar los datos
    template_name = "formularios/crear_proveedor.html"  # Especificamos la plantilla que se usará para renderizar el formulario

    # URL a la que se redirigirá después de que el formulario se haya enviado correctamente
    success_url = reverse_lazy('crear_proveedor')  # Cambia por el nombre de tu vista de lista
    




def proveedor_buscar_avanzado(request):
    if request.method == 'GET':
        formulario = BusquedaAvanzadaProveedorForm(request.GET)
        if formulario.is_valid():
            # Inicializamos la consulta de proveedores
            qs_proveedores = Proveedor.objects.all()
            
            # Obtenemos los filtros
            nombre_proveedor = formulario.cleaned_data.get('nombre_proveedor')
            correo = formulario.cleaned_data.get('correo')
            telefono = formulario.cleaned_data.get('telefono')

            # Filtramos por nombre del proveedor
            if nombre_proveedor:
                qs_proveedores = qs_proveedores.filter(proveedor__icontains=nombre_proveedor)

            # Filtramos por correo
            if correo:
                qs_proveedores = qs_proveedores.filter(correo__icontains=correo)

            # Filtramos por teléfono
            if telefono:
                qs_proveedores = qs_proveedores.filter(telefono__icontains=telefono)

            # Obtenemos los proveedores filtrados
            proveedores = qs_proveedores.all()

            return render(request, 'formularios/busqueda_avanzada.html', {
                "proveedores_mostrar": proveedores,
                "formulario": formulario
            })
    else:
        formulario = BusquedaAvanzadaProveedorForm()

    return render(request, 'formularios/busqueda_avanzada.html', {"formulario": formulario})