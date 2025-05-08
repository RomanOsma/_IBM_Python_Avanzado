print('*** Sistema de Inventarios (con funciones) ***')

# Inventario del almacen
inventario = [
    {'id': 1, 'nombre': 'Camisa', 'precio': 25.99, 'cantidad': 50},
    {'id': 2, 'nombre': 'Pantalones', 'precio': 39.99, 'cantidad': 30},
    {'id': 3, 'nombre': 'Zapatos', 'precio': 49.99, 'cantidad': 20}
]

# Funcion para mostrar el inventario
def mostrar_inventario():
    print('Inventario del almacén: ')
    for producto in inventario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')}, '
              f'Precio: ${producto.get('precio')}, Cantidad: {producto.get('cantidad')}')


# Funcion para agregar un nuevo producto
def agregar_producto():
    # pass  # Pasa por esta funcion, sin ejecutar nada mas
    print('--- Agregar Nuevo Producto ---')
    id = int(input('Id: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id': id, 'nombre': nombre,
                      'precio': precio, 'cantidad': cantidad}
    inventario.append(nuevo_producto)
    print('Producto agregado al inventario')


# Funcion para buscar por id
def buscar_producto_por_id():
    print('--- Buscar Producto por id ---')
    id_a_buscar = int(input('Ingresa el Id a buscar: '))
    for producto in inventario:
        if producto.get('id') == id_a_buscar:
            print('\nInformacion del producto encontrado: ')
            print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')}, '
                  f'Precio: ${producto.get('precio')}, '
                  f'Cantidad: {producto.get('cantidad')}')
            return
    print('\nProducto no encontrado')

# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n--- Menú ---
        1. Mostrar inventario
        2. Agregar nuevo producto
        3. Buscar producto por Id
        4. Salir''')
        opcion = int(input('Proporciona una opción (1-4): '))
        # Revisamos las opciones de menu
        if opcion == 1: # Mostrar inventario
            mostrar_inventario()
        elif opcion == 2: # Agregar nuevo producto
            agregar_producto()
        elif opcion == 3: # Buscar producto por id
            buscar_producto_por_id()
        elif opcion == 4:
            print('Hasta luego!')
            break
        else:
            print('Opción inválida, proporciona una opción válida')