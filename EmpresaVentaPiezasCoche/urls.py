from django.urls import path, re_path #importamos re_path para usar expresiones regulares
from .import views #aqui le estamos diciendo que de mi carpeta 
#principal me importe las vistas en el fichero view

#importamos la vista ProveedorCreateView: from .views import ProveedorCreateView
#from .views import proveedor_buscar_avanzado

urlpatterns = [
    path('', views.index, name='index'),
    path('proveedor',views.proveedores_create,name='proveedores_create'),
    path('proveedores',views.proveedores_lista,name='proveedores_lista'), 
    path('proveedor/eliminar/<int:proveedor_id>',views.proveedor_eliminar,name='proveedor_eliminar'),
    #path('proveedores/buscar',views.proveedores_buscar,name='proveedores_buscar'),

 
    
    

]
