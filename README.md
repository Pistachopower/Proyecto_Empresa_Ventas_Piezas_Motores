# Proyecto_Empresa_Ventas_Piezas_Motores
El siguiente proyecto es de una empresa dedicada a la venta de piezas de coche de alta calidad. Nuestra tienda online ofrece una amplia gama de productos para todas tus necesidades automotrices, garantizando la mejor experiencia de compra y servicio al cliente.

# Descripción del Modelo Entidad-Relación

Este modelo entidad-relación (ER) representa un sistema de gestión de pedidos, empleados, clientes, proveedores y piezas de motor. A continuación, se describen cada uno de los modelos, atributos y parámetros usados en el esquema.

# Descripción del Modelo Entidad-Relación

Este modelo entidad-relación está diseñado para gestionar una plataforma de venta de piezas de coches. En el modelo, se incluyen diversas entidades que representan los principales actores involucrados en el sistema, tales como **Clientes**, **Pedidos**, **Proveedores**, **Piezas de Motor**, entre otros. Además, se establecen las relaciones y cardinalidades necesarias para reflejar la interacción entre estas entidades, permitiendo gestionar de manera eficaz los pedidos, productos, clientes y proveedores.

## Entidades y Atributos

## Proveedor
- **id_proveedor**: Identificador único del proveedor.
- **nombre_proveedor**: Nombre de la empresa o persona que provee las piezas.
- **teléfono**: Número de contacto del proveedor.
- **correo**: Correo electrónico del proveedor.
- **dirección**: Ubicación física del proveedor.

## Proveedor_PiezaMotor
- **id_proveedor**: Identificador del proveedor que suministra la pieza.
- **id_pieza**: Identificador de la pieza suministrada.

## PiezaMotor
- **id_pieza**: Identificador único de la pieza de motor.
- **nombre**: Nombre o descripción de la pieza.
- **precio**: Precio de la pieza.
- **descripción**: Descripción detallada de la pieza.
- **stock_disponible**: Cantidad disponible en inventario.

## Proveedor_Pedido
- **id_proveedor**: Relación con el proveedor que atiende el pedido.
- **id_pedido**: Relación con el pedido específico.

## Pedido
- **id_pedido**: Identificador único del pedido.
- **id_metodo_pago**: Método de pago utilizado para el pedido.
- **id_cliente_pedido**: Cliente que realiza el pedido.
- **fecha_pedido**: Fecha en que se realiza el pedido.
- **total_importe**: Importe total del pedido.
- **estado**: Estado actual del pedido (pendiente, enviado, entregado).

## MétodoPago
- **id_metodo_pago**: Identificador único del método de pago.
- **nombre**: Nombre del método de pago (por ejemplo, tarjeta, PayPal).
- **tipo_pago**: Tipo de método de pago.
- **fecha_Creacion**: Fecha de creación del método de pago.
- **fecha_Ultima_Creacion**: Fecha de la última actualización.

## Cliente
- **id_cliente**: Identificador único del cliente.
- **nombre**: Nombre del cliente.
- **apellido**: Apellido del cliente.
- **correo**: Correo electrónico del cliente.
- **TIPO_CLIENTE**: Especifica si es un cliente particular, empresa, o dirección.

## DirecciónPrincipal
- **id_direccion**: Identificador único de la dirección.
- **id_cliente**: Cliente al que pertenece la dirección.
- **id_Provincia**: Relación con la provincia de la dirección.
- **calle**: Calle de la dirección.
- **provincia**: Provincia de la dirección.
- **código_postal**: Código postal correspondiente.

## Provincia
- **id_Provincia**: Identificador único de la provincia.
- **nombre**: Nombre de la provincia.
- **comunidad**: Comunidad autónoma a la que pertenece la provincia.
- **num_habitantes**: Número de habitantes de la provincia.

## Empleado
- **id_empleado**: Identificador único del empleado.
- **id_empresa_empleado**: Empresa para la que trabaja el empleado.
- **nombre**: Nombre del empleado.
- **apellido**: Apellido del empleado.
- **cargo**: Cargo que ocupa en la empresa.
- **fecha_Contratacion**: Fecha de contratación del empleado.

