# ************ Colecciones en Python ************

# 1. Listas en Python
print('*** Manejo de Listas ***')

# Definición de una lista: Este método sirve para almacenar múltiples valores en una secuencia.
mi_lista = [1, 2, 3, 4, 5]
# Acceder a un elemento por índice. Python utiliza índices basados en cero, donde el primer elemento tiene índice 0.
print(f'Accedemos al valor del índice 4: {mi_lista[4]}')  # Salida: 5
print(f'Accedemos al último índice de la lista: {mi_lista[-1]}')  # Salida: 5

# Modificamos el elemento de la lista en el índice 1.
mi_lista[1] = 10
print(f'Modificamos el valor del índice 1: {mi_lista[1]}')  # Salida: 10

# Agregar un nuevo elemento al final de la lista utilizando el método append().
mi_lista.append(6)
print(f'Lista después de agregar 6: {mi_lista}')  # Salida: [1, 10, 3, 4, 5, 6]

# Añadimos un elemento en un índice específico usando insert().
mi_lista.insert(2, 10)  # El número 10 se agrega en el índice 2.
print(f'Lista después de insertar 10 en el índice 2: {mi_lista}')  # Salida: [1, 10, 10, 3, 4, 5, 6]

# Eliminar elementos de la lista con el método remove(), busca el valor en la lista y lo elimina.
mi_lista.remove(5)
print(f'Lista después de remover 5: {mi_lista}')  # Salida: [1, 10, 10, 3, 4, 6]

# Usamos pop() para eliminar y retornar el elemento en un índice dado.
mi_lista.pop(1)  # Elimina el elemento en el índice 1.
print(f'Lista después de eliminar el índice 1: {mi_lista}')  # Salida: [1, 10, 3, 4, 6]

# También se puede eliminar usando la palabra clave 'del'.
del mi_lista[2]
print(f'Lista después de eliminar el índice 2: {mi_lista}')  # Salida: [1, 10, 4, 6]

# Para obtener la longitud de la lista se usa la función len().
print(f'Largo de la lista: {len(mi_lista)}')  # Salida: 4

# Obtener una sublista usando slicing. Los índices son inclusivos y exclusivos.
sublista = mi_lista[1:3]  # Obtiene elementos del índice 1 al 2 (no incluye el 3).
print(f'Sublista: {sublista}')  # Salida: [10, 4]

# 2. Iterar una Lista en Python
print('*** Iterar una Lista ***')
nombres = ['Karla', 'Juan', 'Laura']
# Iterar sobre una lista usando un bucle for.
for nombre in nombres:
    print(nombre)  # Imprime cada nombre en la lista

# Lista heterogénea que contiene diferentes tipos de datos.
lista_heterogenea = [100, True, 'Ivonne']
for elemento in lista_heterogenea:
    print(elemento)  # Imprime cada elemento de la lista heterogénea

# 3. Ejercicio de un Playlist en Python
print('*** Playlist ***')
# Se define la lista para la reproducción de canciones.
lista_reproduccion = []
numero_canciones = int(input('Cuántas canciones deseas agregar: '))  # El usuario decide cuántas canciones agregar.
# Iteramos desde el índice 0 hasta el número de canciones ingresado.
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la canción {indice + 1}: ')
    lista_reproduccion.append(cancion)  # Agregar canción a la lista

#for indice in range(1, numero_canciones + 1):
#    cancion = input(f'Proporciona la canción {indice}: ')
#    lista_reproduccion.append(cancion)  # Agregar canción a la lista

# Ordenar la lista en orden alfabético utilizando el método sort().
lista_reproduccion.sort()
# lista_reproduccion.sort(reverse=True)
print(f'\nLista de Reproducción en orden Alfabético: ')
for cancion in lista_reproduccion:
    print(f'- {cancion}')  # Muestra cada canción en la lista

# 4. Ejercicio Propuesto - Promedio de Calificaciones en Python
print('*** Promedio de Calificaciones ***')
total_calificaciones = int(input('Proporciona el número de calificaciones a evaluar: '))
calificaciones = []  # Crear lista para almacenar las calificaciones.
# Iterar para ingresar las calificaciones.
for indice in range(total_calificaciones):
    calificacion = int(input(f'Calificación[{indice}] = '))  # Captura de calificación desde el usuario.
    calificaciones.append(calificacion)  # Agregar la calificación a la lista.
