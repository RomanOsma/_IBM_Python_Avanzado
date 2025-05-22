from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('categoria/<slug:categoria_slug>/', views.lista_productos, name='productos_por_categoria'),
    path('producto/<int:id>/<slug:slug>/', views.detalle_producto, name='detalle_producto'),
]
