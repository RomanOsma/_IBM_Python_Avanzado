from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalogo.models import Producto
from .carrito import Carrito
from .forms import AgregarProductoForm

@require_POST
def agregar_al_carrito(request, producto_id):
    """Vista para agregar productos al carrito"""
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    form = AgregarProductoForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        carrito.agregar(producto=producto,
                        cantidad=cd['cantidad'],
                        actualizar_cantidad=cd['actualizar'])
    
    return redirect('carrito:detalle_carrito')

def eliminar_del_carrito(request, producto_id):
    """Vista para eliminar productos del carrito"""
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.eliminar(producto)
    return redirect('carrito:detalle_carrito')

def detalle_carrito(request):
    """Vista para mostrar el detalle del carrito"""
    carrito = Carrito(request)
    return render(request, 'carrito/detalle.html', {'carrito': carrito})

def checkout(request):
    """Vista para el proceso de checkout"""
    carrito = Carrito(request)
    if request.method == 'POST':
        # Simulación de procesamiento de pago
        # En un caso real, aquí se integraría con una pasarela de pago
        carrito.limpiar()
        return render(request, 'carrito/pago_completado.html')
    
    return render(request, 'carrito/checkout.html', {'carrito': carrito})
