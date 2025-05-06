"""
Demuestra el uso de la Comprensión de Listas (List Comprehensions) en Python.

Este script explica y ejemplifica las diferentes formas de usar list comprehensions:
- Sintaxis básica y comparación con bucles for tradicionales.
- Uso de condiciones 'if' para filtrar elementos.
- Uso de condiciones 'if-else'.
- Anidamiento de bucles 'for'.
- Ejemplos prácticos como aplanar matrices, extraer caracteres, conversiones, etc.
- Incluye ejercicios para practicar.
"""

###
# 05 - Comprensión de Listas (List Comprehensions)
# Es una forma concisa y eficiente de crear listas en Python.
# Permite generar listas a partir de iterables (como otras listas, rangos, tuplas, etc.)
# aplicando una expresión a cada elemento y, opcionalmente, filtrando elementos.
# Son una alternativa más legible y a menudo más rápida que los bucles 'for' tradicionales
# para la creación de listas.
###

from os import system
# Importa la función 'system' del módulo 'os' para interactuar con el sistema operativo.
if system("clear") != 0: system("cls")
# Intenta limpiar la consola. "clear" para Linux/macOS, "cls" para Windows.

print("\nComprensión de Listas:")
# Imprime un encabezado para la salida.

# --- Sintaxis Básica y Comparación ---
# La sintaxis fundamental es:
# [expresión for variable in iterable]
# Donde:
# - 'expresión': Es lo que se hará con cada elemento (e.g., x**2, elemento.upper()).
# - 'variable': Es el nombre que toma cada elemento del iterable en cada iteración.
# - 'iterable': Es la secuencia original sobre la que se itera (e.g., una lista, range(), una cadena).
print("\n--- Sintaxis Básica y Comparación ---")

# Ejemplo: Crear una lista con los cuadrados de los números del 1 al 5.

# Forma tradicional con bucle for:
print("Forma tradicional:")
cuadrados_trad = []
# Itera sobre los números del 1 al 5 (range(1, 6))
for x in range(1, 6):
    # Calcula el cuadrado y lo añade a la lista
    cuadrados_trad.append(x**2)
print(f"Lista creada con bucle for: {cuadrados_trad}") # → [1, 4, 9, 16, 25]

# Con comprensión de listas:
print("\nCon Comprensión de Listas:")
# [expresión for variable in iterable]
# x**2 es la expresión, x es la variable, range(1, 6) es el iterable
cuadrados_comp = [x**2 for x in range(1, 6)]
print(f"Lista creada con comprensión: {cuadrados_comp}") # → [1, 4, 9, 16, 25]
# Nota: Es más conciso y a menudo más eficiente.

# Otro ejemplo: Números del 0 al 9
numeros_0_9 = [x for x in range(10)]
print(f"Números del 0 al 9: {numeros_0_9}") # → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Comprensión con Condición (if) ---
# Permite filtrar los elementos del iterable *antes* de aplicar la expresión.
# Solo los elementos que cumplen la condición se incluyen en la nueva lista.
# Sintaxis: [expresion for elemento in iterable if condicion]
print("\n--- Comprensión con Condición (if) ---")

# Ejemplo: Cuadrados de solo los números pares del 0 al 9
# Solo incluye el cuadrado si x es par (x % 2 == 0)
cuadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Cuadrados de pares (0-9): {cuadrados_pares}") # → [0, 4, 16, 36, 64]

# Ejemplo: Números impares del 1 al 10
impares = [num for num in range(1, 11) if num % 2 != 0]
print(f"Impares del 1 al 10: {impares}") # → [1, 3, 5, 7, 9]

# Ejemplo: Palabras que empiezan con 'a'
palabras = ["manzana", "pera", "aguacate", "naranja", "albaricoque"]
palabras_con_a = [p for p in palabras if p.startswith('a')]
print(f"Palabras que empiezan con 'a': {palabras_con_a}") # → ['manzana', 'aguacate', 'albaricoque']

