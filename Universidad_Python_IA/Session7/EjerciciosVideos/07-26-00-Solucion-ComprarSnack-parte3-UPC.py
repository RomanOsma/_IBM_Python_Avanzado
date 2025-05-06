# Programa de Máquina de Snacks

# Definicion de la lista de snacks
snacks = [
    {'id': 1, 'nombre': 'Papas', 'precio': 30},
    {'id': 2, 'nombre': 'Refresco', 'precio': 50},
    {'id': 3, 'nombre': 'Sandwich', 'precio': 120}
]

# Lista de productos (vacia). Son los snacks que queremos comprar
productos = []


# Falta agregar las funciones de la máquina de snacks
def mostrar_snacks():
    print('--- Snacks Disponibles ---')
    for snack in snacks:
        print(f'\tId: {snack.get('id')} -> {snack.get('nombre')} '
              f'- ${snack.get('precio')}')

def buscar_snack_por_id(id_a_buscar):
    for snack in snacks:
        if snack.get('id') == id_a_buscar:
            return snack
    # Si llegamos al final y no encontramos el snack regresa None
    return None

def comprar_snack():
    id_snack = int(input('Que snack quieres comprar (id): '))
    snack_encontrado = buscar_snack_por_id(id_snack)
    if snack_encontrado:
        productos.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'Snack NO encontrado con id: {id_snack}')


def mostrar_ticket():
    pass


# Programa principal
if __name__ == '__main__':
    print('*** Máquina de Snacks ***')
    # Cramos el menú
    while True:
        print(f'''Menú:
        1. Mostrar Snacks
        2. Comprar Snack
        3. Mostrar ticket
        4. Salir''')
        opcion = int(input('Escoge una opción: '))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('Regresa pronto!')
            break
        else:
            print('Opción inválida, selecciona otra opción!')