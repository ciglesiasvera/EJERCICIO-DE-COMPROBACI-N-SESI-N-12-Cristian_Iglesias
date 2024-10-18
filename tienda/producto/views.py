from django.shortcuts import render

# Create your views here.

def insertar_producto(request):
    """Vista para insertar un nuevo producto."""
    return render(request, 'insertar.html')