# --- Comprensión con Condición (if-else) ---
# Permite aplicar una expresión u otra dependiendo de una condición para *cada* elemento.
# ¡Importante! La sintaxis cambia: la condición va *antes* del 'for'.
# Sintaxis: [expresion_si_verdadero if condicion else expresion_si_falso for elemento in iterable]
print("\n--- Comprensión con Condición (if-else) ---")

# Ejemplo: Clasificar números del 0 al 4 como "par" o "impar"
# Si x es par, añade "par", si no, añade "impar"
clasificacion = ["par" if x % 2 == 0 else "impar" for x in range(5)]
print(f"Clasificación (0-4): {clasificacion}") # → ['par', 'impar', 'par', 'impar', 'par']

# Ejemplo: Duplicar pares, mantener impares (0-5)
# Si x es par, añade x*2, si no, añade x
resultado_ifelse = [x * 2 if x % 2 == 0 else x for x in range(6)]
print(f"Duplicar pares, mantener impares (0-5): {resultado_ifelse}") # → [0, 1, 4, 3, 8, 5]

# --- Comprensión Anidada (Múltiples for) ---
# Permite iterar sobre múltiples iterables, similar a bucles 'for' anidados.
# El orden de los 'for' es el mismo que en bucles anidados: el bucle exterior va primero,
# seguido de los bucles interiores.
# Sintaxis: [expresion for var_ext in iterable_ext for var_int in iterable_int ...]
print("\n--- Comprensión Anidada (Múltiples for) ---")

# Ejemplo: Producto cartesiano de dos listas (todas las combinaciones posibles)
colores = ['rojo', 'verde', 'azul']
tallas = ['S', 'M']
# El bucle exterior (colores) va primero, luego el interior (tallas)
combinaciones = [(color, talla) for color in colores for talla in tallas]
print("Combinaciones color-talla:")
print(combinaciones)
# → [('rojo', 'S'), ('rojo', 'M'), ('verde', 'S'), ('verde', 'M'), ('azul', 'S'), ('azul', 'M')]

# Comparación con bucles anidados tradicionales:
combinaciones_trad = []
for color in colores:
    for talla in tallas:
        combinaciones_trad.append((color, talla))
# print(combinaciones_trad) # Mismo resultado

# --- Ejemplos Prácticos Adicionales ---
print("\n--- Ejemplos Prácticos Adicionales ---")

print("\n1. Aplanar una matriz (lista de listas):")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Itera sobre cada 'fila' en 'matriz', y luego sobre cada 'num' en 'fila'
plana = [num for fila in matriz for num in fila]
print(f"Matriz original: {matriz}")
print(f"Lista aplanada: {plana}") # → [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\n2. Extraer vocales de una cadena:")
cadena = "Listas por Comprensión en Python"
# Convierte a minúsculas y verifica si el carácter está en la cadena de vocales
vocales = [c for c in cadena.lower() if c in 'aeiouáéíóú']
print(f"Cadena original: '{cadena}'")
print(f"Vocales extraídas: {vocales}") # → ['i', 'a', 'o', 'o', 'e', 'i', 'ó', 'e', 'o']

print("\n3. Convertir temperaturas Celsius a Fahrenheit:")
celsius = [0, 10, 20, 30, 40]
# Aplica la fórmula de conversión a cada 'temp' en 'celsius'
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(f"Temperaturas Celsius: {celsius}")
print(f"Temperaturas Fahrenheit: {fahrenheit}") # → [32.0, 50.0, 68.0, 86.0, 104.0]

print("\n4. Crear una matriz identidad (lista de listas anidadas):")
# Bucle externo para filas (i), bucle interno para columnas (j)
# Si i == j (diagonal principal), el valor es 1, sino 0
dimension = 3
matriz_identidad = [[1 if i == j else 0 for j in range(dimension)] for i in range(dimension)]
print(f"Matriz Identidad {dimension}x{dimension}:")
for fila in matriz_identidad: # Imprime la matriz de forma más legible
    print(fila)
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]

