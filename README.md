# Proyecto_Empresa_Ventas_Piezas_Motores
El siguiente proyecto es de una empresa dedicada a la venta de piezas de coche de alta calidad. Nuestra tienda online ofrece una amplia gama de productos para todas tus necesidades automotrices, garantizando la mejor experiencia de compra y servicio al cliente.

# Descripción del Modelo Entidad-Relación

Este modelo entidad-relación (ER) representa un sistema de gestión de pedidos, empleados, clientes, proveedores y piezas de motor. A continuación, se describen cada uno de los modelos, atributos y parámetros usados en el esquema.

## Entidades y Atributos

1. **DirecciónPrincipal**
   - **id_direccion**: Identificador único de la dirección.
   - **calle**: Nombre de la calle.
   - **ciudad**: Nombre de la ciudad.
   - **provincia**: Nombre de la provincia.
   - **codigo_postal**: Código postal.
   - **id_empresa_direccion_empresa**: Identificador de la relación con la empresa.

2. **Empresa**
   - **id_empresa**: Identificador único de la empresa.
   - **nombre**: Nombre de la empresa.
   - **telefono**: Número de teléfono de la empresa.

3. **Empleado**
   - **id_empleado**: Identificador único del empleado.
   - **nombre**: Nombre del empleado.
   - **apellido**: Apellido del empleado.
   - **cargo**: Cargo del empleado.

4. **Cliente**
   - **id_cliente**: Identificador único del cliente.
   - **nombre**: Nombre del cliente.
   - **apellido**: Apellido del cliente.
   - **correo**: Correo electrónico del cliente.
   - **empresa**: Nombre de la empresa del cliente.
   - **particular**: Indicador si el cliente es particular.
   - **tipo_cliente**: Tipo de cliente.

5. **Pedido**
   - **id_pedido**: Identificador único del pedido.
   - **fecha_pedido**: Fecha del pedido.
   - **total_importe**: Importe total del pedido.
   - **id_cliente_pedido**: Identificador del cliente que realizó el pedido.
   - **id_metodo_pago**: Identificador del método de pago.
   - **estado**: Estado del pedido (pendiente, enviado, entregado).

6. **MetodoPago**
   - **id_metodo_pago**: Identificador único del método de pago.
   - **nombre**: Nombre del método de pago.
   - **divisa**: Divisa del método de pago.
   - **tipo_pago**: Tipo de pago.

7. **PiezaMotor**
   - **id_pieza**: Identificador único de la pieza.
   - **nombre**: Nombre de la pieza.
   - **precio**: Precio de la pieza.
   - **descripcion**: Descripción de la pieza.
   - **stock_disponible**: Cantidad de stock disponible.
   - **id_pedido_pieza_motor**: Identificador del pedido que contiene la pieza.

8. **Proveedor**
   - **id_proveedor**: Identificador único del proveedor.
   - **nombre_proveedor**: Nombre del proveedor.
   - **telefono**: Número de teléfono del proveedor.
   - **correo**: Correo electrónico del proveedor.
   - **direccion**: Dirección del proveedor.

9. **Provincia**
   - **nombre**: Nombre de la provincia.
   - **comunidad**: Comunidad a la que pertenece la provincia.

## Relaciones

1. **DirecciónPrincipal - Empresa**
   - Relación 1:1 entre DirecciónPrincipal y Empresa.
   - Una empresa tiene una dirección principal.

2. **Empresa - Empleado**
   - Relación 1:N entre Empresa y Empleado.
   - Una empresa tiene muchos empleados.

3. **Empleado - Pedido**
   - Relación N:M entre Empleado y Pedido.
   - Un empleado gestiona muchos pedidos y un pedido puede ser gestionado por muchos empleados.

4. **Cliente - Pedido**
   - Relación 1:N entre Cliente y Pedido.
   - Un cliente puede realizar muchos pedidos.

5. **Pedido - MetodoPago**
   - Relación 1:N entre Pedido y MetodoPago.
   - Un pedido puede tener un método de pago.

6. **Pedido - PiezaMotor**
   - Relación 1:N entre Pedido y PiezaMotor.
   - Un pedido puede contener muchas piezas de motor.

7. **PiezaMotor - Proveedor**
   - Relación N:M entre PiezaMotor y Proveedor.
   - Una pieza de motor puede ser suministrada por muchos proveedores y un proveedor puede suministrar muchas piezas de motor.

8. **Proveedor - Provincia**
   - Relación N:M entre Proveedor y Provincia.
   - Un proveedor puede estar en muchas provincias y una provincia puede tener muchos proveedores.

## Esquema del Modelo Entidad-Relación

El esquema del modelo entidad-relación se muestra en la imagen proporcionada. Este esquema visualiza las entidades, sus atributos y las relaciones entre ellas, proporcionando una representación clara y estructurada del sistema de gestión de pedidos.

