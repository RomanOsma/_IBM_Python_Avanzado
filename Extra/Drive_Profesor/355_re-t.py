"""
Introduce y demuestra el uso básico del módulo 're' para Expresiones Regulares en Python.

Este script explica:
- Qué son las expresiones regulares (regex) y por qué son útiles.
- Cómo importar el módulo 're'.
- Funciones básicas:
    - re.search(): Encontrar la primera coincidencia de un patrón.
    - re.findall(): Encontrar todas las coincidencias no solapadas.
    - re.finditer(): Encontrar todas las coincidencias como un iterador (eficiente en memoria).
    - re.sub(): Reemplazar texto que coincide con un patrón.
- Acceso a la información de una coincidencia (match object): .group(), .start(), .end().
- Uso de flags (modificadores), específicamente re.IGNORECASE.
- La importancia de usar raw strings (r"...") para patrones regex.
- Incluye ejercicios para practicar los conceptos.
"""

###
# 01 - Expresiones Regulares (Regex) con el módulo 're'
# https://regex101.com/ (Una excelente herramienta para probar regex)
#
# Las expresiones regulares son secuencias de caracteres que definen un patrón de búsqueda.
# Son extremadamente útiles para trabajar con texto.
###

# --- ¿Por qué aprender Regex? ---
# - Búsqueda avanzada: Encontrar patrones específicos (emails, URLs, fechas, etc.)
#   en textos grandes de forma rápida y precisa.
# - Validación de datos: Asegurarse de que la entrada del usuario (emails, teléfonos,
#   contraseñas) cumple un formato específico.
# - Manipulación de texto: Extraer, reemplazar o modificar partes de cadenas de texto
#   de manera flexible y potente.
# - Web Scraping: Extraer información estructurada de páginas web.

# 1. Importar el módulo 're'
import re
from os import system

# Limpiar consola para mejor visualización
if system("clear") != 0: system("cls")

print("\n--- Introducción a Expresiones Regulares con 're' ---")

# --- Conceptos Básicos ---
# - Patrón (Pattern): La expresión regular en sí, escrita como una cadena.
#   Es recomendable usar "raw strings" (r"...") para evitar problemas con las barras invertidas (\).
# - Texto (Text): La cadena donde se buscará el patrón.
# - Coincidencia (Match): Una instancia donde el patrón se encuentra dentro del texto.

# --- 1. Encontrar la Primera Coincidencia: re.search() ---
# Busca el patrón en el texto y devuelve un objeto 'match' si lo encuentra,
# o None si no lo encuentra. Solo devuelve la *primera* ocurrencia.
print("\n--- 1. re.search(): Encontrar la primera coincidencia ---")

# 2. Crear un patrón (usando raw string r"...")
pattern_hola = r"Hola"
# 3. El texto donde buscar
text_saludo = "Hola mundo, hola de nuevo."

# 4. Usar la función de búsqueda
match_result = re.search(pattern_hola, text_saludo)

# 5. Comprobar si se encontró una coincidencia
if match_result:
    print(f"Patrón '{pattern_hola}' encontrado en '{text_saludo}'!")
    # Acceder a la información del match:
    print(f"  Texto coincidente: {match_result.group()}") # .group() devuelve la cadena que coincide
    print(f"  Posición inicial: {match_result.start()}") # .start() devuelve el índice inicial
    print(f"  Posición final: {match_result.end()}")     # .end() devuelve el índice final (exclusivo)
    print(f"  Span (inicio, fin): {match_result.span()}") # .span() devuelve una tupla (start, end)
else:
    print(f"Patrón '{pattern_hola}' NO encontrado en '{text_saludo}'.")

# Ejemplo donde no se encuentra
pattern_adios = r"Adiós"
match_adios = re.search(pattern_adios, text_saludo)
if not match_adios:
    print(f"\nPatrón '{pattern_adios}' NO encontrado en '{text_saludo}'. (Resultado: {match_adios})")

# Ejemplo práctico (originalmente Ejercicio 01)
print("\nEjemplo práctico con search():")
text_ia = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la IA puede cagarla."
pattern_ia = r"IA" # Buscamos "IA" exactamente
found_ia = re.search(pattern_ia, text_ia)

if found_ia:
  print(f"Primera ocurrencia de '{pattern_ia}' encontrada:")
  print(f"  Texto: '{found_ia.group()}'")
  print(f"  Posición: {found_ia.start()}-{found_ia.end()}")
