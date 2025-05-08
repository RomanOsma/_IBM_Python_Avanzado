# dict - diccionario
print('*** Diccionarios en Python ***')

# Crear un diccionario de persona con llave y valor
persona = {
    'nombre': 'Sergio',
    'edad': 30,
    'ciudad': 'México'
}

print(f'Diccionario de persona: {persona}')

# Acceder a los elementos del diccionario
print(f'Nombre: {persona['nombre']}')
print(f'Edad: {persona['edad']}')
print(f'Ciudad: {persona['ciudad']}')

# Modificar un valor del diccionario
persona['edad'] = 35
print(f'Diccionario de persona: {persona}')

# Agregar un nuevo elemento al dict
persona['profesion'] = 'Ingeniero'
print(f'Diccionario de persona: {persona}')

# Eliminar un elemento del diccionario
del persona['ciudad']
print(f'Diccionario de persona: {persona}')

# iterar los elementos de un dict (llave, valor) (key-value)
for clave, valor in persona.items():
    print(f'Clave: {clave}, Valor: {valor}')