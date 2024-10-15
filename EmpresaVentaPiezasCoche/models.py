from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

#FALTA AGREGRAR EN LOS ATRIBUTOS PARAMETROS(null, blank, choices, db_column, primary_key)


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
    tipo_cliente= [('P', 'Particular'), #pendiente por modificar 
                    ('E', 'Empresa')]
    direccion=  models.TextField()
    
class MetodoPago(models.Model):
    id_metodo_pago= models.CharField(max_length=100)
    nombre= models.CharField(max_length=100)
    tipo_pago= models.CharField(max_length=100)
    
class Empresa(models.Model): 
    id_empresa= models.CharField(max_length=100)
    nombre= models.TextField()
    telefono= models.TextField()
    direccion= models.TextField()
    
class Provincia(models.Model):
    id_Provincia= models.CharField(max_length=100)
    nombre= models.TextField()
    comunidad= models.CharField(max_length=100)
    num_habitantes= models.IntegerField()

class Pedido(models.Model):
    id_pedido= models.CharField(max_length=100)
    id_metodo_pago= models.ForeignKey(MetodoPago, on_delete = models.CASCADE)
    id_cliente_pedido= models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha_pedido= models.DateField()
    total_importe= models.IntegerField()
    estado= [('P', 'Pendiente'), #pendiente por modificar 
                    ('ENV', 'Enviado'),
                    ('ENTR', 'Entregado')]
    

#tablas dependientes
class Empleado(models.Model):
    id_empleado= models.CharField(max_length=100)
    id_empresa_empleado= models.ForeignKey(Empresa, on_delete = models.CASCADE)
    nombre= models.TextField()
    apellido= models.TextField()
    cargo= models.CharField(max_length=100)
    
class DireccionPrincipal(models.Model):
    id_direccion= models.CharField(max_length=100)
    id_cliente= models.ForeignKey(Cliente, on_delete = models.CASCADE)
    id_Provincia= models.ForeignKey(Provincia, on_delete = models.CASCADE)
    id_Empresa= models.ForeignKey(Empresa, on_delete = models.CASCADE)
    calle= models.TextField()
    provincia= models.CharField(max_length=100)
    codigo_postal= models.IntegerField()
    
class PiezaMotor(models.Model):
    id_pieza= models.CharField(max_length=100)
    proveedor= models.ManyToManyField(Proveedor)
    id_pedido= models.ManyToManyField(Pedido, through='PiezaMotor_Pedido')
    nombre= models.TextField()
    precio= models.FloatField()
    descripción= models.TextField()
    stock_disponible= models.IntegerField()
    
#tabla intermedia
class PiezaMotor_Pedido(models.Model):
    id_pieza= models.ForeignKey(PiezaMotor, on_delete=models.CASCADE)
    id_pedido= models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad= models.IntegerField()
    precioTotal= models.FloatField()