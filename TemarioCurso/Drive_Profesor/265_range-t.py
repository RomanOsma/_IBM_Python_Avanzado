###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
# range() es una función incorporada en Python que genera una secuencia inmutable de números.
# Es muy eficiente en memoria porque no almacena todos los números a la vez, sino que los genera sobre la marcha.
###

from os import system
# Importa la función 'system' del módulo 'os' para interactuar con el sistema operativo.
if system("clear") != 0: system("cls")
# Intenta limpiar la consola. "clear" para Linux/macOS, "cls" para Windows.
# Esto es solo para presentación, no afecta la lógica de range().

print("\nrange():")
# Imprime un encabezado para la salida.

# --- Uso de range() con 1 argumento: range(stop) ---
# Genera una secuencia de números desde 0 (por defecto) hasta stop - 1.

print("\n--- range(stop) ---")
# Generando una secuencia de números del 0 al 9 (no incluye el 10)
for num in range(10):
  # El bucle 'for' itera sobre la secuencia generada por range(10).
  print(num) # Imprime cada número: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# --- Uso de range() con 2 argumentos: range(start, stop) ---
# Genera una secuencia de números desde start hasta stop - 1.
print("\n--- range(start, stop) ---")
# range(inicio, fin)
for num in range(5, 10):
  # Genera números desde 5 hasta 9 (no incluye el 10).
  print(num) # Imprime: 5, 6, 7, 8, 9

# --- Uso de range() con 3 argumentos: range(start, stop, step) ---
# Genera una secuencia desde start hasta stop - 1, incrementando/decrementando en step.
print("\n--- range(start, stop, step) ---")
# range(inicio, fin, paso)
for num in range(0, 1000, 5):
  # Genera números desde 0 hasta 999, de 5 en 5.
  print(num) # Imprime: 0, 5, 10, ..., 995

# --- range() con números negativos ---
print("\n--- range() con negativos ---")
for num in range(-5, 0):
  # Genera números desde -5 hasta -1 (no incluye el 0).
  print(num) # Imprime: -5, -4, -3, -2, -1

# --- range() con paso negativo (contando hacia atrás) ---
print("\n--- range() con paso negativo ---")
for num in range(10, 0, -1):
  # Genera números desde 10 hacia abajo, hasta 1 (no incluye el 0), decrementando de 1 en 1.
  print(num) # Imprime: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# --- Otro ejemplo básico ---
print("\n--- Otro ejemplo range(0, 444) ---")
for num in range(0, 444):
  # Similar a range(444), genera números de 0 a 443.
  print(num) # Imprime: 0, 1, 2, ..., 443

# --- range() crea un objeto 'range', no una lista directamente ---
print("\n--- El objeto range() ---")
nums = range(10)
# 'nums' no es una lista [0, 1, ..., 9]. Es un objeto 'range' que representa esa secuencia.
print(type(nums)) # Imprime: <class 'range'>
print(nums)       # Imprime: range(0, 10)

# Para obtener una lista con los números de la secuencia, hay que convertirlo explícitamente.
list_of_nums = list(nums)
print(list_of_nums) # Imprime: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Usar range() para repetir una acción N veces ---
print("\n--- range() para repetición ---")
# A menudo, solo queremos que un bucle se ejecute un número fijo de veces,
# y no nos importa el valor del contador en cada iteración.
# En estos casos, es común usar '_' como nombre de variable.
# 'seria para hacerlo cinco veces' (comentario original)
for _ in range(5): # El bucle se ejecutará 5 veces (para los valores 0, 1, 2, 3, 4)
  print("hacer cinco veces algo") # Esta línea se imprime 5 veces.

###
# EJERCICIOS (range)
# Estos ejercicios sirven para practicar el uso de range() en diferentes escenarios.
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
# Solución:
# for i in range(1, 11):
#   print(i)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
# Solución:
# for i in range(1, 21, 2): # Empieza en 1, hasta 20, paso de 2
#   print(i)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
# Solución:
# for i in range(5, 51, 5): # Empieza en 5, hasta 50, paso de 5
#   print(i)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
# Solución:
# for i in range(10, 0, -1): # Empieza en 10, hasta 1 (no incluye 0), paso de -1
#   print(i)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
# Solución:
# suma_total = 0
# for i in range(1, 101):
#   suma_total += i
# print(f"La suma es: {suma_total}")
# O más directo: print(sum(range(1, 101)))

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
# Solución:
# try:
#   numero_tabla = int(input("Introduce un número para ver su tabla de multiplicar: "))
#   for i in range(1, 11):
#     print(f"{numero_tabla} x {i} = {numero_tabla * i}")
# except ValueError:
#   print("Entrada inválida. Por favor, introduce un número entero.")
# range() es una función incorporada en Python que genera una secuencia inmutable de números.
# Es muy eficiente en memoria porque no almacena todos los números a la vez, sino que los genera sobre la marcha.
###

