from django.shortcuts import render, redirect
from django.db.models import Q  #Q: para trabajar con condiciones OR
from django.db.models import Avg, Max, Min, Prefetch
from django.views.defaults import page_not_found
from .models import Pedido, MetodoPago, Cliente, Empleado, PiezaMotor_Pedido, PiezaMotor, Proveedor
from .forms import ProveedorModelForm


#esta sera la vista principal que muestra 
#todas las url o informacion de los modelos
def index(request):
    return render(request, 'index.html')

def proveedores_create(request):
    if request.method == "POST":
        formulario = ProveedorModelForm(request.POST)
        if formulario.is_valid():
            try:
                # Guarda el libro en la base de datos
                formulario.save()
                return redirect("proveedores_lista")
            except Exception as error:
                print(error)
    else:
        formulario = ProveedorModelForm()
          
    return render(request, 'formularios/Proveedores_create.html',{"proveedores_create":formulario})  



def proveedores_lista(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'formularios/proveedores_lista.html',{"proveedores_lista":proveedores})


def proveedor_eliminar(request,proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    try:
        proveedor.delete()
        #messages.success(request, "Se ha elimnado el libro "+libro.nombre+" correctamente")
    except Exception as error:
        print(error)
    return redirect('proveedores_lista')


"""
def proveedor_buscar(request):
    
    formulario = BusquedaLibroForm(request.GET)
    
    if formulario.is_valid():
        texto = formulario.cleaned_data.get('textoBusqueda')
        libros = Libro.objects.select_related("biblioteca").prefetch_related("autores")
        libros = libros.filter(Q(nombre__contains=texto) | Q(descripcion__contains=texto)).all()
        mensaje_busqueda = "Se buscar por textos que contienen en su nombre o contenido la palabra: "+texto
        return render(request, 'libro/lista_busqueda.html',{"libros_mostrar":libros,"texto_busqueda":mensaje_busqueda})
    
    #me redireccione a la página desde la que hice la búsqueda
    if("HTTP_REFERER" in request.META):
        return redirect(request.META["HTTP_REFERER"])
    else:
        return redirect("index")
"""





#vista de error
def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_400(request, exception=None):
    return render(request, 'errores/400.html', status=400)

def mi_error_403(request, exception=None):
    return render(request, 'errores/403.html', status=403)

def mi_error_500(request):
    return render(request, 'errores/500.html', status=500)



