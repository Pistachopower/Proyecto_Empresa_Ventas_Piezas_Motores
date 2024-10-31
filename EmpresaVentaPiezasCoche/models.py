from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.


#tablas independientes
class Proveedor(models.Model):
    proveedor= models.CharField(max_length=100) #los id se ponen a 100 porque puede incrementar los registros
    nombre_proveedor= models.CharField(max_length=100)
    telefono= models.TextField()
    correo= models.CharField(max_length=100, unique=True) #Texto y  único
    direccion= models.TextField()
    


class Cliente(models.Model):
    cliente= models.CharField(max_length=100)
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    correo= models.CharField(max_length=100, unique=True) #Texto y  único
    TIPO_CLIENTES= [('P', 'Particular'),  
                    ('E', 'Empresa')]
    
    #max_length=2: longitud máxima de caracteres de tipos de clientes
    #recuerda que en la bd se guardara con los caracteres P y E
    tipo_clientes= models.CharField(max_length=2,choices=TIPO_CLIENTES)
    direccion=  models.TextField(null=True, blank=True) #puede existir registos de clientes sin correo
    
class MetodoPago(models.Model):
    metodo_pago= models.CharField(max_length=100)
    nombre= models.CharField(max_length=100)
    tipo_pago= models.CharField(max_length=100)
    
    #los atributos fecha_Creacion y fecha_Ultima_Actualizacion  hacen referencia 
    #a registrar cuándo se creo y se actualizó cada metodo de pago
    fecha_creacion= models.DateTimeField(default=timezone.now)
    fecha_ultima_actualizacion= models.DateTimeField(auto_now=True) #se usa este parametro para poder manejar la fecha exacta de que se actualizó algún campo en el modelo MetodoPago
    #nuevo atributo
    pagado = models.BooleanField(default=False) # Valor por defecto si no se proporciona)
    default=False  # Valor por defecto si no se proporciona
    
    
class Pedido(models.Model):
    pedido= models.CharField(max_length=100)
    metodo_pago= models.ForeignKey(MetodoPago, on_delete = models.CASCADE)
    fecha_pedido= models.DateField()
    total_importe= models.IntegerField()
    ESTADO= [('P', 'Pendiente'), #pendiente por modificar 
                    ('ENV', 'Enviado'),
                    ('ENTR', 'Entregado')]
    estado= models.CharField(max_length=4,choices=ESTADO) #se pone en max_length=4 para que agarre los caracteres de ENTR
    metodo_pago = models.ForeignKey(MetodoPago, on_delete = models.CASCADE)
    cliente_pedido= models.ForeignKey(Cliente, on_delete = models.CASCADE, related_name='pedido_cliente')
    

#tablas dependientes
class Empleado(models.Model):
    empleado= models.CharField(max_length=100)
    nombre= models.TextField()
    apellido= models.TextField()
    cargo= models.CharField(max_length=100)
    fecha_contratacion = models.DateField(null=True, blank=True)  # Fecha de contratación
    cliente=  models.ForeignKey(Cliente, on_delete = models.CASCADE)

#tabla intermedia  
class PiezaMotor(models.Model):
    pieza= models.CharField(max_length=100)
    nombre= models.TextField()
    proveedor= models.ManyToManyField(Proveedor)
    pedido= models.ManyToManyField(Pedido, through='PiezaMotor_Pedido')
    precio= models.DecimalField(max_digits=10, decimal_places=2) #se permite 10 digitos en total de los cuales 2 pueden esta en el punto decimal
    descripción= models.TextField()
    stock_disponible= models.IntegerField(null=True, blank=True) #se permite que este campo este vacio
    proveedor= models.ManyToManyField(Proveedor)
    
#tabla intermedia
class PiezaMotor_Pedido(models.Model):
    pieza= models.ForeignKey(PiezaMotor, on_delete=models.CASCADE)
    pedido= models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad= models.IntegerField(null=True, blank=True) #se pone estos parametros para evitar el el error que no pueda ser nulo el valor
    precioTotal= models.FloatField(default=0.0) #se agrega este parametros para evitar error: Internal error: NOT NULL constraint failed
    