from os import system
# Importa la función 'system' del módulo 'os' para interactuar con el sistema operativo.
if system("clear") != 0: system("cls")
# Intenta limpiar la consola. "clear" para Linux/macOS, "cls" para Windows.
# Esto es solo para presentación, no afecta la lógica de range().

print("\nrange():")
# Imprime un encabezado para la salida.

# --- Uso de range() con 1 argumento: range(stop) ---
# Genera una secuencia de números desde 0 (por defecto) hasta stop - 1.
print("\n--- range(stop) ---")
# Generando una secuencia de números del 0 al 9 (no incluye el 10)
for num in range(10):
  # El bucle 'for' itera sobre la secuencia generada por range(10).
  print(num) # Imprime cada número: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# --- Uso de range() con 2 argumentos: range(start, stop) ---
# Genera una secuencia de números desde start hasta stop - 1.
print("\n--- range(start, stop) ---")
# range(inicio, fin)
for num in range(5, 10):
  # Genera números desde 5 hasta 9 (no incluye el 10).
  print(num) # Imprime: 5, 6, 7, 8, 9

# --- Uso de range() con 3 argumentos: range(start, stop, step) ---
# Genera una secuencia desde start hasta stop - 1, incrementando/decrementando en step.
print("\n--- range(start, stop, step) ---")
# range(inicio, fin, paso)
for num in range(0, 1000, 5):
  # Genera números desde 0 hasta 999, de 5 en 5.
  print(num) # Imprime: 0, 5, 10, ..., 995

# --- range() con números negativos ---
print("\n--- range() con negativos ---")
for num in range(-5, 0):
  # Genera números desde -5 hasta -1 (no incluye el 0).
  print(num) # Imprime: -5, -4, -3, -2, -1

# --- range() con paso negativo (contando hacia atrás) ---
print("\n--- range() con paso negativo ---")
for num in range(10, 0, -1):
  # Genera números desde 10 hacia abajo, hasta 1 (no incluye el 0), decrementando de 1 en 1.
  print(num) # Imprime: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# --- Otro ejemplo básico ---
print("\n--- Otro ejemplo range(0, 444) ---")
for num in range(0, 444):
  # Similar a range(444), genera números de 0 a 443.
  print(num) # Imprime: 0, 1, 2, ..., 443

# --- range() crea un objeto 'range', no una lista directamente ---
print("\n--- El objeto range() ---")
nums = range(10)
# 'nums' no es una lista [0, 1, ..., 9]. Es un objeto 'range' que representa esa secuencia.
print(type(nums)) # Imprime: <class 'range'>
print(nums)       # Imprime: range(0, 10)

# Para obtener una lista con los números de la secuencia, hay que convertirlo explícitamente.
list_of_nums = list(nums)
print(list_of_nums) # Imprime: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Usar range() para repetir una acción N veces ---
print("\n--- range() para repetición ---")
# A menudo, solo queremos que un bucle se ejecute un número fijo de veces,
# y no nos importa el valor del contador en cada iteración.
# En estos casos, es común usar '_' como nombre de variable.
# 'seria para hacerlo cinco veces' (comentario original)
for _ in range(5): # El bucle se ejecutará 5 veces (para los valores 0, 1, 2, 3, 4)
  print("hacer cinco veces algo") # Esta línea se imprime 5 veces.

###
# EJERCICIOS (range)
# Estos ejercicios sirven para practicar el uso de range() en diferentes escenarios.
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
# Solución:
for i in range(1, 11):
  print(i)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
# Solución:
for i in range(1, 21, 2): # Empieza en 1, hasta 20, paso de 2
  print(i)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
# Solución:
for i in range(5, 51, 5): # Empieza en 5, hasta 50, paso de 5
  print(i)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
# Solución:
for i in range(10, 0, -1): # Empieza en 10, hasta 1 (no incluye 0), paso de -1
  print(i)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
# Solución:
suma_total = 0
for i in range(1, 101):
  suma_total += i
print(f"La suma es: {suma_total}")
# O más directo: print(sum(range(1, 101)))

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
# Solución:
try:
  numero_tabla = int(input("Introduce un número para ver su tabla de multiplicar: "))
  for i in range(1, 11):
     print(f"{numero_tabla} x {i} = {numero_tabla * i}")
except ValueError:
   print("Entrada inválida. Por favor, introduce un número entero.")
"""
Demuestra el uso de la función incorporada range() de Python.

Este script explica y ejemplifica las diferentes formas de utilizar range():
- Con un argumento (stop).
- Con dos argumentos (start, stop).
- Con tres argumentos (start, stop, step).
- Con números negativos y pasos negativos.

También muestra que range() crea un objeto iterable y cómo usarlo
para repeticiones simples en bucles for. Incluye ejercicios prácticos.
"""