else:
  print(f"Patrón '{pattern_ia}' no encontrado.")

# --- 2. Encontrar Todas las Coincidencias: re.findall() ---
# Busca *todas* las ocurrencias no solapadas del patrón en el texto.
# Devuelve una lista de strings con todas las coincidencias encontradas.
print("\n--- 2. re.findall(): Encontrar todas las coincidencias ---")

text_python = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python."
pattern_python = r"Python" # Buscamos la palabra "Python"

matches_list = re.findall(pattern_python, text_python)

print(f"Patrón '{pattern_python}' encontrado {len(matches_list)} veces.")
print(f"Lista de coincidencias: {matches_list}")

# Nota: findall() solo devuelve los strings, no objetos match con detalles como start/end.

# --- 3. Encontrar Todas las Coincidencias (Iterador): re.finditer() ---
# Similar a findall(), pero devuelve un iterador de objetos 'match'.
# Es más eficiente en memoria si esperas muchas coincidencias, ya que no
# crea la lista completa de strings en memoria de una vez.
print("\n--- 3. re.finditer(): Iterador de coincidencias ---")

matches_iter = re.finditer(pattern_python, text_python)

print(f"Iterando sobre las coincidencias de '{pattern_python}':")
count = 0
for match in matches_iter:
    count += 1
    print(f"  Coincidencia {count}: '{match.group()}' en posición {match.start()}-{match.end()}")

# Ejemplo práctico (originalmente Ejercicio 02)
print("\nEjemplo práctico con finditer():")
text_midu = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
pattern_midu = r"midu"
matches_midu_iter = re.finditer(pattern_midu, text_midu)
count_midu = 0
print(f"Buscando '{pattern_midu}' en '{text_midu}':")
for match in matches_midu_iter:
    count_midu += 1
    print(f"  Encontrado '{match.group()}' en posición {match.start()}-{match.end()}")
print(f"Total de ocurrencias de '{pattern_midu}': {count_midu}")


# --- 4. Modificadores (Flags) ---
# Permiten cambiar el comportamiento de la búsqueda regex.
# Se pasan como argumento adicional a las funciones de 're'.
print("\n--- 4. Modificadores (Flags) ---")

# re.IGNORECASE (o re.I): Ignora diferencias entre mayúsculas y minúsculas.
print("\nEjemplo con re.IGNORECASE:")
text_case = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern_ia_case = r"IA"

# Sin ignorecase
found_strict = re.findall(pattern_ia_case, text_case)
print(f"  findall('{pattern_ia_case}', text_case): {found_strict}") # Solo encuentra 'IA'

# Con ignorecase
found_ignorecase = re.findall(pattern_ia_case, text_case, flags=re.IGNORECASE)
print(f"  findall('{pattern_ia_case}', text_case, re.IGNORECASE): {found_ignorecase}") # Encuentra 'IA', 'ia', 'Ia'

# Ejemplo práctico (originalmente Ejercicio 03)
print("\nEjemplo práctico con flag:")
text_python_case = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern_python_case = r"python"
found_python_ignorecase = re.findall(pattern_python_case, text_python_case, flags=re.IGNORECASE)
print(f"Ocurrencias de '{pattern_python_case}' (ignorando mayúsculas): {found_python_ignorecase}")


# --- 5. Reemplazar Texto: re.sub() ---
# Busca todas las ocurrencias del patrón y las reemplaza con un nuevo texto.
# re.sub(pattern, replacement, text, count=0, flags=0)
# - pattern: El patrón regex a buscar.
# - replacement: El texto con el que se reemplazará.
# - text: El texto original.
# - count (opcional): Número máximo de reemplazos a realizar (0 = todos).
# - flags (opcional): Modificadores como re.IGNORECASE.
print("\n--- 5. Reemplazar Texto: re.sub() ---")

text_reemplazo = "Hola, mundo! Hola de nuevo. Hola otra vez."
pattern_reemplazo = r"hola"
replacement_str = "Adiós"

# Reemplazar todas las ocurrencias, ignorando mayúsculas/minúsculas
new_text = re.sub(pattern_reemplazo, replacement_str, text_reemplazo, flags=re.IGNORECASE)
print(f"Texto original: '{text_reemplazo}'")
print(f"Texto después de re.sub('{pattern_reemplazo}', '{replacement_str}', ..., re.IGNORECASE): '{new_text}'")

