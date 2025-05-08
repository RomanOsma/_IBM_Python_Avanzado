#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curso Completo de Manejo de Archivos en Python
=============================================

Este archivo único sirve como material de estudio completo para aprender
a trabajar con archivos en Python. Incluye:
- Conceptos básicos: Abrir, leer, escribir, cerrar archivos.
- Modos de apertura y el uso de 'with'.
- Operaciones avanzadas: Manejo de rutas (os.path y pathlib), directorios.
- Trabajo con formatos específicos: CSV, JSON.
- Serialización de objetos con Pickle.
- Manejo de errores comunes.
- Un proyecto práctico: Sistema de gestión de inventario simple.
- Ejercicios propuestos con soluciones comentadas.

Ideal para estudiantes que necesiten una referencia completa en un solo lugar.

Autor: Tu Asistente AI (Basado en tu solicitud)
Fecha: 20 de Abril de 2025
"""

import os
import csv
import json
import pickle
import sys
from datetime import datetime
from pathlib import Path # Alternativa moderna a os.path

# =============================================================================
# DEFINICIONES DE CLASES (Movidas fuera de las funciones para evitar errores)
# =============================================================================

class Persona:
    """
    Clase simple para demostrar la serialización con Pickle.
    """
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def __str__(self):
        return f"Persona(Nombre: {self.nombre}, Edad: {self.edad}, Profesión: {self.profesion})"

class Producto:
    """
    Representa un producto en el sistema de inventario.

    Attributes:
        id_producto (int): Identificador único del producto.
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        cantidad (int): Cantidad disponible en inventario.
    """
    # Variable de clase para llevar la cuenta del último ID asignado.
    # Se actualizará al cargar desde el archivo para evitar colisiones.
    _contador_productos = 0

    def __init__(self, nombre='', precio=0.0, cantidad=0, id_producto=None):
        """
        Inicializa un nuevo producto. Si no se provee id_producto,
        se genera uno nuevo automáticamente.

        Args:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            cantidad (int): Cantidad disponible.
            id_producto (int, optional): ID existente (útil al cargar desde archivo).
        """
        if id_producto is None:
            Producto._contador_productos += 1
            self.id_producto = Producto._contador_productos
        else:
            self.id_producto = int(id_producto)
            # Aseguramos que el contador esté al día con los IDs cargados
            if self.id_producto > Producto._contador_productos:
                Producto._contador_productos = self.id_producto

        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def __str__(self):
        """Devuelve una representación en string del producto."""
        return (f"Producto [ID: {self.id_producto:03d}] - {self.nombre:<15} - "
                f"Precio: ${self.precio:7.2f} - Stock: {self.cantidad:3d}")

    def formato_csv(self):
        """Devuelve los datos del producto como una lista para CSV."""
        return [self.id_producto, self.nombre, self.precio, self.cantidad]

    @staticmethod
    def encabezados_csv():
        """Devuelve los encabezados para el archivo CSV."""
        return ['ID', 'Nombre', 'Precio', 'Cantidad']


# =============================================================================
# SECCIÓN 1: CONCEPTOS BÁSICOS DEL MANEJO DE ARCHIVOS
# =============================================================================

def seccion_conceptos_basicos():
    """
    Muestra y explica los conceptos básicos del manejo de archivos en Python.

    Esta función ejecuta ejemplos que ilustran cómo abrir, leer, escribir y
    cerrar archivos utilizando diferentes métodos y modos de apertura,
    incluyendo el manejo básico de errores.
    """
    print("\n" + "="*70)
    print("SECCIÓN 1: CONCEPTOS BÁSICOS DEL MANEJO DE ARCHIVOS")
    print("="*70)

    # Directorio para guardar los archivos de ejemplo de esta sección
    dir_ejemplos_basicos = "ejemplos_basicos"
    os.makedirs(dir_ejemplos_basicos, exist_ok=True) # Crea el directorio si no existe

    # ---------------------------------------------------------------------------
    # 1.1 Creación y escritura básica de archivos - Método tradicional
    # ---------------------------------------------------------------------------
    print("\n1.1 Creación y escritura básica - Método tradicional (open/close)")
    print("-"*70)

    nombre_archivo = os.path.join(dir_ejemplos_basicos, 'ejemplo1_tradicional.txt')
    print(f"Intentando crear y escribir en: {nombre_archivo}")

    try:
        # Abrimos el archivo en modo escritura ('w')
        # 'w' = write: Crea un archivo nuevo (o sobrescribe si existe).
        # encoding='utf-8' es crucial para compatibilidad con caracteres especiales (acentos, etc.)
        archivo = open(nombre_archivo, 'w', encoding='utf-8')

        # Escribimos texto en el archivo
        archivo.write('Línea 1: ¡Hola, mundo!\n')
        archivo.write('Línea 2: Este es un ejemplo usando open() y close().\n')
        archivo.write('Línea 3: Es importante cerrar el archivo manualmente.\n')

        # IMPORTANTE: Debemos cerrar el archivo para guardar los cambios y liberar recursos.
        archivo.close()
        print(f"Archivo '{os.path.basename(nombre_archivo)}' creado y cerrado exitosamente.")

    except IOError as e:
        print(f"Error de E/S al intentar escribir en {nombre_archivo}: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    # Leemos y mostramos el contenido del archivo recién creado (método tradicional)
    print("\nContenido del archivo creado (lectura tradicional):")
    try:
        archivo_lectura = open(nombre_archivo, 'r', encoding='utf-8')
        contenido = archivo_lectura.read()
        archivo_lectura.close()
        print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
    except IOError as e:
        print(f"Error de E/S al leer {nombre_archivo}: {e}")

    # ---------------------------------------------------------------------------
    # 1.2 Uso del bloque 'with' - Forma recomendada y segura
    # ---------------------------------------------------------------------------
    print("\n1.2 Uso del bloque 'with' - Forma recomendada (cierre automático)")
    print("-"*70)

    nombre_archivo = os.path.join(dir_ejemplos_basicos, 'ejemplo2_with.txt')
    print(f"Creando y escribiendo en: {nombre_archivo} usando 'with'")

    try:
        # El bloque 'with' garantiza que el archivo se cierre automáticamente,
        # incluso si ocurren errores dentro del bloque. Es la forma idiomática en Python.
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write('Línea 1: Usando el bloque with.\n')
            archivo.write('Línea 2: ¡El archivo se cierra solo!\n')
            archivo.write('Línea 3: Mucho más seguro y limpio.\n')
            # No necesitamos llamar a archivo.close()

        print(f"Archivo '{os.path.basename(nombre_archivo)}' creado exitosamente con 'with'.")

        # Lectura usando también el bloque 'with'
        print("\nContenido del archivo (lectura con 'with'):")
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print(contenido)

    except IOError as e:
        print(f"Error de E/S con 'with' en {nombre_archivo}: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado con 'with': {e}")

    # ---------------------------------------------------------------------------
    # 1.3 Modos de apertura de archivos (Resumen)
    # ---------------------------------------------------------------------------
    print("\n1.3 Modos de apertura de archivos (Resumen)")
    print("-"*70)
    print("Python ofrece varios modos para abrir archivos con `open(ruta, modo)`:")
    print("  'r'  - Read (Lectura): Abre un archivo para lectura. Error si no existe. (Predeterminado)")
    print("  'w'  - Write (Escritura): Crea un archivo nuevo para escritura. Sobrescribe si existe.")
    print("  'a'  - Append (Anexar): Abre un archivo para añadir contenido al final. Crea si no existe.")
    print("  'x'  - Exclusive creation (Creación exclusiva): Crea un archivo nuevo. Falla si ya existe.")
    print("  'b'  - Binary mode (Modo binario): Para archivos no textuales (imágenes, ejecutables). Se combina: 'rb', 'wb', 'ab', 'xb'.")
    print("  't'  - Text mode (Modo texto): Para archivos de texto. (Predeterminado). Se combina: 'rt', 'wt', 'at', 'xt'.")
    print("  '+'  - Update (Actualización): Permite lectura y escritura. Se combina: 'r+', 'w+', 'a+'.")
    print("  `encoding='utf-8'` : Muy recomendado para modo texto para manejar caracteres internacionales.")

    # ---------------------------------------------------------------------------
    # 1.4 Modo exclusivo ('x') - Evita sobrescribir accidentalmente
    # ---------------------------------------------------------------------------
    print("\n1.4 Modo exclusivo ('x')")
    print("-"*70)

    nombre_archivo_exclusivo = os.path.join(dir_ejemplos_basicos, 'ejemplo3_exclusivo.txt')

    # Primer intento: Debería funcionar si el archivo no existe
    try:
        with open(nombre_archivo_exclusivo, 'x', encoding='utf-8') as archivo:
            archivo.write('Este archivo se creó en modo exclusivo.\n')
        print(f"Archivo '{os.path.basename(nombre_archivo_exclusivo)}' creado exitosamente en modo 'x'.")
    except FileExistsError:
        print(f"El archivo '{os.path.basename(nombre_archivo_exclusivo)}' ya existe. El modo 'x' previene la sobrescritura.")
    except IOError as e:
        print(f"Error de E/S al intentar crear en modo 'x': {e}")

    # Segundo intento: Debería fallar porque el archivo ahora existe
    try:
        with open(nombre_archivo_exclusivo, 'x', encoding='utf-8') as archivo:
            archivo.write('Esto no debería escribirse.\n')
    except FileExistsError:
        print(f"Confirmado: El archivo '{os.path.basename(nombre_archivo_exclusivo)}' ya existe. El segundo intento con 'x' falló como se esperaba.")
    except IOError as e:
        print(f"Error de E/S en el segundo intento con 'x': {e}")

    # ---------------------------------------------------------------------------
    # 1.5 Modo anexar ('a') - Añadir al final del archivo
    # ---------------------------------------------------------------------------
    print("\n1.5 Modo anexar ('a')")
    print("-"*70)

    nombre_archivo_anexar = os.path.join(dir_ejemplos_basicos, 'ejemplo2_with.txt') # Reutilizamos este archivo

    print(f"Anexando contenido al archivo: {os.path.basename(nombre_archivo_anexar)}")
    try:
        with open(nombre_archivo_anexar, 'a', encoding='utf-8') as archivo:
            archivo.write('\n--- Contenido Anexado ---\n')
            archivo.write(f'Línea anexada el: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
            archivo.write('El modo "a" es útil para logs o añadir datos sin borrar lo anterior.\n')

        print("Contenido anexado exitosamente.")

        # Mostramos el contenido actualizado
        print("\nContenido actualizado del archivo:")
        with open(nombre_archivo_anexar, 'r', encoding='utf-8') as archivo:
            print(archivo.read())
    except FileNotFoundError:
         print(f"Error: El archivo {nombre_archivo_anexar} no se encontró para anexar.")
    except IOError as e:
        print(f"Error de E/S al anexar a {nombre_archivo_anexar}: {e}")

    # ---------------------------------------------------------------------------
    # 1.6 Métodos de lectura de archivos
    # ---------------------------------------------------------------------------
    print("\n1.6 Métodos de lectura de archivos")
    print("-"*70)

    nombre_archivo_lectura = os.path.join(dir_ejemplos_basicos, 'ejemplo_lectura.txt')

    # Creamos un archivo de ejemplo con varias líneas
    try:
        with open(nombre_archivo_lectura, 'w', encoding='utf-8') as f:
            f.write("Primera línea.\n")
            f.write("Segunda línea del archivo.\n")
            f.write("Tercera línea, un poco más larga.\n")
            f.write("Cuarta línea final.\n")
        print(f"Archivo '{os.path.basename(nombre_archivo_lectura)}' para ejemplos de lectura creado.")
    except IOError as e:
         print(f"Error creando archivo de lectura: {e}")
         return # Salir si no se puede crear el archivo

    # 1.6.1 Método read(): Lee todo el contenido en una sola cadena
    print("\n1.6.1 Método read(): Lee todo el contenido")
    try:
        with open(nombre_archivo_lectura, 'r', encoding='utf-8') as archivo:
            contenido_total = archivo.read()
            print("--- Contenido completo (read()) ---")
            print(contenido_total)
            print(f"Tipo de dato devuelto por read(): {type(contenido_total)}")
    except Exception as e: print(f"Error en read(): {e}")

    # 1.6.2 Método readline(): Lee una línea a la vez (incluyendo el '\n')
    print("\n1.6.2 Método readline(): Lee una línea a la vez")
    try:
        with open(nombre_archivo_lectura, 'r', encoding='utf-8') as archivo:
            print("--- Leyendo línea por línea (readline()) ---")
            linea1 = archivo.readline()
            print(f"Línea 1: {linea1.strip()} (Longitud original: {len(linea1)})") # strip() quita espacios/saltos al inicio/final
            linea2 = archivo.readline()
            print(f"Línea 2: {linea2.strip()} (Longitud original: {len(linea2)})")
            linea_vacia = archivo.readline(0) # Leer 0 bytes devuelve cadena vacía
            print(f"Leer 0 bytes con readline(): '{linea_vacia}'")
            linea3 = archivo.readline()
            print(f"Línea 3: {linea3.strip()} (Longitud original: {len(linea3)})")
    except Exception as e: print(f"Error en readline(): {e}")

    # 1.6.3 Método readlines(): Lee todas las líneas y las devuelve como una lista de cadenas
    print("\n1.6.3 Método readlines(): Lee todas las líneas en una lista")
    try:
        with open(nombre_archivo_lectura, 'r', encoding='utf-8') as archivo:
            lista_lineas = archivo.readlines()
            print("--- Contenido como lista (readlines()) ---")
            print(lista_lineas)
            print(f"Tipo de dato devuelto por readlines(): {type(lista_lineas)}")
            print(f"Número de líneas leídas: {len(lista_lineas)}")
            print("Accediendo a la segunda línea (índice 1):", lista_lineas[1].strip())
    except Exception as e: print(f"Error en readlines(): {e}")

    # 1.6.4 Iteración directa sobre el archivo (Forma eficiente y recomendada para leer línea por línea)
    print("\n1.6.4 Iteración directa sobre el archivo (recomendado para línea por línea)")
    try:
        with open(nombre_archivo_lectura, 'r', encoding='utf-8') as archivo:
            print("--- Iterando directamente sobre el objeto archivo ---")
            for i, linea in enumerate(archivo, 1):
                print(f"Línea {i} (iteración): {linea.strip()}")
            # Al salir del bucle, el archivo está al final. Intentar leer más no dará error,
            # simplemente no devolverá nada.
            mas_lineas = archivo.readline()
            print(f"Intento de leer más después de iterar: '{mas_lineas}' (vacío como se esperaba)")
    except Exception as e: print(f"Error en iteración directa: {e}")

    # ---------------------------------------------------------------------------
    # 1.7 Manejo de la posición del cursor (puntero) en archivos
    # ---------------------------------------------------------------------------
    print("\n1.7 Manejo de la posición del cursor (seek, tell)")
    print("-"*70)

    nombre_archivo_cursor = os.path.join(dir_ejemplos_basicos, 'ejemplo_cursor.txt')

    try:
        # Creamos un archivo para el ejemplo
        with open(nombre_archivo_cursor, 'w+', encoding='utf-8') as archivo: # w+ para escribir y luego leer
            archivo.write("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\n")
            archivo.write("abcdefghijklmnopqrstuvwxyz\n")
            print(f"Archivo '{os.path.basename(nombre_archivo_cursor)}' creado para demo de cursor.")

            # Empezamos desde el principio (aunque 'w+' nos deja al final, lo movemos)
            archivo.seek(0) # Mueve el cursor al byte 0 (inicio del archivo)
            print(f"Posición actual tras seek(0): {archivo.tell()}") # tell() devuelve la posición actual

            # Leemos los primeros 5 caracteres (bytes en modo texto con UTF-8 pueden variar)
            datos = archivo.read(5)
            print(f"Leídos los primeros 5 caracteres: '{datos}'")
            print(f"Posición actual del cursor después de leer 5: {archivo.tell()}")

            # Leemos los siguientes 10 caracteres
            datos = archivo.read(10)
            print(f"Leídos los siguientes 10 caracteres: '{datos}'")
            print(f"Posición actual del cursor: {archivo.tell()}")

            # Mover el cursor 5 bytes hacia adelante desde la posición actual
            # seek(offset, whence): whence=0 (inicio), 1 (actual), 2 (final)
            archivo.seek(5, 1)
            print(f"Cursor movido 5 bytes adelante desde la posición actual ({archivo.tell()})")

            # Leer desde la nueva posición
            datos = archivo.read(5)
            print(f"Leídos 5 caracteres desde la nueva posición: '{datos}'")

            # Mover el cursor al inicio de la segunda línea (posición 37: 36 + '\n')
            # (Nota: La longitud de '\n' puede variar entre OS, pero suele ser 1 o 2 bytes. UTF-8 complica esto)
            # Calcularemos la posición buscando el primer '\n'
            archivo.seek(0) # Volver al inicio
            primera_linea = archivo.readline()
            pos_segunda_linea = archivo.tell()
            print(f"Posición calculada del inicio de la segunda línea: {pos_segunda_linea}")
            archivo.seek(pos_segunda_linea)
            segunda_linea_leida = archivo.readline()
            print(f"Leyendo desde la posición {pos_segunda_linea}: '{segunda_linea_leida.strip()}'")

            # Mover el cursor 10 bytes antes del final del archivo
            archivo.seek(-10, 2)
            print(f"Cursor movido a 10 bytes antes del final ({archivo.tell()})")
            datos_finales = archivo.read()
            print(f"Leyendo los últimos 10 bytes (aprox): '{datos_finales.strip()}'")

    except FileNotFoundError:
         print(f"Error: El archivo {nombre_archivo_cursor} no se encontró.")
    except IOError as e:
        print(f"Error de E/S con seek/tell en {nombre_archivo_cursor}: {e}")

    # ---------------------------------------------------------------------------
    # 1.8 Manejo de errores comunes
    # ---------------------------------------------------------------------------
    print("\n1.8 Manejo de errores comunes (FileNotFoundError, PermissionError)")
    print("-"*70)

    # Intentar leer un archivo que no existe
    archivo_inexistente = "archivo_que_no_existe_seguro.txt"
    try:
        with open(archivo_inexistente, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Error controlado: El archivo '{archivo_inexistente}' no se encontró (FileNotFoundError).")
    except Exception as e:
        print(f"Otro error al intentar leer '{archivo_inexistente}': {e}")

    # Intentar escribir en un directorio (simulación de falta de permisos o tipo incorrecto)
    # (Este ejemplo puede variar mucho dependiendo del sistema operativo y permisos)
    # En lugar de crear un archivo protegido, intentaremos escribir en un directorio existente.
    directorio_actual = "."
    try:
        # Intentar abrir un directorio como si fuera un archivo para escritura suele dar error
        with open(directorio_actual, 'w') as f:
            f.write("Esto no debería funcionar.")
    except PermissionError:
        # En Linux/macOS es más probable PermissionError
        print(f"Error controlado: No se puede escribir en '{directorio_actual}' (PermissionError).")
    except IsADirectoryError:
        # En algunos sistemas puede dar IsADirectoryError
        print(f"Error controlado: '{directorio_actual}' es un directorio, no se puede abrir para escribir (IsADirectoryError).")
    except IOError as e:
         # IOError es una clase base para errores de E/S
         print(f"Error controlado de E/S al intentar escribir en '{directorio_actual}': {e}")
    except Exception as e:
        print(f"Otro error inesperado al intentar escribir en '{directorio_actual}': {e}")

    print("\nFin de la Sección 1.")


# =============================================================================
# SECCIÓN 2: OPERACIONES AVANZADAS Y FORMATOS DE ARCHIVO
# =============================================================================

def seccion_operaciones_avanzadas():
    """
    Demuestra operaciones más avanzadas: manipulación de rutas, directorios,
    archivos CSV, JSON, Pickle y archivos binarios. Introduce pathlib.
    """
    print("\n" + "="*70)
    print("SECCIÓN 2: OPERACIONES AVANZADAS Y FORMATOS DE ARCHIVO")
    print("="*70)

    # Directorio para ejemplos avanzados
    dir_ejemplos_avanzados = "ejemplos_avanzados"
    os.makedirs(dir_ejemplos_avanzados, exist_ok=True)

    # ---------------------------------------------------------------------------
    # 2.1 Manejo de rutas con el módulo os.path (Forma tradicional)
    # ---------------------------------------------------------------------------
    print("\n2.1 Manejo de rutas con os.path (Tradicional)")
    print("-"*70)

    # Usaremos un archivo de la sección anterior como ejemplo
    archivo_ejemplo_path = os.path.join("ejemplos_basicos", 'ejemplo1_tradicional.txt')

    if os.path.exists(archivo_ejemplo_path):
        print(f"Analizando ruta: '{archivo_ejemplo_path}'")
        print(f"  ¿Existe?           : {os.path.exists(archivo_ejemplo_path)}")
        print(f"  ¿Es archivo?       : {os.path.isfile(archivo_ejemplo_path)}")
        print(f"  ¿Es directorio?    : {os.path.isdir(archivo_ejemplo_path)}")
        print(f"  Ruta absoluta      : {os.path.abspath(archivo_ejemplo_path)}")
        print(f"  Directorio padre   : {os.path.dirname(archivo_ejemplo_path)}")
        print(f"  Nombre base        : {os.path.basename(archivo_ejemplo_path)}")
        print(f"  Separar extensión  : {os.path.splitext(archivo_ejemplo_path)}") # Devuelve (ruta_sin_ext, extension)
        print(f"  Tamaño (bytes)     : {os.path.getsize(archivo_ejemplo_path)}")
        # Unir partes de ruta de forma segura (independiente del OS)
        ruta_construida = os.path.join("directorio", "subdirectorio", "archivo.txt")
        print(f"  Ruta construida    : {ruta_construida}")
    else:
        print(f"El archivo de ejemplo '{archivo_ejemplo_path}' no se encontró para el análisis de os.path.")

    # ---------------------------------------------------------------------------
    # 2.2 Manejo de rutas con el módulo pathlib (Forma moderna y orientada a objetos)
    # ---------------------------------------------------------------------------
    print("\n2.2 Manejo de rutas con pathlib (Moderno, OO)")
    print("-"*70)

    # Crear un objeto Path
    path_obj = Path("ejemplos_basicos") / "ejemplo2_with.txt" # Usa / para unir rutas

    if path_obj.exists():
        print(f"Analizando ruta (Path object): '{path_obj}'")
        print(f"  ¿Existe?           : {path_obj.exists()}")
        print(f"  ¿Es archivo?       : {path_obj.is_file()}")
        print(f"  ¿Es directorio?    : {path_obj.is_dir()}")
        print(f"  Ruta absoluta      : {path_obj.resolve()}") # Equivalente a abspath
        print(f"  Directorio padre   : {path_obj.parent}")
        print(f"  Nombre base        : {path_obj.name}")
        print(f"  Nombre sin extensión: {path_obj.stem}")
        print(f"  Extensión          : {path_obj.suffix}")
        print(f"  Tamaño (bytes)     : {path_obj.stat().st_size}") # stat() da más info

        # Leer/Escribir texto directamente desde el objeto Path (¡muy conveniente!)
        try:
            contenido_pathlib = path_obj.read_text(encoding='utf-8')
            print(f"\n  Contenido leído con pathlib:\n{contenido_pathlib[:50]}...") # Muestra primeros 50 chars
            # Escribir (sobrescribe)
            # path_obj.write_text("Nuevo contenido con pathlib", encoding='utf-8')
        except Exception as e:
            print(f"Error leyendo/escribiendo con pathlib: {e}")
    else:
        print(f"El archivo de ejemplo '{path_obj}' no se encontró para el análisis de pathlib.")

    # ---------------------------------------------------------------------------
    # 2.3 Operaciones con directorios (os y pathlib)
    # ---------------------------------------------------------------------------
    print("\n2.3 Operaciones con directorios")
    print("-"*70)

    # Crear un directorio
    nuevo_directorio_os = os.path.join(dir_ejemplos_avanzados, "subdir_os")
    nuevo_directorio_pathlib = Path(dir_ejemplos_avanzados) / "subdir_pathlib"

    try:
        os.makedirs(nuevo_directorio_os, exist_ok=True) # Crea directorios padres si no existen
        print(f"Directorio creado (o ya existía) con os: '{nuevo_directorio_os}'")
        nuevo_directorio_pathlib.mkdir(parents=True, exist_ok=True) # Equivalente con pathlib
        print(f"Directorio creado (o ya existía) con pathlib: '{nuevo_directorio_pathlib}'")
    except OSError as e:
        print(f"Error al crear directorios: {e}")

    # Listar contenido de un directorio
    print(f"\nListando contenido de '{dir_ejemplos_avanzados}' (usando os.listdir):")
    try:
        for item in os.listdir(dir_ejemplos_avanzados):
            ruta_item = os.path.join(dir_ejemplos_avanzados, item)
            tipo = "DIR" if os.path.isdir(ruta_item) else "FILE"
            print(f"  - {item} ({tipo})")
    except FileNotFoundError:
        print(f"  Directorio '{dir_ejemplos_avanzados}' no encontrado.")

    print(f"\nListando contenido de '{dir_ejemplos_avanzados}' (usando pathlib):")
    try:
        path_dir_avanzado = Path(dir_ejemplos_avanzados)
        for item in path_dir_avanzado.iterdir(): # iterdir() devuelve objetos Path
             tipo = "DIR" if item.is_dir() else "FILE"
             print(f"  - {item.name} ({tipo})")
    except FileNotFoundError:
        print(f"  Directorio '{dir_ejemplos_avanzados}' no encontrado.")

    # Renombrar y eliminar (usaremos pathlib por brevedad)
    try:
        path_a_renombrar = Path(dir_ejemplos_avanzados) / "a_renombrar.txt"
        path_renombrado = Path(dir_ejemplos_avanzados) / "renombrado.txt"
        path_a_eliminar = Path(dir_ejemplos_avanzados) / "a_eliminar.txt"

        path_a_renombrar.write_text("Archivo para renombrar", encoding='utf-8')
        path_a_eliminar.write_text("Archivo para eliminar", encoding='utf-8')
        print(f"\nArchivos creados: '{path_a_renombrar.name}', '{path_a_eliminar.name}'")

        path_a_renombrar.rename(path_renombrado)
        print(f"Archivo renombrado a: '{path_renombrado.name}'")

        path_a_eliminar.unlink() # unlink() para eliminar archivos
        print(f"Archivo eliminado: '{path_a_eliminar.name}'")

        # Eliminar directorios (deben estar vacíos)
        # subdir_os_path = Path(nuevo_directorio_os)
        # if subdir_os_path.exists():
        #     subdir_os_path.rmdir()
        #     print(f"Directorio eliminado: '{subdir_os_path.name}'")

    except Exception as e:
        print(f"Error durante renombrado/eliminación: {e}")

    # ---------------------------------------------------------------------------
    # 2.4 Archivo CSV (Valores Separados por Comas) - Básico y con DictReader/Writer
    # ---------------------------------------------------------------------------
    print("\n2.4 Trabajando con archivos CSV")
    print("-"*70)

    nombre_archivo_csv = Path(dir_ejemplos_avanzados) / 'datos_personas.csv'

    # Datos de ejemplo
    datos_lista = [
        ['Nombre', 'Edad', 'Ciudad'],
        ['Ana', '28', 'Madrid'],
        ['Carlos', '35', 'Barcelona'],
        ['Elena', '42', 'Valencia']
    ]
    datos_dict = [
        {'Nombre': 'David', 'Edad': '31', 'Ciudad': 'Sevilla'},
        {'Nombre': 'Laura', 'Edad': '25', 'Ciudad': 'Bilbao'},
        {'Nombre': 'Pedro', 'Edad': '50', 'Ciudad': 'Zaragoza'}
    ]

    # 2.4.1 Escritura básica con csv.writer (listas)
    print("2.4.1 Escribiendo CSV con csv.writer (listas)...")
    try:
        # newline='' es importante para evitar dobles saltos de línea en algunos OS
        with nombre_archivo_csv.open('w', newline='', encoding='utf-8') as f_csv:
            escritor_csv = csv.writer(f_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # Escribir todas las filas de la lista
            escritor_csv.writerows(datos_lista)
            # También se puede fila por fila: escritor_csv.writerow(['Juan', '22', 'Málaga'])
        print(f"Archivo CSV '{nombre_archivo_csv.name}' creado/sobrescrito con datos iniciales.")
    except IOError as e:
        print(f"Error escribiendo CSV básico: {e}")

    # 2.4.2 Lectura básica con csv.reader (listas)
    print("\n2.4.2 Leyendo CSV con csv.reader (listas)...")
    try:
        with nombre_archivo_csv.open('r', encoding='utf-8') as f_csv:
            lector_csv = csv.reader(f_csv)
            print("Contenido leído:")
            for i, fila in enumerate(lector_csv):
                if i == 0:
                    print(f"  Encabezados: {', '.join(fila)}")
                else:
                    print(f"  Fila {i}: {', '.join(fila)}")
    except FileNotFoundError:
        print(f"Error: Archivo CSV '{nombre_archivo_csv.name}' no encontrado para lectura.")
    except Exception as e:
        print(f"Error leyendo CSV básico: {e}")

    # 2.4.3 Escritura con csv.DictWriter (diccionarios) - Añade al archivo existente
    print("\n2.4.3 Escribiendo (anexando) CSV con csv.DictWriter (diccionarios)...")
    try:
        # 'a' para anexar. Necesitamos especificar los nombres de campo (fieldnames)
        fieldnames = datos_dict[0].keys() # Obtenemos los nombres de las claves del primer dict
        with nombre_archivo_csv.open('a', newline='', encoding='utf-8') as f_csv:
            # No escribimos encabezado de nuevo ya que estamos anexando
            escritor_dict = csv.DictWriter(f_csv, fieldnames=fieldnames)
            # Escribir las filas desde la lista de diccionarios
            escritor_dict.writerows(datos_dict)
        print(f"Datos de diccionarios anexados a '{nombre_archivo_csv.name}'.")
    except IOError as e:
        print(f"Error anexando CSV con DictWriter: {e}")

    # 2.4.4 Lectura con csv.DictReader (diccionarios)
    print("\n2.4.4 Leyendo CSV con csv.DictReader (diccionarios)...")
    try:
        with nombre_archivo_csv.open('r', encoding='utf-8') as f_csv:
            lector_dict = csv.DictReader(f_csv) # Automáticamente usa la primera fila como encabezados
            print("Contenido leído como diccionarios:")
            for i, fila_dict in enumerate(lector_dict, 1):
                # fila_dict es un diccionario OrderedDict o dict
                print(f"  Registro {i}: Nombre={fila_dict.get('Nombre', 'N/A')}, Edad={fila_dict.get('Edad', 'N/A')}, Ciudad={fila_dict.get('Ciudad', 'N/A')}")
    except FileNotFoundError:
        print(f"Error: Archivo CSV '{nombre_archivo_csv.name}' no encontrado para lectura Dict.")
    except Exception as e:
        print(f"Error leyendo CSV con DictReader: {e}")


    # ---------------------------------------------------------------------------
    # 2.5 Archivo JSON (JavaScript Object Notation)
    # ---------------------------------------------------------------------------
    print("\n2.5 Trabajando con archivos JSON")
    print("-"*70)

    nombre_archivo_json = Path(dir_ejemplos_avanzados) / 'datos_config.json'

    # Datos Python (diccionarios, listas, strings, números, booleanos, None)
    datos_python = {
        "aplicacion": "Mi Gestor",
        "version": 1.2,
        "usuarios_activos": ["admin", "invitado1", "dev"],
        "configuracion": {
            "tema": "oscuro",
            "notificaciones": True,
            "max_items": None # null en JSON
        },
        "permisos": [
            {"rol": "admin", "acceso": ["lectura", "escritura", "eliminar"]},
            {"rol": "invitado", "acceso": ["lectura"]}
        ]
    }

    # Escribir datos Python a un archivo JSON
    print(f"Escribiendo datos Python en JSON: '{nombre_archivo_json.name}'")
    try:
        with nombre_archivo_json.open('w', encoding='utf-8') as f_json:
            # json.dump() escribe el objeto Python en el archivo en formato JSON
            # indent=4 : Formatea el JSON para que sea legible por humanos
            # ensure_ascii=False : Permite caracteres no ASCII (como acentos) directamente
            json.dump(datos_python, f_json, indent=4, ensure_ascii=False, sort_keys=True)
        print("Datos guardados en JSON exitosamente.")
    except TypeError as e:
        print(f"Error de tipo al serializar a JSON (objeto no serializable?): {e}")
    except IOError as e:
        print(f"Error de E/S escribiendo JSON: {e}")

    # Leer datos desde un archivo JSON a un objeto Python
    print("\nLeyendo datos desde archivo JSON a Python:")
    try:
        with nombre_archivo_json.open('r', encoding='utf-8') as f_json:
            # json.load() lee del archivo y lo convierte en objeto Python
            datos_leidos_json = json.load(f_json)

        print("Datos cargados desde JSON exitosamente.")
        # Acceder a los datos como un diccionario Python
        print(f"  Aplicación: {datos_leidos_json.get('aplicacion', 'N/A')}")
        print(f"  Versión: {datos_leidos_json.get('version', 'N/A')}")
        print(f"  Configuración de Tema: {datos_leidos_json.get('configuracion', {}).get('tema', 'N/A')}")
        print(f"  Primer usuario activo: {datos_leidos_json.get('usuarios_activos', [None])[0]}")
        print(f"  Permisos del rol admin: {datos_leidos_json['permisos'][0]['acceso']}") # Acceso más directo
    except FileNotFoundError:
        print(f"Error: Archivo JSON '{nombre_archivo_json.name}' no encontrado.")
    except json.JSONDecodeError as e:
        print(f"Error decodificando JSON (archivo mal formado?): {e}")
    except IOError as e:
        print(f"Error de E/S leyendo JSON: {e}")
    except KeyError as e:
        print(f"Error: Clave '{e}' no encontrada en los datos JSON leídos.")


    # ---------------------------------------------------------------------------
    # 2.6 Serialización con Pickle (Guardar objetos Python completos)
    # ---------------------------------------------------------------------------
    print("\n2.6 Serialización de objetos Python con Pickle")
    print("-"*70)
    print("Pickle permite guardar casi cualquier objeto Python (listas, dicts, instancias de clase) en un archivo.")
    print("¡CUIDADO! No cargues archivos pickle de fuentes no confiables, pueden ejecutar código malicioso.")

    nombre_archivo_pickle = Path(dir_ejemplos_avanzados) / 'objetos_persona.pkl' # .pkl o .pickle

    # Usamos la clase Persona definida al principio del script
    personas_a_guardar = [
        Persona("Roberto", 45, "Ingeniero"),
        Persona("Sofía", 38, "Médica"),
        Persona("Pablo", 29, "Profesor")
    ]
    # También podemos guardar otros tipos de objetos
    datos_extra = {"fecha_guardado": datetime.now(), "origen": "Ejemplo Pickle"}
    objeto_completo = (personas_a_guardar, datos_extra) # Guardaremos una tupla

    # Serializar (guardar) el objeto en un archivo binario
    print(f"Serializando (guardando) objetos Python en: '{nombre_archivo_pickle.name}'")
    try:
        # 'wb' = write binary (Pickle trabaja con bytes)
        with nombre_archivo_pickle.open('wb') as f_pickle:
            # pickle.dump(objeto_a_guardar, archivo)
            pickle.dump(objeto_completo, f_pickle)
        print("Objetos serializados con Pickle exitosamente.")
    except pickle.PicklingError as e:
        print(f"Error al serializar con Pickle: {e}")
    except IOError as e:
        print(f"Error de E/S escribiendo archivo Pickle: {e}")

    # Deserializar (cargar) el objeto desde el archivo binario
    print("\nDeserializando (cargando) objetos Python desde archivo Pickle:")
    try:
        # 'rb' = read binary
        with nombre_archivo_pickle.open('rb') as f_pickle:
            # objeto_cargado = pickle.load(archivo)
            objeto_cargado_pickle = pickle.load(f_pickle)

        print("Objeto deserializado con Pickle exitosamente.")

        # Verificar y usar el objeto cargado
        if isinstance(objeto_cargado_pickle, tuple) and len(objeto_cargado_pickle) == 2:
            personas_cargadas, metadata_cargada = objeto_cargado_pickle
            print("\n--- Personas Cargadas ---")
            for persona in personas_cargadas:
                print(f"  - {persona}") # Usará el __str__ de la clase Persona
            print("\n--- Metadata Cargada ---")
            for clave, valor in metadata_cargada.items():
                print(f"  - {clave}: {valor}")
        else:
            print("El objeto cargado no tiene la estructura esperada.")

    except FileNotFoundError:
        print(f"Error: Archivo Pickle '{nombre_archivo_pickle.name}' no encontrado.")
    except pickle.UnpicklingError as e:
        print(f"Error al deserializar Pickle (archivo corrupto o no es Pickle?): {e}")
    except ImportError as e:
         print(f"Error de importación al deserializar (la clase '{e}' no se encuentra?): {e}")
    except IOError as e:
        print(f"Error de E/S leyendo archivo Pickle: {e}")

    # ---------------------------------------------------------------------------
    # 2.7 Trabajando con archivos binarios directamente
    # ---------------------------------------------------------------------------
    print("\n2.7 Trabajando directamente con archivos binarios ('rb', 'wb')")
    print("-"*70)

    nombre_archivo_binario = Path(dir_ejemplos_avanzados) / 'datos.bin'

    # Datos binarios (bytes) para escribir
    datos_bytes = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\xFF\xFE' # Secuencia de bytes

    # Escribir datos binarios
    print(f"Escribiendo datos binarios en '{nombre_archivo_binario.name}'...")
    try:
        with nombre_archivo_binario.open('wb') as f_bin: # 'wb' -> Write Binary
            bytes_escritos = f_bin.write(datos_bytes)
        print(f"Se escribieron {bytes_escritos} bytes en el archivo.")
    except IOError as e:
        print(f"Error escribiendo archivo binario: {e}")

    # Leer datos binarios
    print("\nLeyendo datos binarios del archivo...")
    try:
        with nombre_archivo_binario.open('rb') as f_bin: # 'rb' -> Read Binary
            contenido_binario = f_bin.read()

        print(f"Contenido binario leído ({len(contenido_binario)} bytes): {contenido_binario}")
        # Mostrar los bytes como hexadecimal
        print("Contenido en hexadecimal:", contenido_binario.hex())
        # Intentar decodificar (puede fallar si no es texto válido)
        try:
            print("Intento de decodificar como UTF-8:", contenido_binario.decode('utf-8', errors='replace'))
        except Exception as decode_err:
            print(f"No se pudo decodificar como texto: {decode_err}")

    except FileNotFoundError:
        print(f"Error: Archivo binario '{nombre_archivo_binario.name}' no encontrado.")
    except IOError as e:
        print(f"Error leyendo archivo binario: {e}")


    print("\nFin de la Sección 2.")


# =============================================================================
# SECCIÓN 3: PROYECTO PRÁCTICO - SISTEMA DE GESTIÓN DE INVENTARIO (CSV)
# =============================================================================
# La clase Producto está definida al principio del script.

class ServicioInventario:
    """
    Gestiona las operaciones de inventario...
    """

    def __init__(self, nombre_archivo='inventario.csv'):
        """
        Inicializa el servicio de inventario.

        Args:
            nombre_archivo (str): Nombre del archivo CSV para guardar los datos.
        """
        # --- INICIO DE LA MODIFICACIÓN ---
        # Obtener la ruta absoluta del directorio donde está este script .py
        script_dir = Path(__file__).parent.resolve()
        # Construir la ruta completa al archivo CSV dentro de ese directorio
        self.ruta_archivo = script_dir / nombre_archivo
        # --- FIN DE LA MODIFICACIÓN ---

        # El resto del __init__ sigue igual:
        self.productos = []
        self._cargar_productos() # Carga inicial al crear la instancia

    def _cargar_productos(self):
        """
        Carga los productos desde el archivo CSV. Si el archivo no existe,
        inicializa una lista vacía y puede crear el archivo con encabezados.
        Actualiza el contador de IDs de la clase Producto.
        """
        self.productos = []
        Producto._contador_productos = 0 # Reseteamos contador antes de cargar

        if not self.ruta_archivo.exists():
            print(f"Archivo '{self.ruta_archivo}' no encontrado. Se creará uno nuevo al guardar.")
            # Opcional: Crear archivo con encabezados ahora
            # try:
            #     with self.ruta_archivo.open('w', newline='', encoding='utf-8') as f:
            #         escritor = csv.writer(f)
            #         escritor.writerow(Producto.encabezados_csv())
            # except IOError as e:
            #     print(f"Advertencia: No se pudo crear el archivo CSV inicial: {e}")
            return # No hay nada que cargar

        try:
            with self.ruta_archivo.open('r', newline='', encoding='utf-8') as archivo_csv:
                lector = csv.DictReader(archivo_csv)
                # Asegurarse de que los encabezados esperados están presentes
                if not all(h in lector.fieldnames for h in Producto.encabezados_csv()):
                     print(f"Advertencia: Encabezados del CSV ('{lector.fieldnames}') no coinciden con los esperados ('{Producto.encabezados_csv()}'). Intentando cargar de todas formas.")

                for fila in lector:
                    try:
                        # Intentamos crear el producto, manejando posibles errores de formato
                        producto = Producto(
                            id_producto=int(fila.get('ID', 0)), # Usamos get con default
                            nombre=fila.get('Nombre', 'N/D'),
                            precio=float(fila.get('Precio', 0.0)),
                            cantidad=int(fila.get('Cantidad', 0))
                        )
                        self.productos.append(producto)
                    except (ValueError, TypeError) as e_fila:
                        print(f"Advertencia: Saltando fila inválida en CSV: {fila}. Error: {e_fila}")

            print(f"Inventario cargado desde '{self.ruta_archivo}'. {len(self.productos)} productos encontrados.")
            # Aseguramos que el contador de ID esté más allá del máximo cargado
            if self.productos:
                 max_id_cargado = max(p.id_producto for p in self.productos)
                 if max_id_cargado > Producto._contador_productos:
                      Producto._contador_productos = max_id_cargado
            print(f"Contador de Producto ID ajustado a: {Producto._contador_productos}")

        except FileNotFoundError:
             # Ya controlado al inicio, pero por si acaso
             print(f"Archivo '{self.ruta_archivo}' no encontrado durante la carga.")
        except Exception as e:
            print(f"Error crítico al cargar productos desde '{self.ruta_archivo}': {e}")
            # Podríamos decidir si continuar con lista vacía o parar la aplicación
            self.productos = [] # Aseguramos lista vacía en caso de error grave

    def _guardar_todos_los_productos(self):
        """
        Guarda la lista completa de productos actuales en el archivo CSV,
        sobrescribiendo el contenido anterior. Incluye encabezados.
        Es llamado después de agregar, actualizar o eliminar.
        """
        try:
            with self.ruta_archivo.open('w', newline='', encoding='utf-8') as archivo_csv:
                escritor = csv.DictWriter(archivo_csv, fieldnames=Producto.encabezados_csv())
                escritor.writeheader() # Escribir la fila de encabezados
                for producto in self.productos:
                    # Convertimos el producto a un diccionario para DictWriter
                    datos_prod = {
                        'ID': producto.id_producto,
                        'Nombre': producto.nombre,
                        'Precio': producto.precio,
                        'Cantidad': producto.cantidad
                    }
                    escritor.writerow(datos_prod)
            # print(f"Inventario guardado correctamente en '{self.ruta_archivo}'.") # Opcional: Mensaje menos verboso
        except IOError as e:
            print(f"Error al guardar el inventario completo en '{self.ruta_archivo}': {e}")
        except Exception as e:
            print(f"Error inesperado al guardar inventario: {e}")

    def agregar_producto(self, nombre, precio, cantidad):
        """
        Agrega un nuevo producto al inventario y guarda los cambios.

        Args:
            nombre (str): Nombre del nuevo producto.
            precio (float): Precio del nuevo producto.
            cantidad (int): Cantidad inicial del nuevo producto.

        Returns:
            Producto: El objeto Producto creado y agregado, o None si falla.
        """
        try:
            # Validaciones básicas
            if not nombre:
                print("Error: El nombre del producto no puede estar vacío.")
                return None
            precio = float(precio)
            cantidad = int(cantidad)
            if precio < 0 or cantidad < 0:
                 print("Error: El precio y la cantidad no pueden ser negativos.")
                 return None

            nuevo_producto = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
            self.productos.append(nuevo_producto)
            self._guardar_todos_los_productos()
            print(f"Producto agregado exitosamente: {nuevo_producto}")
            return nuevo_producto
        except ValueError:
            print("Error: Precio y cantidad deben ser números válidos.")
            return None
        except Exception as e:
            print(f"Error inesperado al agregar producto: {e}")
            return None

    def buscar_producto(self, id_producto):
        """
        Busca un producto por su ID.

        Args:
            id_producto (int): ID del producto a buscar.

        Returns:
            Producto: El producto encontrado o None si no existe.
        """
        try:
            id_producto_int = int(id_producto)
            for producto in self.productos:
                if producto.id_producto == id_producto_int:
                    return producto
            return None # No encontrado
        except ValueError:
            print("Error: El ID del producto debe ser un número entero.")
            return None

    def actualizar_producto(self, id_producto, nuevo_nombre=None,
                            nuevo_precio=None, nueva_cantidad=None):
        """
        Actualiza los datos de un producto existente y guarda los cambios.

        Args:
            id_producto (int): ID del producto a actualizar.
            nuevo_nombre (str, optional): Nuevo nombre. Si es None, no se cambia.
            nuevo_precio (float, optional): Nuevo precio. Si es None, no se cambia.
            nueva_cantidad (int, optional): Nueva cantidad. Si es None, no se cambia.

        Returns:
            bool: True si se actualizó correctamente, False en caso contrario.
        """
        producto = self.buscar_producto(id_producto)
        if not producto:
            print(f"Error: Producto con ID {id_producto} no encontrado.")
            return False

        actualizado = False
        try:
            if nuevo_nombre is not None and nuevo_nombre.strip(): # No permitir nombre vacío
                producto.nombre = nuevo_nombre.strip()
                actualizado = True
            if nuevo_precio is not None:
                precio_float = float(nuevo_precio)
                if precio_float >= 0:
                    producto.precio = precio_float
                    actualizado = True
                else:
                    print("Advertencia: El precio no puede ser negativo. No se actualizó el precio.")
            if nueva_cantidad is not None:
                 cantidad_int = int(nueva_cantidad)
                 if cantidad_int >= 0:
                     producto.cantidad = cantidad_int
                     actualizado = True
                 else:
                      print("Advertencia: La cantidad no puede ser negativa. No se actualizó la cantidad.")

            if actualizado:
                self._guardar_todos_los_productos()
                print(f"Producto ID {id_producto} actualizado exitosamente.")
                return True
            else:
                print(f"Producto ID {id_producto}: No se proporcionaron cambios válidos.")
                return False

        except ValueError:
            print("Error: Precio y cantidad deben ser números válidos.")
            return False
        except Exception as e:
            print(f"Error inesperado al actualizar producto ID {id_producto}: {e}")
            return False

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario y guarda los cambios.

        Args:
            id_producto (int): ID del producto a eliminar.

        Returns:
            bool: True si se eliminó correctamente, False en caso contrario.
        """
        producto = self.buscar_producto(id_producto)
        if not producto:
            print(f"Error: Producto con ID {id_producto} no encontrado.")
            return False

        try:
            self.productos.remove(producto)
            self._guardar_todos_los_productos()
            print(f"Producto '{producto.nombre}' (ID: {id_producto}) eliminado exitosamente.")
            return True
        except Exception as e:
            # Captura errores inesperados durante la eliminación o guardado
            print(f"Error inesperado al eliminar producto ID {id_producto}: {e}")
            # Podríamos intentar recargar los productos si falla el guardado
            # self._cargar_productos()
            return False

    def listar_productos(self):
        """Muestra todos los productos del inventario formateados."""
        print("\n--- INVENTARIO ACTUAL ---")
        if not self.productos:
            print("El inventario está vacío.")
            return

        # Imprimir encabezados
        print(f"{'ID':<5} {'Nombre':<15} {'Precio':>10} {'Cantidad':>10}")
        print("-" * 45)
        # Imprimir cada producto
        for producto in self.productos:
            print(f"{producto.id_producto:<5d} {producto.nombre:<15} ${producto.precio:>9.2f} {producto.cantidad:>10d}")
        print("-" * 45)
        print(f"Total de productos: {len(self.productos)}")

    def generar_reporte(self, nombre_reporte='reporte_inventario.txt'):
        """
        Genera un reporte detallado del inventario en un archivo de texto.

        Args:
            nombre_reporte (str): Nombre del archivo de reporte.
        """
        print(f"\nGenerando reporte en '{nombre_reporte}'...")
        try:
            with open(nombre_reporte, 'w', encoding='utf-8') as archivo_reporte:
                archivo_reporte.write("=" * 60 + "\n")
                archivo_reporte.write("        REPORTE DE INVENTARIO\n")
                archivo_reporte.write("=" * 60 + "\n")
                archivo_reporte.write(f"Fecha y Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                archivo_reporte.write(f"Archivo de datos: {self.ruta_archivo.resolve()}\n")
                archivo_reporte.write("-" * 60 + "\n\n")

                if not self.productos:
                    archivo_reporte.write("El inventario está vacío.\n")
                else:
                    valor_total_inventario = 0.0
                    archivo_reporte.write(f"{'ID':<5} {'Nombre':<20} {'Precio Unit.':>15} {'Cantidad':>10} {'Valor Total':>15}\n")
                    archivo_reporte.write("-" * 70 + "\n")

                    for producto in self.productos:
                        valor_producto = producto.precio * producto.cantidad
                        valor_total_inventario += valor_producto
                        archivo_reporte.write(f"{producto.id_producto:<5d} ")
                        archivo_reporte.write(f"{producto.nombre:<20} ")
                        archivo_reporte.write(f"${producto.precio:>14.2f} ")
                        archivo_reporte.write(f"{producto.cantidad:>10d} ")
                        archivo_reporte.write(f"${valor_producto:>14.2f}\n")

                    archivo_reporte.write("-" * 70 + "\n")
                    archivo_reporte.write(f"Total de productos: {len(self.productos)}\n")
                    archivo_reporte.write(f"Valor total del inventario: ${valor_total_inventario:,.2f}\n") # Formato con comas

                archivo_reporte.write("\n" + "=" * 60 + "\n")
                archivo_reporte.write("        FIN DEL REPORTE\n")
                archivo_reporte.write("=" * 60 + "\n")

            print(f"Reporte generado exitosamente en '{nombre_reporte}'.")
        except IOError as e:
            print(f"Error de E/S al generar el reporte: {e}")
        except Exception as e:
            print(f"Error inesperado al generar el reporte: {e}")


class SistemaInventarioUI:
    """
    Interfaz de usuario en consola para interactuar con el ServicioInventario.
    """

    def __init__(self):
        """Inicializa la UI y el servicio de inventario."""
        self.servicio = ServicioInventario() # Usa el archivo 'inventario.csv' por defecto

    def mostrar_menu(self):
        """Muestra el menú principal y devuelve la opción elegida."""
        print("\n===== SISTEMA DE GESTIÓN DE INVENTARIO =====")
        print("1. Listar todos los productos")
        print("2. Buscar producto por ID")
        print("3. Agregar nuevo producto")
        print("4. Actualizar producto existente")
        print("5. Eliminar producto")
        print("6. Generar reporte de inventario")
        print("7. Salir")
        print("============================================")

        while True:
            try:
                opcion = input("Seleccione una opción (1-7): ")
                opcion_int = int(opcion)
                if 1 <= opcion_int <= 7:
                    return opcion_int
                else:
                    print("Opción inválida. Por favor, ingrese un número entre 1 y 7.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

    def ejecutar(self):
        """Bucle principal del sistema de inventario."""
        print("¡Bienvenido al Sistema de Gestión de Inventario!")

        while True:
            opcion = self.mostrar_menu()

            if opcion == 1:
                self.servicio.listar_productos()
            elif opcion == 2:
                self.buscar_producto_ui()
            elif opcion == 3:
                self.agregar_producto_ui()
            elif opcion == 4:
                self.actualizar_producto_ui()
            elif opcion == 5:
                self.eliminar_producto_ui()
            elif opcion == 6:
                self.servicio.generar_reporte()
            elif opcion == 7:
                print("\nGuardando cambios y saliendo del sistema. ¡Hasta pronto!")
                break # Sale del bucle while

            input("\nPresione Enter para continuar...") # Pausa para ver la salida

    def buscar_producto_ui(self):
        """Solicita ID y muestra el producto encontrado."""
        try:
            id_buscar = int(input("Ingrese el ID del producto a buscar: "))
            producto = self.servicio.buscar_producto(id_buscar)
            if producto:
                print("\n--- Producto Encontrado ---")
                print(producto)
                print("-------------------------")
            else:
                print(f"No se encontró ningún producto con el ID {id_buscar}.")
        except ValueError:
            print("Error: Ingrese un ID numérico válido.")

    def agregar_producto_ui(self):
        """Solicita datos y agrega un nuevo producto."""
        print("\n--- Agregar Nuevo Producto ---")
        try:
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                return
            precio_str = input("Precio del producto: ")
            cantidad_str = input("Cantidad inicial: ")
            # La validación de tipos y valores la hace el servicio
            self.servicio.agregar_producto(nombre, precio_str, cantidad_str)
        except Exception as e: # Captura errores generales durante la entrada
             print(f"Ocurrió un error durante la entrada de datos: {e}")

    def actualizar_producto_ui(self):
        """Solicita ID y nuevos datos para actualizar."""
        print("\n--- Actualizar Producto Existente ---")
        try:
            id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
            producto = self.servicio.buscar_producto(id_actualizar)
            if not producto:
                print(f"No se encontró producto con ID {id_actualizar}.")
                return

            print(f"Producto actual: {producto}")
            nuevo_nombre = input(f"Nuevo nombre (Enter para mantener '{producto.nombre}'): ").strip()
            nuevo_precio_str = input(f"Nuevo precio (Enter para mantener '{producto.precio:.2f}'): ").strip()
            nueva_cantidad_str = input(f"Nueva cantidad (Enter para mantener '{producto.cantidad}'): ").strip()

            # Pasamos None si el usuario no ingresó nada para ese campo
            self.servicio.actualizar_producto(
                id_actualizar,
                nuevo_nombre if nuevo_nombre else None,
                nuevo_precio_str if nuevo_precio_str else None,
                nueva_cantidad_str if nueva_cantidad_str else None
            )
        except ValueError:
            print("Error: Ingrese un ID numérico y valores válidos para precio/cantidad.")
        except Exception as e:
             print(f"Ocurrió un error durante la actualización: {e}")

    def eliminar_producto_ui(self):
        """Solicita ID y confirma la eliminación."""
        print("\n--- Eliminar Producto ---")
        try:
            id_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
            producto = self.servicio.buscar_producto(id_eliminar)
            if not producto:
                print(f"No se encontró producto con ID {id_eliminar}.")
                return

            confirmacion = input(f"¿Está seguro de que desea eliminar '{producto.nombre}' (ID: {id_eliminar})? (s/N): ").lower()
            if confirmacion == 's':
                self.servicio.eliminar_producto(id_eliminar)
            else:
                print("Eliminación cancelada.")
        except ValueError:
            print("Error: Ingrese un ID numérico válido.")


# =============================================================================
# SECCIÓN 4: EJERCICIOS PROPUESTOS
# =============================================================================

def seccion_ejercicios():
    """
    Presenta ejercicios para practicar los conceptos de manejo de archivos
    y muestra las soluciones comentadas.
    """
    print("\n" + "="*70)
    print("SECCIÓN 4: EJERCICIOS PROPUESTOS")
    print("="*70)

    dir_ejercicios = "ejercicios_resueltos"
    os.makedirs(dir_ejercicios, exist_ok=True)

    # --- Ejercicio 1 ---
    print("\n--- Ejercicio 1: Escribir y Leer Líneas ---")
    print("Crea un archivo llamado 'mi_diario.txt'.")
    print("Escribe al menos 3 entradas de diario en líneas separadas.")
    print("Luego, lee el archivo y muestra cada línea precedida por su número.")

    def solucion_ejercicio_1():
        print("\n-- Solución Ejercicio 1 --")
        ruta_diario = os.path.join(dir_ejercicios, 'mi_diario.txt')
        try:
            # Escribir en el diario
            with open(ruta_diario, 'w', encoding='utf-8') as f:
                f.write("Hoy aprendí sobre manejo de archivos en Python.\n")
                f.write("El bloque 'with' es muy útil.\n")
                f.write("Mañana practicaré con archivos CSV.\n")
            print(f"Archivo '{os.path.basename(ruta_diario)}' creado y escrito.")

            # Leer y mostrar el diario
            print("\nContenido de mi_diario.txt:")
            with open(ruta_diario, 'r', encoding='utf-8') as f:
                for i, linea in enumerate(f, 1):
                    print(f"{i}: {linea.strip()}")
        except IOError as e:
            print(f"Error en ejercicio 1: {e}")
    solucion_ejercicio_1()


    # --- Ejercicio 2 ---
    print("\n--- Ejercicio 2: Anexar a un Archivo ---")
    print("Abre el archivo 'mi_diario.txt' del ejercicio anterior en modo anexar ('a').")
    print("Añade una nueva entrada al final del archivo incluyendo la fecha actual.")
    print("Vuelve a leer todo el archivo para verificar que la nueva línea se añadió.")

    def solucion_ejercicio_2():
        print("\n-- Solución Ejercicio 2 --")
        ruta_diario = os.path.join(dir_ejercicios, 'mi_diario.txt')
        try:
            # Anexar al diario
            fecha_actual = datetime.now().strftime('%Y-%m-%d')
            with open(ruta_diario, 'a', encoding='utf-8') as f:
                f.write(f"Entrada del {fecha_actual}: ¡Sigo aprendiendo!\n")
            print(f"Nueva entrada anexada a '{os.path.basename(ruta_diario)}'.")

            # Leer y mostrar el diario actualizado
            print("\nContenido actualizado de mi_diario.txt:")
            with open(ruta_diario, 'r', encoding='utf-8') as f:
                 print(f.read())
        except FileNotFoundError:
             print(f"Error: El archivo '{ruta_diario}' no existe. Ejecuta la solución 1 primero.")
        except IOError as e:
            print(f"Error en ejercicio 2: {e}")
    solucion_ejercicio_2()


    # --- Ejercicio 3 ---
    print("\n--- Ejercicio 3: Contar Palabras en un Archivo ---")
    print("Crea una función `contar_palabras(ruta_archivo)` que:")
    print("  - Reciba la ruta a un archivo de texto.")
    print("  - Lea el contenido del archivo.")
    print("  - Cuente cuántas palabras hay en total (separadas por espacios).")
    print("  - Devuelva el número total de palabras.")
    print("Pruébala con el archivo 'mi_diario.txt'.")

    def contar_palabras(ruta_archivo):
        """Lee un archivo y cuenta el número total de palabras."""
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                palabras = contenido.split() # Divide por espacios en blanco (espacios, tabs, saltos)
                return len(palabras)
        except FileNotFoundError:
            print(f"Error en contar_palabras: Archivo '{ruta_archivo}' no encontrado.")
            return 0
        except IOError as e:
            print(f"Error de E/S en contar_palabras: {e}")
            return 0

    def solucion_ejercicio_3():
        print("\n-- Solución Ejercicio 3 --")
        ruta_diario = os.path.join(dir_ejercicios, 'mi_diario.txt')
        num_palabras = contar_palabras(ruta_diario)
        if num_palabras > 0:
            print(f"El archivo '{os.path.basename(ruta_diario)}' contiene {num_palabras} palabras.")
    solucion_ejercicio_3()


    # --- Ejercicio 4 ---
    print("\n--- Ejercicio 4: Trabajar con CSV ---")
    print("Crea un archivo llamado 'productos_ejercicio.csv' con los siguientes datos:")
    print("  ID,Nombre,Precio")
    print("  101,Teclado,25.50")
    print("  102,Ratón,15.00")
    print("  103,Monitor,150.75")
    print("Luego, lee el archivo CSV y calcula el precio total de todos los productos.")

    def solucion_ejercicio_4():
        print("\n-- Solución Ejercicio 4 --")
        ruta_csv = os.path.join(dir_ejercicios, 'productos_ejercicio.csv')
        datos_productos = [
            ['ID', 'Nombre', 'Precio'],
            ['101', 'Teclado', '25.50'],
            ['102', 'Ratón', '15.00'],
            ['103', 'Monitor', '150.75']
        ]
        try:
            # Escribir el archivo CSV
            with open(ruta_csv, 'w', newline='', encoding='utf-8') as f:
                escritor = csv.writer(f)
                escritor.writerows(datos_productos)
            print(f"Archivo '{os.path.basename(ruta_csv)}' creado.")

            # Leer el archivo CSV y calcular el total
            precio_total = 0.0
            with open(ruta_csv, 'r', newline='', encoding='utf-8') as f:
                lector = csv.reader(f)
                next(lector) # Saltar la fila de encabezados
                for fila in lector:
                    try:
                        # La columna de precio es la tercera (índice 2)
                        precio = float(fila[2])
                        precio_total += precio
                    except (IndexError, ValueError) as e_fila:
                         print(f"Advertencia: Saltando fila CSV inválida o con formato incorrecto: {fila}. Error: {e_fila}")

            print(f"El precio total de los productos en '{os.path.basename(ruta_csv)}' es: ${precio_total:.2f}")

        except IOError as e:
            print(f"Error en ejercicio 4: {e}")
    solucion_ejercicio_4()


    # --- Ejercicio 5 ---
    print("\n--- Ejercicio 5: Copiar Contenido de Archivo ---")
    print("Crea una función `copiar_archivo(origen, destino)` que copie el contenido")
    print("completo de un archivo `origen` a un archivo `destino`.")
    print("Asegúrate de manejar el caso en que el archivo de origen no exista.")
    print("Pruébala copiando 'mi_diario.txt' a 'copia_diario.txt'.")

    def copiar_archivo(origen, destino):
        """Copia el contenido de un archivo a otro."""
        try:
            with open(origen, 'r', encoding='utf-8') as f_origen, \
                 open(destino, 'w', encoding='utf-8') as f_destino:
                contenido = f_origen.read()
                f_destino.write(contenido)
            print(f"Archivo '{origen}' copiado exitosamente a '{destino}'.")
            return True
        except FileNotFoundError:
            print(f"Error al copiar: El archivo origen '{origen}' no existe.")
            return False
        except IOError as e:
            print(f"Error de E/S al copiar archivos: {e}")
            return False

    def solucion_ejercicio_5():
        print("\n-- Solución Ejercicio 5 --")
        ruta_origen = os.path.join(dir_ejercicios, 'mi_diario.txt')
        ruta_destino = os.path.join(dir_ejercicios, 'copia_diario.txt')
        copiar_archivo(ruta_origen, ruta_destino)

        # Verificar (opcional)
        try:
            with open(ruta_destino, 'r', encoding='utf-8') as f:
                print(f"\nContenido de '{os.path.basename(ruta_destino)}':")
                print(f.read())
        except Exception as e:
            print(f"No se pudo verificar la copia: {e}")
    solucion_ejercicio_5()


    print("\nFin de la Sección 4.")


# =============================================================================
# PUNTO DE ENTRADA PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    """
    Esta parte del código solo se ejecuta cuando el script se corre directamente
    (no cuando se importa como módulo). Permite elegir qué sección ejecutar.
    """
    print("#####################################################")
    print("### CURSO DE MANEJO DE ARCHIVOS EN PYTHON (DEMO) ###")
    print("#####################################################")

    # Descomenta las secciones que quieras ejecutar o ejecuta el sistema de inventario.

    # --- Ejecutar Demostraciones de Conceptos ---
    print("\n*** Ejecutando Sección 1: Conceptos Básicos ***")
    seccion_conceptos_basicos()
    input("\nPresiona Enter para continuar a la Sección 2...")

    print("\n*** Ejecutando Sección 2: Operaciones Avanzadas ***")
    seccion_operaciones_avanzadas()
    input("\nPresiona Enter para continuar a la Sección 4...")

    # --- Ejecutar Ejercicios ---
    print("\n*** Ejecutando Sección 4: Ejercicios Propuestos ***")
    seccion_ejercicios()
    input("\nPresiona Enter para ejecutar el Proyecto Práctico...")

    # --- Ejecutar el Proyecto Práctico (Sistema de Inventario) ---
    print("\n*** Ejecutando Sección 3: Proyecto Práctico - Sistema de Inventario ***")
    sistema_inventario = SistemaInventarioUI()
    sistema_inventario.ejecutar() # Inicia el menú interactivo


    print("\n#####################################################")
    print("###           FIN DE LA DEMOSTRACIÓN             ###")
    print("#####################################################")

    # Limpieza opcional de archivos y directorios creados (¡cuidado!)
    # import shutil
    # directorios_a_limpiar = ["ejemplos_basicos", "ejemplos_avanzados", "ejercicios_resueltos"]
    # archivos_a_limpiar = ["inventario.csv", "reporte_inventario.txt"]
    # print("\nLimpiando archivos y directorios de ejemplo...")
    # for archivo in archivos_a_limpiar:
    #     if os.path.exists(archivo):
    #         try:
    #             os.remove(archivo)
    #             print(f" - Archivo '{archivo}' eliminado.")
    #         except OSError as e:
    #             print(f"Error eliminando archivo '{archivo}': {e}")
    # for directorio in directorios_a_limpiar:
    #     if os.path.exists(directorio):
    #         try:
    #             shutil.rmtree(directorio)
    #             print(f" - Directorio '{directorio}' eliminado.")
    #         except OSError as e:
    #              print(f"Error eliminando directorio '{directorio}': {e}")
