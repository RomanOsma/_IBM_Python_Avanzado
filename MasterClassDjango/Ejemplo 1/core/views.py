# Create your views here.
from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'core/home.html')

def about(request):
     return render(request, 'core/about.html')

def productos(request):
     return render(request, 'core/productos.html')

def contacto(request):
     return render(request, 'core/contacto.html')


