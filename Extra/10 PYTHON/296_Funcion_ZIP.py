


# zip() toma dos o más iterables (listas, tuplas, strings, etc.) y los 
# combina elemento a elemento, devolviendo un iterador de tuplas.

# 📌 Sintaxis

# zip(iterable1, iterable2, ...)

✅ Ejemplo básico

nombres = ["Ana", "Luis", "Carlos"]
edades = [30, 25, 40]

combinado = zip(nombres, edades)

print(list(combinado))
# → [('Ana', 30), ('Luis', 25), ('Carlos', 40)]

# 🧪 ¿Qué pasa si las listas tienen distinto tamaño?

nombres = ["Ana", "Luis"]
edades = [30, 25, 40]  # una edad extra

print(list(zip(nombres, edades)))
# → [('Ana', 30), ('Luis', 25)]

# 👉 zip() se detiene cuando la lista más corta termina

# 🛠️ Usos típicos de zip()
# 1. Recorrer dos listas a la vez

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# 2. Crear un diccionario desde dos listas

keys = ["nombre", "edad", "ciudad"]
values = ["Ángel", 32, "Málaga"]

diccionario = dict(zip(keys, values))
print(diccionario)
# → {'nombre': 'Ángel', 'edad': 32, 'ciudad': 'Málaga'}

# 3. Desempaquetar (unzip) una lista de tuplas

pares = [("a", 1), ("b", 2), ("c", 3)]

letras, numeros = zip(*pares)

print(letras)   # → ('a', 'b', 'c')
print(numeros)  # → (1, 2, 3)

# 🧠 El * sirve para "desempaquetar" listas o tuplas.

# 4. Sumar elementos de dos listas

a = [1, 2, 3]
b = [4, 5, 6]

suma = [x + y for x, y in zip(a, b)]
print(suma)  # → [5, 7, 9]

# 5. Juntar tres listas

nombres = ["Ana", "Luis", "Carlos"]
edades = [30, 25, 40]
ciudades = ["Madrid", "Sevilla", "Málaga"]

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre}, {edad} años, vive en {ciudad}")

# 🧠 zip() devuelve un iterador, no una lista
# Eso significa que si haces:

z = zip([1, 2], [3, 4])
print(z)  # → <zip object at 0x...>

# Tienes que convertirlo con list() o recorrerlo con un bucle para ver su contenido.