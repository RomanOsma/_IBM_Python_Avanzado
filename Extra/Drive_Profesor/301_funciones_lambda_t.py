"""
Analiza y demuestra el uso de las Funciones Lambda en Python.

Este script explica:
- Qué son las funciones lambda (funciones anónimas).
- Su sintaxis concisa.
- Comparación con funciones definidas con 'def'.
- Casos de uso comunes con funciones como map(), filter(), y sorted().
- Ventajas y desventajas (cuándo usarlas y cuándo evitarlas).
- Incluye ejercicios para practicar.
"""

###
# 06 - Funciones Lambda
# Son funciones anónimas (sin nombre formal) que se definen en una sola línea.
# Su principal característica es la concisión.
# Son útiles para operaciones cortas y específicas, especialmente cuando
# se pasan como argumentos a otras funciones de orden superior (como map, filter, sorted).
###

from os import system
# Importa la función 'system' del módulo 'os' para interactuar con el sistema operativo.
if system("clear") != 0: system("cls")
# Intenta limpiar la consola. "clear" para Linux/macOS, "cls" para Windows.

print("\nFunciones Lambda:")
# Imprime un encabezado para la salida.

# --- Sintaxis ---
# La sintaxis es simple:
# lambda argumentos: expresion
# Donde:
# - 'lambda': Palabra clave que indica la creación de una función anónima.
# - 'argumentos': Uno o más argumentos que recibe la función, separados por comas (igual que en 'def').
# - 'expresion': Una única expresión que se evalúa y cuyo resultado es devuelto por la función.
#   ¡Importante! Solo puede contener una expresión, no múltiples sentencias ni bloques complejos.
print("\n--- Sintaxis y Ejemplo Básico ---")

# Ejemplo: Una función lambda que duplica un número.
doble = lambda x: x * 2
# 'x' es el argumento, 'x * 2' es la expresión que se retorna.

# Llamada a la función lambda:
resultado_doble = doble(5)
print(f"Resultado de doble(5): {resultado_doble}") # → 10

# Comparación con una función definida con 'def':
def doble_def(x):
  """Función tradicional que duplica un número."""
  return x * 2

print(f"Resultado de doble_def(5): {doble_def(5)}") # → 10
# La función lambda es más concisa para esta operación simple.

# Ejemplo con múltiples argumentos:
sumar = lambda a, b: a + b
print(f"Resultado de sumar(3, 4): {sumar(3, 4)}") # → 7

# --- Casos de Uso Comunes ---
# Las lambdas brillan cuando se usan junto con funciones incorporadas
# que aceptan otras funciones como argumento.

print("\n--- Casos de Uso Comunes ---")

# 1. Con map(): Aplica una función a cada elemento de un iterable.
print("\n1. Uso con map():")
numeros = [1, 2, 3, 4, 5]
# Usamos lambda para definir la operación (elevar al cuadrado) directamente en map.
cuadrados = list(map(lambda x: x**2, numeros))
# map() devuelve un iterador, lo convertimos a lista para verlo.
print(f"Lista original: {numeros}")
print(f"Cuadrados (con map y lambda): {cuadrados}") # → [1, 4, 9, 16, 25]

# 2. Con filter(): Filtra elementos de un iterable según una condición.
print("\n2. Uso con filter():")
# Usamos lambda para definir la condición de filtrado (ser par).
pares = list(filter(lambda x: x % 2 == 0, numeros))
# filter() devuelve un iterador, lo convertimos a lista.
print(f"Lista original: {numeros}")
print(f"Números pares (con filter y lambda): {pares}") # → [2, 4]

# 3. Con sorted(): Ordena un iterable, permitiendo una clave de ordenación personalizada.
print("\n3. Uso con sorted():")
personas = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Carlos", "edad": 40}
]
# Usamos lambda para especificar que la clave de ordenación es el valor de 'edad'.
personas_ordenadas_por_edad = sorted(personas, key=lambda p: p["edad"])
print("Lista de personas original:")
print(personas)
print("Lista ordenada por edad (con sorted y lambda):")
print(personas_ordenadas_por_edad)
# → [{'nombre': 'Luis', 'edad': 25}, {'nombre': 'Ana', 'edad': 30}, {'nombre': 'Carlos', 'edad': 40}]

# También se puede ordenar por nombre:
personas_ordenadas_por_nombre = sorted(personas, key=lambda p: p["nombre"])
print("Lista ordenada por nombre (con sorted y lambda):")
print(personas_ordenadas_por_nombre)
# → [{'nombre': 'Ana', 'edad': 30}, {'nombre': 'Carlos', 'edad': 40}, {'nombre': 'Luis', 'edad': 25}]


