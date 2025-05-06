print('*** Playlist ***')

# Aqui se define la lista
lista_reproduccion = []
numero_canciones = int(input('Cuantas canciones deseas agregar: '))

# Iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)

# Ordenar la lista en orden alfabetico en orden ascendente
lista_reproduccion.sort()
#lista_reproduccion.sort(reverse=True) # orden descendente

# Mostrar la lista de canciones
print(f'\n Lista de Reproducción en orden Alfabético: ')
for cancion in lista_reproduccion:
    print(f'- {cancion}')

#print(f'Lista de canciones: {lista_reproduccion}')