###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
# range() es una función incorporada en Python que genera una secuencia inmutable de números.
# Es muy eficiente en memoria porque no almacena todos los números a la vez, sino que los genera sobre la marcha.
###

from os import system
# Importa la función 'system' del módulo 'os' para interactuar con el sistema operativo.
if system("clear") != 0: system("cls")
# Intenta limpiar la consola. "clear" para Linux/macOS, "cls" para Windows.
# Esto es solo para presentación, no afecta la lógica de range().

print("\nrange():")
# Imprime un encabezado para la salida.

# --- Uso de range() con 1 argumento: range(stop) ---
# Genera una secuencia de números desde 0 (por defecto) hasta stop - 1.
print("\n--- range(stop) ---")
# Generando una secuencia de números del 0 al 9 (no incluye el 10)
for num in range(10):
  # El bucle 'for' itera sobre la secuencia generada por range(10).
  print(num) # Imprime cada número: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# --- Uso de range() con 2 argumentos: range(start, stop) ---
# Genera una secuencia de números desde start hasta stop - 1.
print("\n--- range(start, stop) ---")
# range(inicio, fin)
for num in range(5, 10):
  # Genera números desde 5 hasta 9 (no incluye el 10).
  print(num) # Imprime: 5, 6, 7, 8, 9

# --- Uso de range() con 3 argumentos: range(start, stop, step) ---
# Genera una secuencia desde start hasta stop - 1, incrementando/decrementando en step.
print("\n--- range(start, stop, step) ---")
# range(inicio, fin, paso)
for num in range(0, 1000, 5):
  # Genera números desde 0 hasta 999, de 5 en 5.
  print(num) # Imprime: 0, 5, 10, ..., 995

# --- range() con números negativos ---
print("\n--- range() con negativos ---")
for num in range(-5, 0):
  # Genera números desde -5 hasta -1 (no incluye el 0).
  print(num) # Imprime: -5, -4, -3, -2, -1

# --- range() con paso negativo (contando hacia atrás) ---
print("\n--- range() con paso negativo ---")
for num in range(10, 0, -1):
  # Genera números desde 10 hacia abajo, hasta 1 (no incluye el 0), decrementando de 1 en 1.
  print(num) # Imprime: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# --- Otro ejemplo básico ---
print("\n--- Otro ejemplo range(0, 444) ---")
for num in range(0, 444):
  # Similar a range(444), genera números de 0 a 443.
  print(num) # Imprime: 0, 1, 2, ..., 443

# --- range() crea un objeto 'range', no una lista directamente ---
print("\n--- El objeto range() ---")
nums = range(10)
# 'nums' no es una lista [0, 1, ..., 9]. Es un objeto 'range' que representa esa secuencia.
print(type(nums)) # Imprime: <class 'range'>
print(nums)       # Imprime: range(0, 10)

# Para obtener una lista con los números de la secuencia, hay que convertirlo explícitamente.
list_of_nums = list(nums)
print(list_of_nums) # Imprime: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Usar range() para repetir una acción N veces ---
print("\n--- range() para repetición ---")
# A menudo, solo queremos que un bucle se ejecute un número fijo de veces,
# y no nos importa el valor del contador en cada iteración.
# En estos casos, es común usar '_' como nombre de variable.
# 'seria para hacerlo cinco veces' (comentario original)
for _ in range(5): # El bucle se ejecutará 5 veces (para los valores 0, 1, 2, 3, 4)
  print("hacer cinco veces algo") # Esta línea se imprime 5 veces.

###
# EJERCICIOS (range)
# Estos ejercicios sirven para practicar el uso de range() en diferentes escenarios.
###

# (Aquí irían las soluciones a los ejercicios, idealmente cada una como una función documentada)

# Ejemplo si el Ejercicio 1 fuera una función:
def imprimir_numeros_1_a_10():
    """Imprime los números del 1 al 10 (inclusive) usando range()."""
    print("\nEjercicio 1:")
    for i in range(1, 11):
      print(i)

# Ejemplo si el Ejercicio 6 fuera una función:
def tabla_de_multiplicar():
    """
    Pide un número al usuario e imprime su tabla de multiplicar del 1 al 10.

    Maneja posibles errores si la entrada no es un número entero.
    """
    print("\nEjercicio 6:")
    try:
      numero_tabla = int(input("Introduce un número para ver su tabla de multiplicar: "))
      print(f"Tabla del {numero_tabla}:")
      for i in range(1, 11):
        print(f"{numero_tabla} x {i} = {numero_tabla * i}")
    except ValueError:
      print("Entrada inválida. Por favor, introduce un número entero.")

# Puedes llamar a las funciones aquí para ejecutarla

# Llamadas a las funciones de ejemplo (si las defines)
# imprimir_numeros_1_a_10()
# tabla_de_multiplicar()


