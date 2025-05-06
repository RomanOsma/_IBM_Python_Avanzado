#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PYTHON AVANZADO - GUÍA DE ESTUDIO (PARTE 2)
===========================================
Temas cubiertos:
- Ordenamiento con sorted
- Generadores e iteradores
- Decoradores
- Manejo de excepciones
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
# 6. ORDENAMIENTO CON SORTED
# -----------------------------------------------------------------------------
def seccion_sorted():
    titulo("6. ORDENAMIENTO CON SORTED")

    # Ordenar lista de diccionarios
    empleados = [
        {"nombre": "Ana", "salario": 3000},
        {"nombre": "Juan", "salario": 2500}
    ]
    ordenados = sorted(empleados, key=lambda x: x["salario"], reverse=True)
    print(f"Empleados ordenados: {ordenados}")


# -----------------------------------------------------------------------------
# 7. GENERADORES E ITERADORES
# -----------------------------------------------------------------------------
def seccion_generadores():
    titulo("7. GENERADORES E ITERADORES")

    # Generador de números pares
    def generador_pares(maximo):
        n = 0
        while n < maximo:
            yield n
            n += 2

    print("Números pares < 10:", list(generador_pares(10)))


# -----------------------------------------------------------------------------
# 8. DECORADORES
# -----------------------------------------------------------------------------
def seccion_decoradores():
    titulo("8. DECORADORES")

    # Decorador para medir tiempo
    import time
    def medir_tiempo(func):
        def wrapper(*args):
            inicio = time.time()
            resultado = func(*args)
            print(f"Tiempo: {time.time() - inicio:.2f}s")
            return resultado

        return wrapper

    @medir_tiempo
    def suma_larga(n):
        return sum(range(n))

    print("Suma de 0 a 1,000,000:", suma_larga(1_000_000))


# -----------------------------------------------------------------------------
# 9. MANEJO DE EXCEPCIONES
# -----------------------------------------------------------------------------
def seccion_excepciones():
    titulo("9. MANEJO DE EXCEPCIONES")

    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("¡Error! División por cero.")
    finally:
        print("Bloque 'finally' ejecutado.")


# -----------------------------------------------------------------------------
# EJECUCIÓN
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    seccion_sorted()
    seccion_generadores()
    seccion_decoradores()
    seccion_excepciones()