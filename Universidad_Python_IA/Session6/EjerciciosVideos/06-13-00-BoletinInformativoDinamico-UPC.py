print('*** Boletín Informativo ***')

# Definimos el set inicial
#suscriptores = {} #aqui se esta definiendo un diccionario vacio, esto no nos sirve
suscriptores = set()

numero_suscriptores = int(input('Proporciona el número de suscriptores iniciales: '))
for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))

print(f'Lista de suscriptores inicial: {suscriptores}')

# Verificar si un nuevo suscriptor ya está en la lista
nuevo_suscriptor = input('Proporciona el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya está en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista {nuevo_suscriptor}')

# Eliminar un suscriptor existente
suscriptor_eliminar = input('Proporciona el suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista')
print(f'Lista de suscriptores: {suscriptores}')

# Verificar la cantidad total de suscriptores
print(f'Cantidad total suscriptores: {len(suscriptores)}')

# Mostrar todos los suscriptores
print(f'--- Lista de suscriptores ---')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')