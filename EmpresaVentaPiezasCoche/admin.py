from django.contrib import admin



from .models import Proveedor, Cliente, MetodoPago, Empresa, Provincia,Pedido,Empleado, DireccionPrincipal, PiezaMotor, PiezaMotor_Pedido 

admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(MetodoPago)
admin.site.register(Empresa)
admin.site.register(Provincia)
admin.site.register(Pedido)
admin.site.register(Empleado)
admin.site.register(DireccionPrincipal)
admin.site.register(PiezaMotor)
admin.site.register(PiezaMotor_Pedido)