# --- Ventajas y Desventajas ---
print("\n--- Ventajas y Desventajas ---")

# Ventajas:
# - Concisión: Ideales para funciones muy simples que se usan una sola vez.
# - Inline: Se pueden definir directamente donde se necesitan (como en map, filter, sorted).
# - Claridad (en casos simples): Pueden hacer el código más legible si la operación es trivial.

# Desventajas:
# - Limitación a una sola expresión: No pueden contener múltiples líneas, bucles, condicionales complejos (aunque sí expresiones ternarias), ni sentencias como 'print' (solo devuelven el resultado de la expresión).
# - Legibilidad (en casos complejos): Si la expresión se vuelve muy compleja, una función 'def' con un nombre descriptivo es preferible.
# - Sin nombre: Dificulta la reutilización directa y las pruebas unitarias específicas.
# - Sin Docstrings: No se les puede añadir documentación formal (docstrings).

# Ejemplo de lambda compleja (NO RECOMENDADO):
# Es difícil de leer a simple vista.
procesar_complejo = lambda x: x**2 if x > 0 else (-x if x < 0 else 0)
print(f"Procesar complejo (5): {procesar_complejo(5)}")   # → 25
print(f"Procesar complejo (-3): {procesar_complejo(-3)}") # → 3
print(f"Procesar complejo (0): {procesar_complejo(0)}")   # → 0

# Versión equivalente con 'def' (MÁS LEGIBLE):
def procesar_def(x):
  """Procesa x: devuelve su cuadrado si es positivo, su opuesto si es negativo, o 0 si es cero."""
  if x > 0:
    return x**2
  elif x < 0:
    return -x
  else:
    return 0

print(f"Procesar con def (5): {procesar_def(5)}")
print(f"Procesar con def (-3): {procesar_def(-3)}")
print(f"Procesar con def (0): {procesar_def(0)}")

###
# EJERCICIOS (Funciones Lambda)
# Practica usando funciones lambda en diferentes contextos.
# Descomenta las líneas de solución para ver los resultados.
###

# Ejercicio 1: Convertir a Mayúsculas
# Dada la lista: palabras = ["hola", "mundo", "python"]
# Usa map() y una función lambda para crear una nueva lista con todas las palabras en mayúsculas.
print("\nEjercicio 1: Convertir a Mayúsculas")
palabras_ej1 = ["hola", "mundo", "python"]
# Solución:
# mayusculas = list(map(lambda s: s.upper(), palabras_ej1))
# print(mayusculas) # → ['HOLA', 'MUNDO', 'PYTHON']

# Ejercicio 2: Filtrar Números Mayores a 10
# Dada la lista: numeros = [5, 12, 3, 18, 7, 25]
# Usa filter() y una función lambda para crear una nueva lista solo con los números mayores que 10.
print("\nEjercicio 2: Filtrar Números > 10")
numeros_ej2 = [5, 12, 3, 18, 7, 25]
# Solución:
# mayores_a_10 = list(filter(lambda n: n > 10, numeros_ej2))
# print(mayores_a_10) # → [12, 18, 25]

# Ejercicio 3: Ordenar por Longitud de Cadena
# Dada la lista: palabras = ["casa", "elefante", "sol", "libro"]
# Usa sorted() y una función lambda para ordenar la lista de palabras por su longitud (de menor a mayor).
print("\nEjercicio 3: Ordenar por Longitud")
palabras_ej3 = ["casa", "elefante", "sol", "libro"]
# Solución:
# ordenadas_por_longitud = sorted(palabras_ej3, key=lambda p: len(p))
# print(ordenadas_por_longitud) # → ['sol', 'casa', 'libro', 'elefante']

# Ejercicio 4: Lambda Simple para Resta
# Crea una función lambda llamada 'restar' que tome dos argumentos y devuelva su diferencia.
print("\nEjercicio 4: Lambda para Resta")
# Solución:
# restar = lambda x, y: x - y
# print(f"restar(10, 4): {restar(10, 4)}") # → 6

# Ejercicio 5: Filtrar y Mapear
# Dada la lista: numeros = [1, 2, 3, 4, 5, 6]
# Usa filter() y map() con funciones lambda para crear una lista que contenga
# los cuadrados solo de los números impares de la lista original.
print("\nEjercicio 5: Filtrar Impares y Mapear a Cuadrados")
numeros_ej5 = [1, 2, 3, 4, 5, 6]
# Solución:
# impares = filter(lambda x: x % 2 != 0, numeros_ej5)
# cuadrados_impares = list(map(lambda x: x**2, impares))
# O en una línea (menos legible quizás):
# cuadrados_impares = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numeros_ej5)))
# print(cuadrados_impares) # → [1, 9, 25]
