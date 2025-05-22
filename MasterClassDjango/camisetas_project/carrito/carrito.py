from decimal import Decimal
from django.conf import settings
from catalogo.models import Producto

class Carrito:
    """Clase para gestionar el carrito de compras"""
    
    def __init__(self, request):
        """Inicializar el carrito"""
        self.session = request.session
        carrito = self.session.get(settings.CART_SESSION_ID)
        if not carrito:
            # Guardar un carrito vacío en la sesión
            carrito = self.session[settings.CART_SESSION_ID] = {}
        self.carrito = carrito
    
    def agregar(self, producto, cantidad=1, actualizar_cantidad=False):
        """Agregar un producto al carrito o actualizar su cantidad"""
        producto_id = str(producto.id)
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {'cantidad': 0,
                                         'precio': str(producto.precio_final())}
        if actualizar_cantidad:
            self.carrito[producto_id]['cantidad'] = cantidad
        else:
            self.carrito[producto_id]['cantidad'] += cantidad
        self.guardar()
    
    def guardar(self):
        """Marcar la sesión como modificada para asegurar que se guarde"""
        self.session.modified = True
    
    def eliminar(self, producto):
        """Eliminar un producto del carrito"""
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar()
    
    def __iter__(self):
        """Iterar sobre los elementos del carrito y obtener los productos de la base de datos"""
        producto_ids = self.carrito.keys()
        # Obtener los objetos producto y añadirlos al carrito
        productos = Producto.objects.filter(id__in=producto_ids)
        
        carrito = self.carrito.copy()
        for producto in productos:
            carrito[str(producto.id)]['producto'] = producto
        
        for item in carrito.values():
            item['precio'] = Decimal(item['precio'])
            item['precio_total'] = item['precio'] * item['cantidad']
            yield item
    
    def __len__(self):
        """Contar todos los items en el carrito"""
        return sum(item['cantidad'] for item in self.carrito.values())
    
    def get_precio_total(self):
        """Calcular el costo total del carrito"""
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carrito.values())
    
    def limpiar(self):
        """Eliminar el carrito de la sesión"""
        del self.session[settings.CART_SESSION_ID]
        self.guardar()