# Reemplazar solo la primera ocurrencia
new_text_limitado = re.sub(pattern_reemplazo, replacement_str, text_reemplazo, count=1, flags=re.IGNORECASE)
print(f"Texto después de re.sub con count=1: '{new_text_limitado}'")

# --- Comparación con Métodos de String ---
# Python tiene métodos de string como `find()`, `replace()`, `startswith()`, etc.
# Son útiles para búsquedas y reemplazos simples.
# Sin embargo, Regex es mucho más potente para patrones complejos (ej. validar un email,
# encontrar números con un formato específico, extraer datos estructurados).
# Para tareas simples, los métodos de string pueden ser más legibles y rápidos.
# Para tareas complejas, Regex suele ser la mejor opción.

###
# EJERCICIOS (Introducción a re)
# Practica usando las funciones básicas del módulo 're'.
# Descomenta las soluciones para verificar tus respuestas.
###

# Ejercicio 1: Encontrar un número de teléfono simple
# Dado el texto: "Mi número es 123-456-7890. Llámame!"
# Usa re.search() para encontrar el número de teléfono (asume el formato ddd-ddd-dddd).
# Imprime el número encontrado usando .group().
print("\nEjercicio 1: Encontrar número de teléfono")
texto_telefono = "Mi número es 123-456-7890. Llámame!"
# patron_telefono = r"\d\d\d-\d\d\d-\d\d\d\d" # Patrón simple para ddd-ddd-dddd
# Solución:
# match_tel = re.search(patron_telefono, texto_telefono)
# if match_tel:
#     print(f"Número encontrado: {match_tel.group()}")
# else:
#     print("Número no encontrado.")

# Ejercicio 2: Contar palabras específicas
# Dado el texto: "gato perro gato canario gato leon"
# Usa re.findall() para encontrar cuántas veces aparece la palabra "gato".
print("\nEjercicio 2: Contar 'gato'")
texto_animales = "gato perro gato canario gato leon"
# patron_gato = r"gato"
# Solución:
# matches_gato = re.findall(patron_gato, texto_animales)
# print(f"La palabra 'gato' aparece {len(matches_gato)} veces.")
# print(f"Coincidencias: {matches_gato}")

# Ejercicio 3: Encontrar todas las vocales (ignorando mayúsculas)
# Dado el texto: "AEIOU aeiou BCDFGH"
# Usa re.findall() y re.IGNORECASE para encontrar todas las vocales.
print("\nEjercicio 3: Encontrar vocales (ignore case)")
texto_vocales = "AEIOU aeiou BCDFGH"
# patron_vocales = r"[aeiou]" # [aeiou] es un conjunto de caracteres, coincide con a, e, i, o, u
# Solución:
# vocales_encontradas = re.findall(patron_vocales, texto_vocales, flags=re.IGNORECASE)
# print(f"Vocales encontradas: {vocales_encontradas}")

# Ejercicio 4: Reemplazar espacios múltiples por uno solo
# Dado el texto: "Muchos    espacios   aquí."
# Usa re.sub() para reemplazar cualquier secuencia de uno o más espacios por un solo espacio.
print("\nEjercicio 4: Reemplazar espacios múltiples")
texto_espacios = "Muchos    espacios   aquí."
# patron_espacios = r" +" # " +" significa uno o más espacios
# reemplazo_espacio = " "
# Solución:
# texto_corregido = re.sub(patron_espacios, reemplazo_espacio, texto_espacios)
# print(f"Texto original: '{texto_espacios}'")
# print(f"Texto corregido: '{texto_corregido}'")

# Ejercicio 5: Iterar sobre números
# Dado el texto: "Hay 3 manzanas y 15 naranjas."
# Usa re.finditer() para encontrar todos los números en el texto.
# Imprime cada número encontrado y su posición.
print("\nEjercicio 5: Iterar sobre números")
texto_numeros = "Hay 3 manzanas y 15 naranjas."
# patron_numeros = r"\d+" # "\d+" significa uno o más dígitos
# Solución:
# matches_num_iter = re.finditer(patron_numeros, texto_numeros)
# print(f"Números encontrados en '{texto_numeros}':")
# for match in matches_num_iter:
#     print(f"  Número: {match.group()}, Posición: {match.start()}-{match.end()}")