## Empresa
- **id_empresa**: Identificador único de la empresa.
- **nombre**: Nombre de la empresa.
- **teléfono**: Teléfono de contacto de la empresa.
- **dirección**: Dirección de la sede principal de la empresa.
- **email_contacto**: Correo de contacto.

## Relaciones y Cardinalidades

1. **Proveedor - PiezaMotor (N:M)**:  
   Un proveedor puede suministrar muchas piezas de motor, y una pieza de motor puede ser suministrada por varios proveedores.

2. **PiezaMotor - Pedido (N:M)**:  
   Un pedido puede contener varias piezas de motor, y una pieza de motor puede estar en varios pedidos.

3. **Proveedor - Pedido (N:M)**:  
   Un proveedor puede suministrar piezas para varios pedidos, y un pedido puede requerir productos de diferentes proveedores.

4. **Cliente - Pedido (N:1)**:  
   Un cliente puede realizar muchos pedidos, pero un pedido es realizado por un solo cliente.

5. **MétodoPago - Pedido (N:1)**:  
   Muchos pedidos pueden ser realizados con un mismo método de pago, pero cada pedido utiliza solo un método de pago.

6. **Provincia - DirecciónPrincipal (N:1)**:  
   Muchas direcciones pueden estar ubicadas en una provincia, pero cada dirección solo pertenece a una provincia.

7. **Cliente - DirecciónPrincipal (1:1)**:  
   Cada cliente tiene una dirección principal, y una dirección principal pertenece a un solo cliente.

8. **Empleado - Empresa (N:1)**:  
   Muchos empleados pueden trabajar en una empresa, pero cada empleado trabaja para una sola empresa.

9. **Empresa - Empleado (1:N)**:  
   Una empresa puede emplear a muchos empleados, pero cada empleado trabaja para una sola empresa.

## Justificación de las Relaciones

### Relaciones N:M
- **Proveedor - PiezaMotor**: Esta relación permite modelar que un proveedor puede suministrar diversas piezas de motor, y a su vez, una pieza puede ser provista por distintos proveedores. Esto es esencial en un sistema donde se manejan múltiples opciones de proveedores para optimizar costos o disponibilidad de productos.
  
- **PiezaMotor - Pedido**: La relación muchos a muchos entre estas tablas es necesaria porque un pedido puede incluir varias piezas, y una pieza puede estar asociada a múltiples pedidos diferentes a lo largo del tiempo. Esto refleja la realidad de un sistema de pedidos donde las piezas son productos recurrentes.

- **Proveedor - Pedido**: Es necesario modelar la relación entre proveedores y pedidos de forma N:M porque un pedido puede requerir productos de diferentes proveedores, y un proveedor puede estar asociado con múltiples pedidos, lo que es común en un sistema de logística y distribución.

### Relaciones N:1
- **Cliente - Pedido**: La relación muchos a uno refleja que un cliente puede realizar muchos pedidos, pero cada pedido está asociado únicamente a un cliente. Esto es lógico en términos comerciales donde un pedido tiene un responsable (cliente) definido.

- **MétodoPago - Pedido**: Cada pedido utiliza un solo método de pago, pero un método de pago puede ser utilizado en múltiples pedidos. Esto refleja la realidad de cualquier sistema de ventas donde los clientes pueden utilizar un mismo método para varias transacciones.

- **Provincia - DirecciónPrincipal**: Una dirección está en una sola provincia, pero muchas direcciones pueden estar en la misma provincia. Este diseño permite gestionar las ubicaciones geográficas de manera estructurada y lógica.

- **Empleado - Empresa**: La relación muchos a uno entre empleado y empresa es necesaria porque cada empleado trabaja para una sola empresa, aunque una empresa puede tener varios empleados. Este es un reflejo directo de la estructura organizativa de las empresas.

### Relaciones 1:1
- **Cliente - DirecciónPrincipal**: Cada cliente tiene una única dirección principal, lo que garantiza que haya una correspondencia directa entre los datos de cliente y su dirección principal registrada en el sistema.


# Diagrama ER

![Diagrama ER](ruta/a/tu/imagen.png)


