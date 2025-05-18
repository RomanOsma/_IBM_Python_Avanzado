from django import forms
from .models import UserProfile

# Formulario basado en el modelo UserProfile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Usamos el modelo que ya definimos
        fields = ['name', 'login', 'password']  # Campos visibles en el formulario

        # Usamos PasswordInput para ocultar el texto en el campo de contraseña
        widgets = {
            'password': forms.PasswordInput()
        }
