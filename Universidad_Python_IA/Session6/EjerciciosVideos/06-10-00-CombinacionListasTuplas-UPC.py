print('*** Combinación Listas y Tuplas ***')

# Definir una lista que almacena tuplas de productos
productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'Sudadera', 40.00)
]

# Imprimimos la informacion de cada producto
# y calculamos el precio total
precio_total = 0

print(f'Información de los productos: ')
for producto in productos:
    #print(producto)
    id, descripcion, precio = producto  # unpacking
    print(f'Producto: id = {id}, descripcion = {descripcion}, precio = {precio}')
    precio_total += precio # producto[2] para obtener el precio

print(f'Precio total de los productos: {precio_total}')