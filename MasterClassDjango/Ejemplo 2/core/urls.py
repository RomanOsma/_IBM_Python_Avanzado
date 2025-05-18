from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                # Ruta para la página de inicio
    path('products/', views.products, name='products'),  # Ruta para la página de productos
    path('contact/', views.contact, name='contact'),     # Ruta para el formulario de contacto
    path('users/', views.users, name='users'),           # Ruta para ver usuarios
    path('edit/<int:pk>/', views.user_edit, name='edit_user'),   # Ruta para editar
    path('delete/<int:pk>/', views.user_delete, name='delete_user'),  # Ruta para eliminar
]
