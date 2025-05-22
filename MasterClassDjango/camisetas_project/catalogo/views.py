from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
from carrito.forms import AgregarProductoForm

def inicio(request):
    """Vista para la página de inicio"""
    productos = Producto.objects.filter(disponible=True)[:8]
    return render(request, 'catalogo/inicio.html', {
        'productos': productos,
    })

def lista_productos(request, categoria_slug=None):
    """Vista para listar productos, opcionalmente filtrados por categoría"""
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(disponible=True)
    
    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        productos = productos.filter(categoria=categoria)
    
    return render(request, 'catalogo/lista_productos.html', {
        'categoria': categoria,
        'categorias': categorias,
        'productos': productos,
    })

def detalle_producto(request, id, slug):
    """Vista para mostrar el detalle de un producto"""
    producto = get_object_or_404(Producto, id=id, slug=slug, disponible=True)
    form_carrito = AgregarProductoForm()
    
    return render(request, 'catalogo/detalle_producto.html', {
        'producto': producto,
        'form_carrito': form_carrito,
    })
