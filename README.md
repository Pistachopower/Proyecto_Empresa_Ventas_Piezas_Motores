# Proyecto de Gestión de Pedidos de Piezas de Motor

Este proyecto implementa una base de datos para gestionar pedidos de piezas de motor, con funcionalidades para administrar clientes, empleados, proveedores, métodos de pago, y piezas de motor. El sistema permite realizar consultas avanzadas a través de diferentes vistas y URLs, optimizadas para un rendimiento eficiente en Django.

## Descripción de la Base de Datos

La base de datos incluye las siguientes tablas principales:

1. **Proveedor**: Almacena la información de los proveedores de piezas de motor, como nombre, teléfono, correo y dirección.

2. **PiezaMotor**: Registra cada pieza de motor, incluyendo su nombre, precio, descripción, stock disponible y sus proveedores asociados.

3. **Cliente**: Gestiona los datos de los clientes, como nombre, apellido, correo, dirección y tipo de cliente (particular o empresa).

4. **Empleado**: Contiene la información de los empleados, incluyendo nombre, apellido, cargo y fecha de contratación.

5. **Pedido**: Representa los pedidos realizados por los clientes, incluyendo el cliente asociado, el método de pago, la fecha del pedido, el total importe y el estado (pendiente, enviado, entregado).

6. **MetodoPago**: Define los métodos de pago disponibles, con detalles como nombre, tipo de pago, fecha de creación y estado (pagado o no).

7. **Tablas Intermedias**:
   - **PiezaMotor_Proveedor**: Relaciona las piezas de motor con los proveedores que las suministran.
   - **PiezaMotor_Pedido**: Une las piezas de motor con los pedidos, indicando la cantidad y el precio total de cada pieza en el pedido.

## Vistas

El archivo `views.py` contiene varias vistas para realizar diferentes consultas sobre los datos de la base de datos. A continuación, se describen algunas de las principales:

- **index**: Muestra la página principal.
- **mostrar_clientes**: Lista todos los clientes.
- **mostrar_pedidocliente**: Muestra los pedidos asociados a un cliente específico.
- **mostrartodosdatos**: Muestra todos los datos almacenados en el sistema.
- **empleadoatiendecliente**: Lista los clientes atendidos por un empleado específico.
- **pedidos_enviados_pagados**: Filtra los pedidos que están pendientes o pagados.
- **proveedor_piezamotor**: Muestra las piezas de motor de un proveedor específico.
- **proveedor_detalle**: Detalla la información del proveedor, filtrando los nombres que comienzan con una letra mayúscula.
- **cliente_empleado_anio_mes**: Lista los clientes atendidos por empleados en un año y mes específico.
- **pedidos_enviados_O_entregados**: Filtra los pedidos que están enviados o entregados.
- **mediamaxminpedidos**: Muestra la media, máximo y mínimo de los pedidos.
- **clientepedidoinverso**: Consulta inversa de clientes y pedidos.
- **limite_metodo_pago**: Filtra los métodos de pago que cumplen un límite específico.
- **piezasMotor_pedidos_nulo**: Consulta las piezas de motor con pedidos nulos.

## URLs

El archivo `urls.py` define las rutas para acceder a cada una de las vistas. A continuación, se listan algunas de las rutas principales:

- `/`: Página principal.
- `/todosclientes`: Lista todos los clientes.
- `/pedidocliente`: Muestra los pedidos de un cliente.
- `/todoslosdatos`: Muestra todos los datos.
- `/empleadoatiendecliente/<int:id_empleado>`: Clientes atendidos por un empleado específico.
- `/pedidospendientespagados/<str:estado>/<str:pag>`: Filtra pedidos pendientes y pagados.
- `/proveedorpiezas/<str:proveedor_p>`: Piezas de motor de un proveedor específico.
- `/proveedor/<str:proveedor_nombre>`: Detalle de un proveedor, filtrando por nombre en mayúscula.
- `/aniomesempleado/<int:anio>/<int:mes>`: Clientes atendidos por empleados en un año y mes específicos.
- `/estadopedido/<str:estado_P1>`: Filtra pedidos enviados o entregados.
- `/mediamaxminpedidos`: Muestra media, máximo y mínimo de los pedidos.
- `/clientepedidoinverso/<int:id_cliente>`: Consulta inversa de clientes y pedidos.
- `/metodopagolimite`: Filtra métodos de pago según un límite.
- `/piezasMotor_pedidos_nulo`: Consulta piezas de motor con pedidos nulos.

## Requisitos Cumplidos

## Requisitos Cumplidos

1. **Consultas Complejas**: El proyecto implementa filtros avanzados usando condiciones `AND`, `OR`, `aggregate`, y consultas optimizadas con `select_related` y `prefetch_related`.
2. **Manejo de Relaciones**: Se usan relaciones ManyToMany, ManyToOne y OneToOne entre las tablas para optimizar las consultas.
3. **Páginas de Error Personalizadas**: Se incluyen vistas de errores personalizadas para los códigos de error 400, 403, 404, y 500.
4. **Datos de Prueba**: Se usa un fixture para gestionar datos de prueba en producción.
5. **Vista con Dos Parámetros**: Se implementa una vista que utiliza `re_path` con un entero y un string como parámetros, aplicando filtros `AND`, `OR`, `order by`, `aggregate`, relación inversa, `limit`, y el uso de `None`.


## Diagrama del Modelo Relacional

![Modelo Relacional](ruta/a/tu/imagen.png)

