from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class RegistroUsuarioForm(UserCreationForm):
    """Formulario para registro de nuevos usuarios"""
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label='Nombre')
    last_name = forms.CharField(required=True, label='Apellidos')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class PerfilForm(forms.ModelForm):
    """Formulario para actualizar el perfil del usuario"""
    class Meta:
        model = Perfil
        fields = ('direccion', 'codigo_postal', 'ciudad')
