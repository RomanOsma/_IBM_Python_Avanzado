print('*** Sistema de Inventarios ***')

# Definimos la variable de inventario
inventario = []

numero_productos = int(input('Cuantos productos deseas agregar al inventario? '))

for indice in range(numero_productos):
    print(f'Proporciona los valores del producto {indice + 1}')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    # Crear el diccionario con el detalle del producto
    producto = {'id': indice, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    # Agregamos el nuevo producto al inventario
    inventario.append(producto)

# Mostrar el inventario de manera simplificada
print(f'\n{inventario}')

# Buscar un producto por ID
id_buscar = int(input('\nIngresa el ID del producto a buscar: '))
producto_encontrado = None
for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado:
    print('Información del producto encontrado: ')
    print(f'''Id: {producto_encontrado.get('id')}
    Nombre: {producto_encontrado.get('nombre')},
    Precio: {producto_encontrado.get('precio')},
    Cantidad: {producto_encontrado.get('cantidad')}''')
else:
    print(f'Producto con id {id_buscar} no encontrado!')

# Mostrar el inventario detallado
print(f'\nInventario Detallado Actualizado: ')
for producto in inventario:
    print(f'''Id: {producto.get('id')}
    Nombre: {producto.get('nombre')},
    Precio: {producto.get('precio')},
    Cantidad: {producto.get('cantidad')}''')