# Set (conjunto)

print('*** Manejo de Sets ***')

# Crear un conjunto
mi_set = {1, 2, 3, 4, 5, 4}

print(f'Mi set: {mi_set}')

# Agregar elementos al conjunto
mi_set.add(6)
mi_set.add(7)

# Intentar agregar un elemento duplicado
mi_set.add(3)

# Eliminar un elemento del conjunto
mi_set.remove(4)

print(f'Mi set: {mi_set}')

# Iterar los elementos del set
for elemento in mi_set:
    print(elemento, end=' ')

# Comprobar si existe un elemento en el set
print(f'\n{4 in mi_set}')

# Obtener la longitud
print(len(mi_set))