# Proyecto_Empresa_Ventas_Piezas_Motores
El siguiente proyecto es de una empresa dedicada a la venta de piezas de coche de alta calidad. Nuestra tienda online ofrece una amplia gama de productos para todas tus necesidades automotrices, garantizando la mejor experiencia de compra y servicio al cliente.

# Descripción del Modelo Entidad-Relación

Este modelo entidad-relación (ER) representa un sistema de gestión de pedidos, empleados, clientes, proveedores y piezas de motor. A continuación, se describen cada uno de los modelos, atributos y parámetros usados en el esquema.

# Descripción del Modelo Entidad-Relación

Este modelo entidad-relación está diseñado para gestionar una plataforma de venta de piezas de coches. En el modelo, se incluyen diversas entidades que representan los principales actores involucrados en el sistema, tales como **Clientes**, **Pedidos**, **Proveedores**, **Piezas de Motor**, entre otros. Además, se establecen las relaciones y cardinalidades necesarias para reflejar la interacción entre estas entidades, permitiendo gestionar de manera eficaz los pedidos, productos, clientes y proveedores.

## Entidades y Atributos

1. **Proveedor**:
   - `id_proveedor`: Identificador único del proveedor.
   - `nombre_proveedor`: Nombre del proveedor.
   - `teléfono`: Número de contacto del proveedor.
   - `correo`: Correo electrónico del proveedor.
   - `dirección`: Dirección física del proveedor.

2. **PiezaMotor**:
   - `id_pieza`: Identificador único de la pieza.
   - `nombre`: Nombre de la pieza de motor.
   - `precio`: Precio de la pieza.
   - `descripción`: Breve descripción de la pieza.
   - `stock_disponible`: Cantidad de stock disponible de la pieza.

3. **Pedido**:
   - `id_pedido`: Identificador único del pedido.
   - `id_metodo_pago`: Referencia al método de pago utilizado en el pedido.
   - `id_cliente_pedido`: Identificador del cliente que realiza el pedido.
   - `fecha_pedido`: Fecha en la que se realizó el pedido.
   - `total_importe`: Importe total del pedido.
   - `estado`: Estado actual del pedido (pendiente, enviado, entregado).

4. **Cliente**:
   - `id_cliente`: Identificador único del cliente.
   - `nombre`: Nombre del cliente.
   - `apellido`: Apellido del cliente.
   - `correo`: Correo electrónico del cliente.
   - `empresa`: Indica si el cliente es una empresa.
   - `particular`: Indica si el cliente es particular.
   - `tipo_cliente`: Clasificación del cliente (particular o empresa).
   - `id_direccion_cliente`: Identificador de la dirección principal del cliente.

5. **MétodoPago**:
   - `id_metodo_pago`: Identificador único del método de pago.
   - `nombre`: Nombre del método de pago.
   - `tipo_pago`: Tipo de método de pago (por ejemplo, tarjeta de crédito, transferencia bancaria, etc.).

6. **Empleado**:
   - `id_empleado`: Identificador único del empleado.
   - `id_empresa_empleado`: Identificador de la empresa a la que pertenece el empleado.
   - `nombre`: Nombre del empleado.
   - `apellido`: Apellido del empleado.
   - `cargo`: Cargo del empleado dentro de la empresa.

7. **Empresa**:
   - `id_empresa`: Identificador único de la empresa.
   - `nombre`: Nombre de la empresa.
   - `teléfono`: Número de contacto de la empresa.
   - `dirección`: Dirección de la empresa.

8. **Provincia**:
   - `id_Provincia`: Identificador único de la provincia.
   - `nombre`: Nombre de la provincia.
   - `comunidad`: Comunidad autónoma a la que pertenece la provincia.
   - `num_habitantes`: Número de habitantes de la provincia.

9. **DireccionPrincipal**:
   - `id_direccion`: Identificador único de la dirección.
   - `id_cliente`: Identificador del cliente al que pertenece la dirección.
   - `id_Provincia`: Provincia donde está ubicada la dirección.
   - `id_Empresa`: Empresa a la que pertenece la dirección (si aplica).
   - `calle`: Calle donde se encuentra la dirección.
   - `provincia`: Provincia de la dirección.
   - `codigo_postal`: Código postal de la dirección.

## Relaciones y Cardinalidades

1. **Proveedor - PiezaMotor (N:M)**:
   - Un proveedor puede proporcionar múltiples piezas de motor, y una pieza de motor puede ser ofrecida por varios proveedores. Por ello, se establece una relación N:M con la tabla intermedia `Proveedor_PiezaMotor`.
   
2. **PiezaMotor - Pedido (N:M)**:
   - Un pedido puede contener varias piezas, y una misma pieza puede estar en múltiples pedidos. Por lo tanto, se implementa una relación N:M con la tabla intermedia `PiezaMotor_Pedido`.
   
3. **Proveedor - Pedido (N:M)**:
   - Se agregó una relación muchos a muchos para reflejar que un pedido puede involucrar productos de múltiples proveedores, y un proveedor puede estar relacionado con varios pedidos a través de la tabla intermedia `Proveedor_Pedido`.

4. **Pedido - Cliente (N:1)**:
   - Cada pedido está asociado a un único cliente, pero un cliente puede realizar múltiples pedidos. Por ello, se establece una relación de N:1.
   
5. **Pedido - MétodoPago (N:1)**:
   - Un pedido puede tener un único método de pago, pero el mismo método puede ser utilizado en múltiples pedidos, por lo que se establece una relación N:1.
   
6. **Cliente - DireccionPrincipal (1:1)**:
   - Cada cliente tiene una única dirección principal asociada, lo cual se refleja mediante una relación 1:1 con `DireccionPrincipal`. Sin embargo, esta relación podría evolucionar a 1:N si un cliente llegara a tener varias direcciones.

7. **Empleado - Empresa (N:1)**:
   - Un empleado pertenece a una única empresa, pero una empresa puede tener múltiples empleados. Esto se refleja con una relación N:1.

## Justificación de las Relaciones

- Las relaciones N:M entre `Proveedor-PiezaMotor`, `PiezaMotor-Pedido`, y `Proveedor-Pedido` son esenciales para capturar la naturaleza multi-asociativa del sistema. Esto asegura que múltiples proveedores puedan surtir las mismas piezas o pedidos, y que los pedidos puedan involucrar productos de múltiples proveedores.
- Las relaciones N:1 para `Cliente-Pedido` y `Pedido-MétodoPago` son consistentes con la lógica de negocio en la que cada cliente realiza un pedido individualmente y cada pedido tiene un método de pago.
- La relación 1:1 entre `Cliente` y `DireccionPrincipal` ayuda a simplificar la gestión de direcciones, garantizando que un cliente solo tenga una dirección principal registrada.

Este diseño asegura flexibilidad y escalabilidad, facilitando el seguimiento de las piezas, proveedores, pedidos y clientes en la plataforma de venta.