print("\n5. Obtener longitudes de palabras:")
frase = "La comprensión de listas es poderosa"
longitudes = [len(palabra) for palabra in frase.split()] # .split() divide la frase en palabras
print(f"Frase: '{frase}'")
print(f"Longitudes de palabras: {longitudes}") # → [2, 11, 2, 6, 2, 8]

###
# EJERCICIOS (List Comprehensions)
# Practica creando listas de forma concisa usando lo aprendido.
# Descomenta las líneas de solución para ver los resultados.
###

# Ejercicio 1: Números Pares
# Crea una lista con los números pares del 0 al 20 usando list comprehension.
print("\nEjercicio 1: Números Pares (0-20)")
# Solución:
# pares_hasta_20 = [num for num in range(21) if num % 2 == 0]
# print(pares_hasta_20) # → [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Ejercicio 2: Palabras en Mayúsculas
# Dada la lista: palabras = ["hola", "mundo", "python"]
# Crea una nueva lista con todas las palabras en mayúsculas.
print("\nEjercicio 2: Palabras en Mayúsculas")
palabras_ej2 = ["hola", "mundo", "python"]
# Solución:
# mayusculas = [palabra.upper() for palabra in palabras_ej2]
# print(mayusculas) # → ['HOLA', 'MUNDO', 'PYTHON']

# Ejercicio 3: Filtrar por Longitud
# Dada la lista: palabras = ["casa", "elefante", "sol", "libro", "ordenador"]
# Crea una nueva lista que solo contenga las palabras con 5 o más letras.
print("\nEjercicio 3: Filtrar por Longitud (>= 5)")
palabras_ej3 = ["casa", "elefante", "sol", "libro", "ordenador"]
# Solución:
# largas = [p for p in palabras_ej3 if len(p) >= 5]
# print(largas) # → ['elefante', 'libro', 'ordenador']

# Ejercicio 4: Extraer Dígitos
# Dada la cadena: texto = "Python 3.10 es genial!"
# Crea una lista que contenga solo los dígitos encontrados en la cadena (como strings).
print("\nEjercicio 4: Extraer Dígitos")
texto_ej4 = "Python 3.10 es genial!"
# Solución:
# digitos = [c for c in texto_ej4 if c.isdigit()]
# print(digitos) # → ['3', '1', '0']

# Ejercicio 5: Múltiplos de 3 y 5
# Crea una lista con los números del 1 al 50 que sean múltiplos de 3 o de 5.
print("\nEjercicio 5: Múltiplos de 3 o 5 (1-50)")
# Solución:
# multiplos_3_5 = [n for n in range(1, 51) if n % 3 == 0 or n % 5 == 0]
# print(multiplos_3_5) # → [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50]

# Ejercicio 6: Tuplas de Número y Cuadrado
# Crea una lista de tuplas donde cada tupla contenga un número (del 1 al 5) y su cuadrado.
# Ejemplo de salida esperada: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
print("\nEjercicio 6: Tuplas (Número, Cuadrado)")
# Solución:
# num_cuadrado = [(x, x**2) for x in range(1, 6)]
# print(num_cuadrado) # → [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Ejercicio 7: Negativos a Cero
# Dada la lista: numeros = [1, -2, 3, -4, 5, -6]
# Crea una nueva lista donde los números negativos se reemplacen por 0, usando if-else.
print("\nEjercicio 7: Reemplazar Negativos por Cero")
numeros_ej7 = [1, -2, 3, -4, 5, -6]
# Solución:
# positivos_o_cero = [n if n >= 0 else 0 for n in numeros_ej7]
# print(positivos_o_cero) # → [1, 0, 3, 0, 5, 0]
