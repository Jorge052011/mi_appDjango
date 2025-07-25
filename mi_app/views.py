from django.shortcuts import render
from .models import Producto
# Create your views here.

def hola(request):
    return render(request,"mi_app/hola.html")

def listar_productos(request):
    productos = Producto.objects.all()

    return render(request, "mi_app/lista_de_productos.html", {"productos":productos})