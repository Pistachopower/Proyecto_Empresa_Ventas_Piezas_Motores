from django.urls import path
from .import views #aqui le estamos diciendo que de mi carpeta 
#principal me importe las vistas en el fichero view

urlpatterns = [
    path('', views.index, name='index')
]
