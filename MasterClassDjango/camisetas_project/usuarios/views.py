from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistroUsuarioForm, PerfilForm
from .models import Perfil

def registro(request):
    """Vista para registro de nuevos usuarios"""
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # Crear perfil asociado al usuario
            Perfil.objects.create(usuario=usuario)
            login(request, usuario)
            return redirect('catalogo:inicio')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def perfil(request):
    """Vista para ver y actualizar el perfil del usuario"""
    perfil_usuario = Perfil.objects.get_or_create(usuario=request.user)[0]
    
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil_usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios:perfil')
    else:
        form = PerfilForm(instance=perfil_usuario)
    
    return render(request, 'usuarios/perfil.html', {'form': form})
