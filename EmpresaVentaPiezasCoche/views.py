from django.shortcuts import render

#esta sera la vista principal que muestra 
#todas las url o informacion de los modelos
def index(request):
    return render(request, 'index.html')
