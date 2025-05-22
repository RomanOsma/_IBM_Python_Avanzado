from django.db import models
from django.urls import reverse
from decimal import Decimal

class Categoria(models.Model):
    """Modelo para las categorías de productos"""
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        ordering = ('nombre',)
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('catalogo:productos_por_categoria', args=[self.slug])

class Producto(models.Model):
    """Modelo para los productos de la tienda"""
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    imagen = models.ImageField(upload_to='productos/%Y/%m/%d', blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.IntegerField(default=0)  # Porcentaje de descuento
    stock = models.PositiveIntegerField(default=10)
    disponible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('nombre',)
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        indexes = [
            models.Index(fields=['id', 'slug'])
        ]
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('catalogo:detalle_producto', args=[self.id, self.slug])
    
    def precio_final(self):
        """Calcula el precio final después del descuento"""
        if self.descuento:
            # Convertir el descuento a Decimal para evitar errores de tipo
            descuento_decimal = Decimal(str(self.descuento / 100))
            return round(self.precio * (Decimal('1.0') - descuento_decimal), 2)
        return self.precio
