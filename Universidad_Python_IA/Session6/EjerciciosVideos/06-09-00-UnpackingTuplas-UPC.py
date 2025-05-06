print('*** Desempaquetado de Tuplas ***')  # unpacking

producto = ('P001', 'Camisa', 20.00)

# Desempaquetamos cada valor en variables independientes
id, descripcion, precio = producto

print(f'Tupla completa: {producto}')
# Valores independientes ya desempaquetados
print(f'Producto: id = {id}, descripcion = {descripcion}, precio = {precio}')