print(f'Las calificaciones proporcionadas son: {calificaciones}')
# Sumar todas las calificaciones usando la función sum().
suma_calificaciones = sum(calificaciones)
# Calcular el promedio.
promedio = suma_calificaciones / total_calificaciones
print(f'Promedio de las Calificaciones: {promedio}')

# 5. Tuplas en Python
print('*** Manejo de Tuplas ***')
mi_tupla = (1, 2, 3, 4, 5)
print(f'Elemento de la tupla: {mi_tupla}')  # Tupla original
# Iterar sobre los elementos de una tupla.
for elemento in mi_tupla:
    print(elemento)

# Crear una tupla para representar coordenadas x, y.
coordenadas = (3, 5)
print(f'Coordenada x: {coordenadas[0]}, Coordenada y: {coordenadas[1]}')  # Acceder a los elementos de la tupla.

# 6. Desempaquetamiento (unpacking) de tuplas en Python
print('*** Desempaquetado de Tuplas ***')
producto = ('P001', 'Camisa', 20.00)  # Tupla que representa un producto.
# Desempaquetamos la tupla en variables independientes.
id, descripcion, precio = producto
print(f'Id: {id}, Descripción: {descripcion}, Precio: {precio}')  # Muestra los valores desempaquetados.

# 7. Combinación de Listas y Tuplas en Python
print('*** Combinación de Listas y Tuplas ***')
# Definir una lista que almacena tuplas de productos.
productos = [('P001', 'Camiseta', 20.00), ('P002', 'Jeans', 30.00), ('P003', 'Sudadera', 40.00)]
precio_total = 0
print('Información de los productos: ')
for producto in productos:
    id, descripcion, precio = producto  # Unpacking
    print(f'Producto: id = {id}, descripcion = {descripcion}, precio = {precio}')
    precio_total += precio  # Acumular el total de precios

print(f'Precio total de los productos: {precio_total}')

# 8. Sets (conjuntos) en Python
print('*** Manejo de Sets ***')
# Crear un conjunto, el cual no permite duplicados.
mi_set = {1, 2, 3, 4, 5, 4}  # El 4 duplicado es ignorado.
print(f'Mi set: {mi_set}')  # Imprime el conjunto sin duplicados.

# Agregar elementos al conjunto.
mi_set.add(6)
mi_set.add(7)
mi_set.add(3)  # Intento de agregar un elemento duplicado, no tendrá efecto.
# Eliminar un elemento del conjunto.
mi_set.remove(4)
print(f'Mi set después de eliminar 4: {mi_set}')
# Comprobar si un elemento existe en el conjunto.
print(f'¿El 4 está en el set?: {4 in mi_set}')
# Obtener la longitud del conjunto.
print(f'Cantidad total de elementos en mi set: {len(mi_set)}')
# Set (conjunto)
print('*** Manejo de Sets ***')
# Iterar los elementos del set
for elemento in mi_set:
    print(elemento, end=' ')
# Comprobar si existe un elemento en el set
print(f'\n{4 in mi_set}')
# Obtener la longitud
print(len(mi_set))

# 9. Ejercicio Boletín Informativo en Python
print('*** Boletín Informativo ***')
# Definimos el set inicial vacío que almacenará suscriptores.
suscriptores = set()
numero_suscriptores = int(input('Proporciona el número de suscriptores iniciales: '))
# Iteramos para agregar suscriptores a la lista.
for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))  # Se agrega cada nuevo suscriptor.

# Mostrar la lista de suscriptores inicial.
print(f'Lista de suscriptores inicial: {suscriptores}')

