#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PYTHON AVANZADO - GUÍA DE ESTUDIO (PARTE 1)
===========================================
Temas cubiertos:
- Comprensión de listas, diccionarios y conjuntos
- Función zip
- Manejo de cadenas
- Funciones lambda
- Map, filter y reduce
"""


# -----------------------------------------------------------------------------
# Funciones auxiliares para formato
# -----------------------------------------------------------------------------
def titulo(texto):
    print("\n" + "=" * 80)
    print(f"{texto.center(80)}")
    print("=" * 80 + "\n")


def subtitulo(texto):
    print(f"\n{texto}")
    print("-" * len(texto))


# -----------------------------------------------------------------------------
# 1. COMPRENSIÓN DE LISTAS, DICCIONARIOS Y CONJUNTOS
# -----------------------------------------------------------------------------
def seccion_comprension_listas():
    titulo("1. COMPRENSIÓN DE LISTAS")

    # Ejemplo 1: Números pares
    numeros = range(1, 11)
    pares = [n for n in numeros if n % 2 == 0]
    print(f"Números pares del 1-10: {pares}")

    # Ejemplo 2: Diccionario de cuadrados
    cuadrados = {n: n ** 2 for n in numeros if n % 2 != 0}
    print(f"Cuadrados de impares: {cuadrados}")

    # Ejercicio
    subtitulo("Ejercicio: Crea una lista con las longitudes de estas palabras")
    palabras = ["Python", "programación", "lambda", "decorador"]
    # Solución:
    longitudes = [len(p) for p in palabras]
    print(f"Solución: {longitudes}")


# -----------------------------------------------------------------------------
# 2. FUNCIÓN ZIP
# -----------------------------------------------------------------------------
def seccion_zip():
    titulo("2. FUNCIÓN ZIP")

    nombres = ["Ana", "Juan", "María"]
    edades = [25, 30, 28]

    # Combinar listas
    combinados = list(zip(nombres, edades))
    print(f"Combinados: {combinados}")

    # Ejercicio
    subtitulo("Ejercicio: Crea un diccionario a partir de dos listas")
    claves = ["nombre", "edad", "ciudad"]
    valores = ["Carlos", 22, "Lima"]
    # Solución:
    diccionario = dict(zip(claves, valores))
    print(f"Solución: {diccionario}")


# -----------------------------------------------------------------------------
# 3. MANEJO DE CADENAS
# -----------------------------------------------------------------------------
def seccion_cadenas():
    titulo("3. MANEJO DE CADENAS")

    texto = "   Aprendiendo Python Avanzado   "

    # Eliminar espacios y dividir
    texto_limpio = texto.strip().lower().split()
    print(f"Texto procesado: {texto_limpio}")

    # Ejercicio
    subtitulo("Ejercicio: Reemplaza 'Python' por 'Programación' en el texto")
    nuevo_texto = texto.replace("Python", "Programación")
    print(f"Solución: {nuevo_texto}")


# -----------------------------------------------------------------------------
# 4. FUNCIONES LAMBDA
# -----------------------------------------------------------------------------
def seccion_lambda():
    titulo("4. FUNCIONES LAMBDA")

    # Ejemplo: Elevar al cuadrado
    cuadrado = lambda x: x ** 2
    print(f"Cuadrado de 5: {cuadrado(5)}")

    # Ejercicio
    subtitulo("Ejercicio: Filtra números mayores a 10")
    numeros = [5, 12, 8, 15, 3]
    filtrados = list(filter(lambda x: x > 10, numeros))
    print(f"Solución: {filtrados}")


# -----------------------------------------------------------------------------
# 5. MAP, FILTER Y REDUCE
# -----------------------------------------------------------------------------
from functools import reduce


def seccion_map_filter_reduce():
    titulo("5. MAP, FILTER Y REDUCE")

    # Map: Convertir a mayúsculas
    palabras = ["python", "avanzado", "guía"]
    mayusculas = list(map(str.upper, palabras))
    print(f"Mayúsculas: {mayusculas}")

    # Reduce: Sumar todos los elementos
    suma = reduce(lambda x, y: x + y, [1, 2, 3, 4])
    print(f"Suma total: {suma}")


# -----------------------------------------------------------------------------
# EJECUCIÓN
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    seccion_comprension_listas()
    seccion_zip()
    seccion_cadenas()
    seccion_lambda()
    seccion_map_filter_reduce()