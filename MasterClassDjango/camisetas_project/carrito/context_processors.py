def carrito(request):
    """Context processor para hacer el carrito disponible en todas las plantillas"""
    from .carrito import Carrito
    return {'carrito': Carrito(request)}
