
# Create your models here.
from django.db import models

# Modelo que representa un usuario simple para nuestro ejercicio
class UserProfile(models.Model):
    name = models.CharField(max_length=100)        # Campo para el nombre del usuario
    login = models.CharField(max_length=100, unique=True)  # Campo único para el nombre de usuario
    password = models.CharField(max_length=100)     # Contraseña (en texto plano solo para práctica)

    def __str__(self):
        return self.name  # Cómo se mostrará el usuario en el panel de administración o en consultas
