from django.shortcuts import render
from .models import Pedido, MetodoPago, Cliente, Empleado, PiezaMotor_Pedido


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