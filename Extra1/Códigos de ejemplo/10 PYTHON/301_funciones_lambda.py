
#   -------------------------------------
#   FUNCIONES LAMBDA
#   -------------------------------------

# Es una función anónima (sin nombre) que puedes definir en una sola línea. 
# Ideal para usar como funciones cortas y rápidas, especialmente cuando las 
# pasas como argumento a otras funciones.

# Sintaxis:
# lambda argumentos: expresión

# 🎯 Ejemplo básico

doble = lambda x: x * 2
print(doble(5))  # → 10

# Equivale a:

def doble(x):
    return x * 2

# 🔥 Casos de uso típicos
# 1. Con map() → aplicar una función a cada elemento de una lista

numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # → [1, 4, 9, 16]

# 2. Con filter() → filtrar elementos que cumplan una condición

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # → [2, 4]

# 3. Con sorted() → ordenar con una clave personalizada

personas = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Carlos", "edad": 40}
]

ordenadas = sorted(personas, key=lambda p: p["edad"])
print(ordenadas)

# 4. Dentro de expresiones simples

sumar = lambda a, b: a + b
print(sumar(3, 4))  # → 7

# ⚠️ ¿Cuándo no usar lambda?
# Si la función tiene más de una línea → usa def.

# Si necesitas claridad o reutilización → mejor con def y un nombre descriptivo.

# Si necesitas anotaciones de tipo o docstrings → usa def.


# 👎 NO recomendable
procesar = lambda x: x**2 if x > 0 else -x  # confuso

# 👍 Mejor
def procesar(x):
    """Aplica una función especial según el valor de x."""
    return x**2 if x > 0 else -x

# 🧪 Mini reto: convertir una función en lambda

def multiplicar(a, b):
    return a * b

# Versión lambda:

multiplicar = lambda a, b: a * b