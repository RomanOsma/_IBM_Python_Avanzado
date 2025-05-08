###
# Comprensión de Listas 
###

# Es una forma concisa de crear listas a partir de otras listas, rangos, 
# o cualquier iterable, usando una sintaxis parecida a una expresión matemática.

# Sintaxis básica

# [expresión for variable in iterable]

# Ejemplo básico:
# Crear una lista con los cuadrados de los números del 0 al 9
# Sin comprensión de listas:

cuadrados = []

for x in range(1, 6):
    cuadrados.append(x**2)

print(cuadrados)  # → [1, 4, 9, 16, 25]

# Con comprensión de listas:
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Listas por comprensión con condición
# Puedes agregar una condición para filtrar elementos:
# [expresion for elemento in iterable if condicion]

# Ejemplo con condición:
# Cuadrados de solo los números pares del 0 al 9

cuadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
print(cuadrados_pares)  # [0, 4, 16, 36, 64]

# Listas por comprensión con condición else
# Cuando necesitas un else, la sintaxis cambia:
# [expresion_if if condicion else expresion_else for elemento in iterable]

# Ejemplo con if-else:
# Clasificar números como "par" o "impar"

clasificacion = ["par" if x % 2 == 0 else "impar" for x in range(5)]
print(clasificacion)  # ['par', 'impar', 'par', 'impar', 'par']

# Listas por comprensión anidadas
# Puedes anidar múltiples bucles for:

# Ejemplo de anidamiento:
# Producto cartesiano de dos listas

colores = ['rojo', 'verde']
tallas = ['S', 'M', 'L']
combinaciones = [(color, talla) for color in colores for talla in tallas]
print(combinaciones)
# [('rojo', 'S'), ('rojo', 'M'), ('rojo', 'L'), 
#  ('verde', 'S'), ('verde', 'M'), ('verde', 'L')]

# Ejemplos avanzados
# 1. Aplanar una matriz:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plana = [num for fila in matriz for num in fila]
print(plana)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. Extraer vocales de una cadena:
cadena = "Listas por Comprensión en Python"
vocales = [c for c in cadena.lower() if c in 'aeiouáéíóú']
print(vocales)  # ['i', 'a', 'o', 'o', 'e', 'ió', 'e', 'o']

# 3. Convertir temperaturas:
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]

# 4. Lista de listas por comprensión:
# Crear una matriz 3x3 con ceros excepto en la diagonal
matriz_identidad = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print(matriz_identidad)
# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
