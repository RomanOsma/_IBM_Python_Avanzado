print('*** Manejo de Listas ***')

mi_lista = [1, 2, 3, 4, 5]

# Accedemos a un elemento por indice
print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
print(f'Accedemos al último indice de la lista: {mi_lista[-1]}')


# Modificamos el elemento de la lista
mi_lista[1] = 10
print(f'Modificamos el valor del indice 1: {mi_lista[1]}')

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(mi_lista)

# Añadimos un elemento en un índice específico
mi_lista.insert(2, 10)

# Eliminar elementos de la lista
# Usando el metodo remove
mi_lista.remove(5)  # Remueve el elemento con el valor 5 (no es un indice, sino valor)
print(mi_lista)
# Removemos por indice
mi_lista.pop(1)  # Elimina el elemento con el indice 1 de la lista
print(mi_lista)
# Eliminamos usando la palabra del
del mi_lista[2]
print(mi_lista)

# Longitud de la lista
print(f'Largo de la lista: {len(mi_lista)}')

# Obtener una sublista
sublista = mi_lista[1:3] # obtiene na lista del indice 1 al 2 (no incluye el 3)
print(f'Sublista: {sublista}')