

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm

# Página de inicio
def home(request):
    return render(request, 'home.html')  # Devuelve la plantilla de inicio

# Página de productos (por ahora estática)
def products(request):
    return render(request, 'products.html')  # Devuelve la plantilla de productos

# Página de contacto con formulario para registrar nuevos usuarios
def contact(request):
    if request.method == 'POST':
        # Si el formulario ha sido enviado, se procesa
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la base de datos
            return redirect('users')  # Redirige a la lista de usuarios
    else:
        # Si es una petición GET, se muestra el formulario vacío
        form = UserProfileForm()
    return render(request, 'contact.html', {'form': form})  # Muestra la plantilla con el formulario

# Página para ver todos los usuarios registrados
def users(request):
    user_list = UserProfile.objects.all()  # Consulta todos los usuarios
    return render(request, 'users.html', {'users': user_list})

# Página para editar un usuario existente
def user_edit(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)  # Busca el usuario por su ID o devuelve error 404
    form = UserProfileForm(request.POST or None, instance=user)  # Formulario con los datos del usuario
    if form.is_valid():
        form.save()  # Guarda los cambios
        return redirect('users')
    return render(request, 'contact.html', {'form': form})  # Reutilizamos la plantilla de contacto

# Acción para eliminar un usuario
def user_delete(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    user.delete()  # Borra el usuario
    return redirect('users')
