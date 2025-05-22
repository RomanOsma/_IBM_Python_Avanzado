from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.detalle_carrito, name='detalle_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('checkout/', views.checkout, name='checkout'),
]
