# Tienda de Camisetas de Fútbol - Proyecto Django

Este proyecto es una aplicación web desarrollada con Django que simula una tienda online de camisetas de fútbol, inspirada en el diseño de futbolfactory.es. Está diseñada como un ejercicio educativo para alumnos de un curso básico de Django.

## Características

- Catálogo de productos con categorías
- Sistema de autenticación de usuarios
- Carrito de compra
- Simulación de pasarela de pago
- Diseño responsivo
- Interfaz visual inspirada en futbolfactory.es

## Requisitos

- Python 3.8 o superior
- Django 5.2.1
- Pillow (para el manejo de imágenes)

## Instalación

1. Clona este repositorio o descomprime el archivo zip en tu directorio de trabajo.

2. Crea un entorno virtual (opcional pero recomendado):
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```
   pip install django pillow
   ```

4. Aplica las migraciones para crear la base de datos:
   ```
   python manage.py makemigrations catalogo usuarios carrito
   python manage.py migrate
   ```

5. Crea un superusuario para acceder al panel de administración:
   ```
   python manage.py createsuperuser
   ```

6. Inicia el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

7. Accede a la aplicación en tu navegador: http://127.0.0.1:8000/

## Estructura del Proyecto

- `tienda_futbol/`: Configuración principal del proyecto Django
- `catalogo/`: Aplicación para gestionar el catálogo de productos
- `usuarios/`: Aplicación para la gestión de usuarios y perfiles
- `carrito/`: Aplicación para el carrito de compra y proceso de checkout
- `static/`: Archivos estáticos (CSS, JavaScript, imágenes)
- `media/`: Archivos subidos por los usuarios (imágenes de productos)
- `templates/`: Plantillas HTML organizadas por aplicación

## Uso Educativo

Este proyecto está diseñado para que los alumnos puedan:

1. Entender la estructura básica de un proyecto Django
2. Aprender sobre modelos, vistas y plantillas
3. Implementar autenticación de usuarios
4. Trabajar con formularios y validación de datos
5. Gestionar sesiones para el carrito de compra
6. Integrar archivos estáticos y diseño responsivo

## Personalización

Para añadir nuevos productos:

1. Accede al panel de administración: http://127.0.0.1:8000/admin/
2. Inicia sesión con el superusuario creado anteriormente
3. Crea categorías y productos con sus respectivas imágenes

## Notas para el Instructor

- La aplicación utiliza SQLite como base de datos para simplificar la configuración
- La pasarela de pago es una simulación y no procesa pagos reales
- Las imágenes y recursos visuales están inspirados en futbolfactory.es con fines educativos
- El código está comentado para facilitar la comprensión por parte de los alumnos

## Licencia

Este proyecto es solo para uso educativo y no debe utilizarse en entornos de producción sin las debidas modificaciones de seguridad y optimización.
