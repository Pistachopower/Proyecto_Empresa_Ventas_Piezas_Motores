from django.urls import path
from .import views #aqui le estamos diciendo que de mi carpeta 
#principal me importe las vistas en el fichero view

urlpatterns = [
    path('', views.index, name='index'),
    path('todosclientes', views.mostrar_clientes, name='mostrar_clientes'),
    path('pedidocliente', views.mostrar_pedidocliente, name='mostrar_pedidocliente'),
    path('todoslosdatos', views.mostrartodosdatos, name= 'mostrartodosdatos')
    
]
