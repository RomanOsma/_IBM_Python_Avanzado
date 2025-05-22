from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    """Modelo para extender la información del usuario"""
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=250, blank=True)
    codigo_postal = models.CharField(max_length=20, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f'Perfil de {self.usuario.username}'
