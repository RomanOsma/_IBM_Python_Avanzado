print('*** Agenda de Contactos ***')

agenda = {
    "Carlos": {
        "telefono": "55667711",
        "email": "carlos@mail.com",
        "direccion": "Calle Principal 132"
    },
    "María": {
        "telefono": "99887733",
        "email": "maria@mail.com",
        "direccion": "Avenida Central 456"
    },
    "Pedro": {
        "telefono": '55139078',
        'email': 'pedro@mail.com',
        'direccion': 'Plaza Mayor 789'
    }
}

print(agenda)

# Acceder a la informacion de un contacto en específico
print(f'''Información del contacto de María
    Teléfono: {agenda['María']['telefono']}
    Email: {agenda['María']['email']}
    Dirección: {agenda['María']['direccion']}''')

# Agregar un nuevo contacto
agenda['Ana'] = {
    'telefono': '55678392',
    'email': 'ana@mail.com',
    'direccion': 'Calle Salvador Diaz 321'
}

print(agenda)

# Eliminar un contacto existente
# del agenda['Pedro']
# Podemos usar el metodo pop
agenda.pop('Pedro')

print(agenda)

# Mostrar todos los contactos de la agenda
print('\nLista de contactos en la agenda:')
for nombre, detalles in agenda.items():
    print(f''' Nombre: {nombre}
    Telefono: {detalles['telefono']}
    Email: {detalles['email']}
    Dirección: {detalles['direccion']}''')