# Verificar si un nuevo suscriptor ya está en la lista.
nuevo_suscriptor = input('Proporciona el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya está en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)  # Agregar el nuevo suscriptor
    print(f'El nuevo suscriptor se ha agregado a la lista {nuevo_suscriptor}')

# Eliminar un suscriptor existente.
suscriptor_eliminar = input('Proporciona el suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'Lista de suscriptores: {suscriptores}')
# Verificar la cantidad total de suscriptores.
print(f'Cantidad total suscriptores: {len(suscriptores)}')

# 10. Diccionarios en Python
print('*** Diccionarios en Python ***')
# Crear un diccionario con claves y valores.
persona = {
    'nombre': 'Sergio',
    'edad': 30,
    'ciudad': 'México'
}
print(f'Diccionario de persona: {persona}')  # Muestra el diccionario.
# Accediendo a los elementos del diccionario por su clave.
print(f'Nombre: {persona["nombre"]}, Edad: {persona["edad"]}, Ciudad: {persona["ciudad"]}')

# Modificar el valor de una clave en el diccionario.
persona['edad'] = 35
persona['profesion'] = 'Ingeniero'  # Agregamos un nuevo elemento.
print(f'Diccionario actualizado: {persona}')

# Eliminar un elemento del diccionario usando 'del'.
del persona['ciudad']
print(f'Diccionario después de eliminar "ciudad": {persona}')

# Iterar sobre el diccionario (clave, valor).
for clave, valor in persona.items():
    print(f'Clave: {clave}, Valor: {valor}')

# 11. Ejercicio Agenda de Contactos - parte 1
print('*** Agenda de Contactos - parte 1 ***')
# Definimos un diccionario de contactos,
# donde la clave es el nombre y el valor es otro diccionario con detalles.
agenda = {
    "Carlos": { "telefono": "55667711", "email": "carlos@mail.com", "direccion": "Calle Principal 132" },
    "María": { "telefono": "99887733", "email": "maria@mail.com", "direccion": "Avenida Central 456" },
    "Pedro": { "telefono": '55139078', 'email': 'pedro@mail.com', 'direccion': 'Plaza Mayor 789' }
}
print(agenda)

# Acceder a información de un contacto específico usando claves.
print(f'Información de contacto de María: Teléfono: {agenda["María"]["telefono"]}, Email: {agenda["María"]["email"]}, Dirección: {agenda["María"]["direccion"]}')
print(f"Información de contacto de María: email: {agenda["María"].get("email")}")
# Agregar un nuevo contacto a la agenda.
agenda['Ana'] = { 'telefono': '55678392', 'email': 'ana@mail.com', 'direccion': 'Calle Salvador Diaz 321' }
print(f'Diccionario de agenda después de agregar a Ana: {agenda}')

# Eliminar un contacto existente usando el método pop().
agenda.pop('Pedro')
print(f'Agenda después de eliminar a Pedro: {agenda}')

# Mostrar todos los contactos.
print('\nLista de contactos en la agenda:')
for nombre, detalles in agenda.items():
    print(f'Nombre: {nombre}, Teléfono: {detalles["telefono"]}, Email: {detalles["email"]}, Dirección: {detalles["direccion"]}')

# 12. Ejercicio Propuesto - Sistema de Inventarios en Python
print('*** Sistema de Inventarios ***')
inventario = []  # Def inimos la variable de inventario como una lista vacía.
numero_productos = int(input('Cuántos productos deseas agregar al inventario? '))
for indice in range(numero_productos):
    print(f'Proporciona los valores del producto {indice + 1}:')
    nombre = input('Nombre: ')  # Capturando el nombre del producto.
    precio = float(input('Precio: '))  # Capturando el precio del producto. Conversión a float.
    cantidad = int(input('Cantidad: '))  # Capturando la cantidad del producto. Conversión a int.
    # Crear un diccionario con los detalles del producto.
    producto = {'id': indice, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    inventario.append(producto)  # Agregar el nuevo producto al inventario.

# Mostrar el inventario de manera simplificada.
print(f'\nInventario actual: {inventario}')

# Buscar un producto por su ID ingresando el ID para buscar.
id_buscar = int(input('\nIngresa el ID del producto a buscar: '))
producto_encontrado = None  # Inicializamos la variable para almacenar el producto encontrado.
for producto in inventario:
    if producto.get('id') == id_buscar:  # Buscar por el ID.
        producto_encontrado = producto
        break
if producto_encontrado:
    print('Información del producto encontrado: ')
    print(f'Id: {producto_encontrado.get("id")}, Nombre: {producto_encontrado.get("nombre")}, Precio: {producto_encontrado.get("precio")}, Cantidad: {producto_encontrado.get("cantidad")}')
else:
    print(f'Producto con id {id_buscar} no encontrado!')

# Mostrar el inventario detallado actualizado.
print(f'\nInventario Detallado Actualizado:')
for producto in inventario:
    print(f'Id: {producto.get("id")}, Nombre: {producto.get("nombre")}, Precio: {producto.get("precio")}, Cantidad: {producto.get("cantidad")}')

