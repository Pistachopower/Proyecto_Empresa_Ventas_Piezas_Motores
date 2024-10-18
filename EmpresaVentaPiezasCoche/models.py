from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

#FALTA AGREGRAR EN LOS ATRIBUTOS PARAMETROS(null, blank, db_column, primary_key)


#tablas independientes
class Proveedor(models.Model):
    id_proveedor= models.CharField(max_length=100) #los id se ponen a 100 porque puede incrementar los registros
    nombre_proveedor= models.CharField(max_length=100)
    telefono= models.TextField()
    correo= models.CharField(max_length=100, unique=True) #Texto y  único
    direccion= models.TextField()
    
class Cliente(models.Model):
    id_cliente= models.CharField(max_length=100)
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    correo= models.CharField(max_length=100, unique=True) #Texto y  único
    TIPO_CLIENTES= [('P', 'Particular'), #pendiente por modificar 
                    ('E', 'Empresa')]
    
    #max_length=2: longitud máxima de caracteres de tipos de clientes
    #recuerda que en la bd se guardara con los caracteres P y E
    tipo_Clientes= models.CharField(max_length=2,choices=TIPO_CLIENTES)
    direccion=  models.TextField(null=True, blank=True) #puede existir registos de clientes sin correo
    
class MetodoPago(models.Model):
    id_metodo_pago= models.CharField(max_length=100)
    nombre= models.CharField(max_length=100)
    tipo_pago= models.CharField(max_length=100)
    
    #los atributos fecha_Creacion y fecha_Ultima_Actualizacion  hacen referencia 
    #a registrar cuándo se creo y se actualizó cada metodo de pago
    fecha_Creacion= models.DateTimeField(default=timezone.now)
    fecha_Ultima_Actualizacion= models.DateTimeField(auto_now=True) #se usa este parametro para poder manejar la fecha exacta de que se actualizó algún campo en el modelo MetodoPago
    
class Empresa(models.Model): 
    id_empresa= models.CharField(max_length=100)
    nombre= models.TextField()
    telefono= models.TextField()
    direccion= models.TextField()
    email_contacto = models.EmailField(null=True, blank=True) #con este tipo de dato y parametro controlamos que se cumplan que los correos deban tener @ y patrones de correo
    
class Provincia(models.Model):
    id_Provincia= models.CharField(max_length=100)
    nombre= models.TextField()
    comunidad= models.CharField(max_length=100)
    num_habitantes= models.IntegerField()
    codigo_postal = models.CharField(max_length=10, null=True, blank=True) 

class Pedido(models.Model):
    id_pedido= models.CharField(max_length=100)
    id_metodo_pago= models.ForeignKey(MetodoPago, on_delete = models.CASCADE)
    id_cliente_pedido= models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha_pedido= models.DateField()
    total_importe= models.IntegerField()
    ESTADO= [('P', 'Pendiente'), #pendiente por modificar 
                    ('ENV', 'Enviado'),
                    ('ENTR', 'Entregado')]
    estado= models.CharField(max_length=4,choices=ESTADO) #se pone en max_length=4 para que agarre los caracteres de ENTR


#tablas dependientes
class Empleado(models.Model):
    id_empleado= models.CharField(max_length=100)
    id_empresa_empleado= models.ForeignKey(Empresa, on_delete = models.CASCADE)
    nombre= models.TextField()
    apellido= models.TextField()
    cargo= models.CharField(max_length=100)
    fecha_contratacion = models.DateField(null=True, blank=True)  # Fecha de contratación
    
class DireccionPrincipal(models.Model):
    id_direccion= models.CharField(max_length=100)
    id_cliente= models.ForeignKey(Cliente, on_delete = models.CASCADE)
    id_Provincia= models.ForeignKey(Provincia, on_delete = models.CASCADE)
    id_Empresa= models.ForeignKey(Empresa, on_delete = models.CASCADE)
    calle= models.TextField()
    provincia= models.CharField(max_length=100)
    codigo_postal= models.IntegerField()
    numero = models.CharField(max_length=10, null=True, blank=True)  # Número de la dirección
    
class PiezaMotor(models.Model):
    id_pieza= models.CharField(max_length=100)
    proveedor= models.ManyToManyField(Proveedor)
    id_pedido= models.ManyToManyField(Pedido, through='PiezaMotor_Pedido')
    nombre= models.TextField()
    precio= models.DecimalField(max_digits=10, decimal_places=2) #se permite 10 digitos en total de los cuales 2 pueden esta en el punto decimal
    descripción= models.TextField()
    stock_disponible= models.IntegerField(null=True, blank=True) #se permite que este campo este vacio
    
#tabla intermedia
class PiezaMotor_Pedido(models.Model):
    id_pieza= models.ForeignKey(PiezaMotor, on_delete=models.CASCADE)
    id_pedido= models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad= models.IntegerField()
    precioTotal= models.FloatField()