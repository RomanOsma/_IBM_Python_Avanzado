# Curso Completo de Manejo de Archivos en Python

Este repositorio contiene un único archivo Python (`curso_archivos.py`) diseñado como material de estudio completo para aprender a trabajar con archivos en Python. Está pensado para estudiantes que prefieren tener toda la información, ejemplos y ejercicios en un solo lugar.

## Contenido del Curso

El archivo `curso_archivos.py` cubre los siguientes temas:

1.  **Conceptos Básicos:**
    * Abrir archivos (`open()`)
    * Modos de apertura (`'r'`, `'w'`, `'a'`, `'x'`, `'+'`, `'b'`, `'t'`)
    * Lectura de archivos (`read()`, `readline()`, `readlines()`, iteración)
    * Escritura en archivos (`write()`)
    * La importancia de cerrar archivos (`close()`)
    * Uso del gestor de contexto `with` (recomendado)
    * Manejo de la posición del cursor (`seek()`, `tell()`)
    * Manejo de errores comunes (`FileNotFoundError`, `PermissionError`, `IOError`)

2.  **Operaciones Avanzadas y Formatos:**
    * Manejo de rutas y directorios con `os.path` (tradicional)
    * Manejo de rutas y directorios con `pathlib` (moderno, orientado a objetos)
        * Crear, listar, renombrar, eliminar archivos y directorios.
    * Trabajo con archivos **CSV** (Valores Separados por Comas):
        * `csv.reader` y `csv.writer` (listas)
        * `csv.DictReader` y `csv.DictWriter` (diccionarios)
    * Trabajo con archivos **JSON** (JavaScript Object Notation):
        * `json.dump()` (serializar Python a JSON)
        * `json.load()` (deserializar JSON a Python)
    * **Serialización de Objetos** con `pickle`:
        * Guardar objetos Python complejos (`pickle.dump()`)
        * Cargar objetos Python desde archivos (`pickle.load()`)
        * Advertencias de seguridad.
    * Trabajo directo con **Archivos Binarios** (`'rb'`, `'wb'`).

3.  **Proyecto Práctico: Sistema de Gestión de Inventario:**
    * Implementación de un sistema simple basado en consola.
    * Uso de clases (`Producto`, `ServicioInventario`, `SistemaInventarioUI`).
    * Persistencia de datos utilizando un archivo **CSV**.
    * Operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre el inventario.
    * Generación de reportes en archivo de texto.

4.  **Ejercicios Propuestos:**
    * Una serie de ejercicios prácticos para reforzar los conceptos aprendidos.
    * Incluye **soluciones comentadas** directamente en el código.

## Cómo Usar el Archivo

1.  **Descarga:** Guarda el código como un archivo llamado `curso_archivos.py`.
2.  **Ejecución:**
    * Abre una terminal o consola.
    * Navega hasta el directorio donde guardaste el archivo.
    * Ejecuta el script usando Python 3: `python curso_archivos.py`
3.  **Interacción:**
    * Por defecto, el script ejecutará directamente el **Sistema de Gestión de Inventario** (Sección 3). Puedes interactuar con él a través del menú en consola.
    * **Para ver las demostraciones de las otras secciones:**
        * Abre el archivo `curso_archivos.py` en un editor de texto.
        * Ve al final del archivo, dentro del bloque `if __name__ == "__main__":`.
        * **Descomenta** (quita el `#` al inicio) las llamadas a las funciones de las secciones que quieras ejecutar (ej. `seccion_conceptos_basicos()`, `seccion_operaciones_avanzadas()`, `seccion_ejercicios()`).
        * Puedes comentar (`#`) la ejecución del sistema de inventario si solo quieres ver las demos o los ejercicios.
        * Guarda los cambios y vuelve a ejecutar el script: `python curso_archivos.py`
4.  **Estudio:**
    * Lee los comentarios y docstrings en el código para entender qué hace cada parte.
    * Modifica los ejemplos para experimentar.
    * Intenta resolver los ejercicios antes de mirar las soluciones.

## Notas

* El script creará algunos directorios (`ejemplos_basicos`, `ejemplos_avanzados`, `ejercicios_resueltos`) y archivos (`.txt`, `.csv`, `.json`, `.pkl`, `.bin`) en el mismo directorio donde se ejecute.
* El Sistema de Inventario guarda sus datos en `inventario.csv`.
* El código incluye una sección comentada al final para limpiar automáticamente los archivos y directorios creados (usar con precaución).
* Se asume el uso de **Python 3.6** o superior (debido al uso de f-strings y `pathlib`).
* Se recomienda usar `encoding='utf-8'` siempre que se trabaje con archivos de texto para asegurar la compatibilidad con diferentes caracteres.