print('*** Manejo de Tuplas ***')

mi_tupla = (1, 2, 3, 4, 5)
# Las siguientes operaciones no estan permitidas
# mi_tupla[1] = 10
# mi_tupla.append(6)

print(mi_tupla)

# Iteramos los elementos de una tupla
for elemento in mi_tupla:
    print(elemento)

# Crear una tupla para representar una coordenada x, y
coordenadas = (3, 5)

# Acceder a los elementos de la tupla
print(f'\nCoordenada x: {coordenadas[0]}')
print(f'Coordenada y: {coordenadas[1]}')

# Crear una tupla de solo un elemento (unitaria)
tupla_un_elemento = 10,  # si no se pone la coma, no es una tupla sino un tipo entero individual
tupla_un_elemento. # observar lo que despliega 

tupla_anidada = (1, (2, 3), (4, 5))
print(tupla_anidada[1])  # Salida: (2, 3)

