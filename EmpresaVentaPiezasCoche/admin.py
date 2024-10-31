from django.contrib import admin

from .models import Proveedor,Cliente, PiezaMotor, MetodoPago, Pedido, Empleado, PiezaMotor_Pedido   

admin.site.register(Proveedor)
admin.site.register(PiezaMotor)
admin.site.register(Cliente)
admin.site.register(MetodoPago)
admin.site.register(Pedido)
admin.site.register(Empleado)
admin.site.register(PiezaMotor_Pedido)


