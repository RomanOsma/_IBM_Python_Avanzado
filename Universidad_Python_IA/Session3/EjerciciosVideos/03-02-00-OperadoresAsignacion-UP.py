# Operadores de Asignacion
print('*** Operadores de Asignacion ****')
numero = 5
print(f'Valor de numero: {numero}')
cadena = 'Saludos desde Python'
print(f'Valor de cadena: {cadena}')

# Asignacion multiple. Crear multiples variables en una sola linea
a, b, c = 10, 'Saludos', 14.5
print(f'Valor de a = {a}, b = {b}, c = {c}')

# Asignar un mismo valor a varias variables
x = y = z = 10
print(f'Valor de x = {x}, y = {y}, z = {z}')

# Intercambio de valores sin una variable temporal
x = 5
y = 10
x, y = y, x
print(x, y)  # Output: 10 5

5. Recibir múltiples valores de entrada del usuario
Puedes solicitar al usuario que ingrese varios datos a la vez, separados por comas, y usar la asignación múltiple para obtener estos datos.

nombre, apellido = input("Ingresa tu nombre y apellido, separados por una coma: ").split(',')
print(f"Nombre: {nombre.strip()}, Apellido: {apellido.strip()}")
