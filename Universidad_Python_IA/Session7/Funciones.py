"""
MANUAL COMPLETO DE FUNCIONES EN PYTHON
======================================

Este archivo contiene todos los conceptos fundamentales sobre funciones en Python,
explicados con detalle mediante comentarios y ejemplos prácticos. Está organizado
en secciones que cubren desde lo más básico hasta conceptos avanzados.

Contenido:
1. Funciones básicas
2. Parámetros y argumentos
3. Retorno de valores
4. Argumentos por nombre y valores por defecto
5. Retorno de múltiples valores (tuplas)
6. Argumentos variables (*args y **kwargs)
7. Funciones recursivas
8. Ejercicios prácticos (inventario, máquina de snacks, calculadora)
9. Módulos y funciones
"""

# =============================================================================
# 1. FUNCIONES BÁSICAS
# =============================================================================
print("\n" + "=" * 80)
print("1. FUNCIONES BÁSICAS")
print("=" * 80)


def saludar():
    """
    Función simple sin parámetros que imprime un saludo.

    Ejemplo:
    >>> saludar()
    Hola desde mi función
    """
    print('Hola desde mi función')


# Llamada a la función
saludar()  # Se ejecuta el código dentro de la función

# Podemos llamar a la función cuantas veces queramos
saludar()
saludar()

# =============================================================================
# 2. PARÁMETROS Y ARGUMENTOS
# =============================================================================
print("\n" + "=" * 80)
print("2. PARÁMETROS Y ARGUMENTOS")
print("=" * 80)


def saludar_con_mensaje(mensaje):
    """
    Función que recibe un parámetro y lo utiliza.

    Args:
        mensaje (str): El mensaje que se desea imprimir

    Ejemplo:
    >>> saludar_con_mensaje("Hola clase")
    Mensaje recibido: Hola clase
    """
    print(f'Mensaje recibido: {mensaje}')


# Llamada con argumento
saludar_con_mensaje("Bienvenidos al curso de Python")

# =============================================================================
# 3. RETORNO DE VALORES
# =============================================================================
print("\n" + "=" * 80)
print("3. RETORNO DE VALORES")
print("=" * 80)


def sumar(a, b):
    """
    Función que recibe dos parámetros y retorna su suma.

    Args:
        a (float): Primer operando
        b (float): Segundo operando

    Returns:
        float: Resultado de la suma a + b

    Ejemplo:
    >>> resultado = sumar(3, 5)
    >>> print(resultado)
    8
    """
    resultado = a + b
    return resultado


# Uso del valor retornado
resultado_suma = sumar(5, 3.5)
print(f'El resultado de la suma es: {resultado_suma}')

# También podemos usar directamente el retorno
print(f'Otra suma: {sumar(10, 20)}')

# =============================================================================
# 4. ARGUMENTOS POR NOMBRE Y VALORES POR DEFECTO
# =============================================================================
print("\n" + "=" * 80)
print("4. ARGUMENTOS POR NOMBRE Y VALORES POR DEFECTO")
print("=" * 80)


def crear_persona(nombre, apellido='', edad=0):
    """
    Función con parámetros con valores por defecto.

    Args:
        nombre (str): Nombre de la persona (obligatorio)
        apellido (str): Apellido de la persona (opcional, por defecto '')
        edad (int): Edad de la persona (opcional, por defecto 0)

    Ejemplos:
    >>> crear_persona(nombre="Juan")
    Persona: nombre = Juan, apellido = , edad = 0

    >>> crear_persona(nombre="Ana", apellido="García", edad=25)
    Persona: nombre = Ana, apellido = García, edad = 25

    >>> crear_persona(edad=30, nombre="Carlos", apellido="López")
    Persona: nombre = Carlos, apellido = López, edad = 30
    """
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')


# Diferentes formas de llamar a la función
crear_persona(nombre='Ricardo', apellido='Quintana', edad=32)
crear_persona(edad=32, nombre='Ricardo', apellido='Quintana')
crear_persona(nombre='Ricardo')  # Usa valores por defecto para apellido y edad

# =============================================================================
# 5. RETORNO DE MÚLTIPLES VALORES (TUPLAS)
# =============================================================================
print("\n" + "=" * 80)
print("5. RETORNO DE MÚLTIPLES VALORES (TUPLAS)")
print("=" * 80)

print('*** Regresar una tupla de valores desde una función ***')

# Definicion de la funcion
def persona_mayusculas(nombre, apellido, edad):
    print('Esta función regresa varios valores (tupla)')
    return nombre.upper(), apellido.upper(), edad

# Programa principal
nombre, apellido, edad = persona_mayusculas('Sandra', 'Jimenez', 42)
print(f'Resultado Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

def obtener_coordenadas():
    """
    Función que retorna múltiples valores (en una tupla).

    Returns:
        tuple: Tres valores representando coordenadas x, y, z

    Ejemplo:
    >>> x, y, z = obtener_coordenadas()
    >>> print(f"Coordenadas: {x}, {y}, {z}")
    Coordenadas: 10, 20, 30
    """
    x, y, z = 10, 20, 30
    return x, y, z  # Python automáticamente empaqueta en una tupla


# Desempaquetado de la tupla retornada
coord_x, coord_y, coord_z = obtener_coordenadas()
print(f'Coordenadas: x={coord_x}, y={coord_y}, z={coord_z}')

# También podemos obtener la tupla completa
coordenadas = obtener_coordenadas()
print(f'Todas las coordenadas: {coordenadas}')

# =============================================================================
# 6. ARGUMENTOS VARIABLES (*ARGS Y **KWARGS)
# =============================================================================
print("\n" + "=" * 80)
print("6. ARGUMENTOS VARIABLES (*ARGS Y **KWARGS)")
print("=" * 80)
print('*** Argumentos Variables ***')


def superheroe_superpoderes(superheroe, nombre,  *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')
    # Iteramos los superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')


# Llamar a la funcion
superheroe_superpoderes('Spiderman', 'Peter Parker', 'Instinto Arácnido', 'Telaraña')
superheroe_superpoderes('Ironman', 'Tony Stark', 'Armadura', 'Playboy', 'Millonario')

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino', 'Juan Perez')

def sumar_numeros(*args):
    """
    Función que acepta cualquier cantidad de argumentos numéricos.

    Args:
        *args: Tupla de argumentos variables

    Returns:
        float: Suma de todos los argumentos

    Ejemplo:
    >>> sumar_numeros(1, 2, 3, 4)
    10
    >>> sumar_numeros(10, 20)
    30
    """
    total = 0
    for numero in args:
        total += numero
    return total


print(f'Suma de 1 a 5: {sumar_numeros(1, 2, 3, 4, 5)}')
print(f'Suma de 3 números: {sumar_numeros(10, 20, 30)}')


def imprimir_info(**kwargs):
    """
    Función que acepta argumentos con nombre variables.

    Args:
        **kwargs: Diccionario de argumentos con nombre

    Ejemplo:
    imprimir_info(nombre="Ana", edad=25, ciudad="Madrid")
    nombre: Ana
    edad: 25
    ciudad: Madrid
    """
    print('\nInformación recibida:')
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')


imprimir_info(nombre='Karla', edad=30, ciudad='México')
imprimir_info(nombre='Carlos', edad=35, ciudad='México', puesto='Gerente', salario=45000)

print('*** Funcion par ***')

# Funcion para saber si un numero es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


numero = int(input('Proporciona un valor numérico: '))
print(f'Número par? {es_par(numero)}')


# =============================================================================
# 7. FUNCIONES RECURSIVAS
# =============================================================================
print("\n" + "=" * 80)
print("7. FUNCIONES RECURSIVAS")
print("=" * 80)


def factorial(n):
    """
    Función recursiva para calcular el factorial de un número.

    Args:
        n (int): Número para calcular factorial (debe ser >= 0)

    Returns:
        int: Factorial de n

    Ejemplo:
    >>> factorial(5)
    120

    Nota:
    - Caso base: factorial(0) = 1
    - Caso recursivo: factorial(n) = n * factorial(n-1)
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_recursivo2(numero):
    # Caso base: fatorial de 0 o 1 es 1
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    # Caso recursivo, calcular factorial del numero reducido en 1
    else:
        factorial_parcial = numero * factorial_recursivo2(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial



numero = 5
print(f'El factorial de {numero} es {factorial(numero)}')
# Solicitar al usuario el numero del cual desea calcular el factorial
numero = int(input('Proporciona el número para calcular su factorial: '))
# Verificamos si el numero es negativo
if numero < 0:
    print('El favtorial no está definido para números negativos')
else:
    # Llamamos a la función factorial_recursivo para calcular el factorial
    resultado = factorial_recursivo2(numero)
    print(f'El factorial de {numero} es: {resultado}')

print(f'El factorial de {numero} es {factorial_recursivo2(numero)}')


print('*** Imprimir del 1 al 5 de forma recursiva ***')


# Definir la funcion recursiva
def funcion_recursiva(numero):
    # Caso Base
    if numero == 1:
        print(numero, end=' ')
    else:  # Caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=' ')

funcion_recursiva(5)

# =============================================================================
# 8. EJERCICIOS PRÁCTICOS
# =============================================================================
print("\n" + "=" * 80)
print("8. EJERCICIOS PRÁCTICOS")
print("=" * 80)

# -----------------------------------------------------------------------------
# 8.1 Sistema de Inventario
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("8.1 Sistema de Inventario")
print("-" * 50)

inventario = [
    {'id': 1, 'nombre': 'Camisa', 'precio': 25.99, 'cantidad': 50},
    {'id': 2, 'nombre': 'Pantalones', 'precio': 39.99, 'cantidad': 30},
    {'id': 3, 'nombre': 'Zapatos', 'precio': 49.99, 'cantidad': 20}
]


def mostrar_inventario():
    """Muestra todos los productos del inventario."""
    print('\n--- INVENTARIO ---')
    for producto in inventario:
        print(f"ID: {producto['id']} - {producto['nombre']} | "
              f"Precio: ${producto['precio']:.2f} | "
              f"Cantidad: {producto['cantidad']}")


def agregar_producto():
    """Permite al usuario agregar un nuevo producto al inventario."""
    print('\n--- AGREGAR PRODUCTO ---')
    nuevo_id = max(p['id'] for p in inventario) + 1 if inventario else 1
    nombre = input('Nombre del producto: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad inicial: '))

    inventario.append({
        'id': nuevo_id,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    })
    print(f'Producto "{nombre}" agregado con éxito (ID: {nuevo_id})')


def buscar_producto():
    """Busca un producto por ID y muestra su información."""
    print('\n--- BUSCAR PRODUCTO ---')
    id_busqueda = int(input('Ingrese ID del producto: '))

    for producto in inventario:
        if producto['id'] == id_busqueda:
            print('\nProducto encontrado:')
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad disponible: {producto['cantidad']}")
            return

    print(f'No se encontró producto con ID {id_busqueda}')


# Menú del sistema de inventario
def menu_inventario():
    while True:
        print('\n--- MENÚ INVENTARIO ---')
        print('1. Mostrar inventario')
        print('2. Agregar producto')
        print('3. Buscar producto')
        print('4. Salir')

        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            mostrar_inventario()
        elif opcion == '2':
            agregar_producto()
        elif opcion == '3':
            buscar_producto()
        elif opcion == '4':
            print('Saliendo del sistema de inventario...')
            break
        else:
            print('Opción no válida. Intente nuevamente.')


# Para ejecutar el sistema de inventario, descomentar la siguiente línea:
menu_inventario()

# -----------------------------------------------------------------------------
# 8.2 Máquina de Snacks
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("8.2 Máquina de Snacks")
print("-" * 50)

snacks_disponibles = [
    {'id': 1, 'nombre': 'Papas', 'precio': 30},
    {'id': 2, 'nombre': 'Refresco', 'precio': 50},
    {'id': 3, 'nombre': 'Sandwich', 'precio': 120}
]

carrito = []


def mostrar_snacks():
    """Muestra los snacks disponibles para comprar."""
    print('\n--- SNACKS DISPONIBLES ---')
    for snack in snacks_disponibles:
        print(f"ID: {snack['id']} - {snack['nombre']} | Precio: ${snack['precio']}")


def agregar_snack():
    """Agrega un snack al carrito de compras."""
    mostrar_snacks()
    try:
        id_snack = int(input('\nIngrese ID del snack que desea: '))
        snack = next((s for s in snacks_disponibles if s['id'] == id_snack), None)

        if snack:
            carrito.append(snack)
            print(f"Snack '{snack['nombre']}' agregado al carrito!")
        else:
            print('ID no válido. Intente nuevamente.')
    except ValueError:
        print('Por favor ingrese un número válido.')


def mostrar_carrito():
    """Muestra el contenido actual del carrito y el total a pagar."""
    if not carrito:
        print('\nEl carrito está vacío.')
        return

    print('\n--- TU CARRITO ---')
    total = 0
    for snack in carrito:
        print(f"- {snack['nombre']}: ${snack['precio']}")
        total += snack['precio']

    print(f"\nTOTAL A PAGAR: ${total}")


# Menú de la máquina de snacks
def menu_snacks():
    while True:
        print('\n--- MÁQUINA DE SNACKS ---')
        print('1. Mostrar snacks disponibles')
        print('2. Agregar snack al carrito')
        print('3. Ver carrito')
        print('4. Salir')

        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            mostrar_snacks()
        elif opcion == '2':
            agregar_snack()
        elif opcion == '3':
            mostrar_carrito()
        elif opcion == '4':
            print('Gracias por su compra!')
            break
        else:
            print('Opción no válida. Intente nuevamente.')


# Para ejecutar la máquina de snacks, descomentar la siguiente línea:
menu_snacks()

# -----------------------------------------------------------------------------
# 8.3 Calculadora
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("8.3 Calculadora")
print("-" * 50)


def calculadora():
    """Calculadora simple con operaciones básicas."""
    while True:
        print('\n--- CALCULADORA ---')
        print('1. Sumar')
        print('2. Restar')
        print('3. Multiplicar')
        print('4. Dividir')
        print('5. Salir')

        opcion = input('Seleccione una operación: ')

        if opcion == '5':
            print('Saliendo de la calculadora...')
            break

        if opcion not in ('1', '2', '3', '4'):
            print('Opción no válida. Intente nuevamente.')
            continue

        try:
            num1 = float(input('Ingrese primer número: '))
            num2 = float(input('Ingrese segundo número: '))
        except ValueError:
            print('Por favor ingrese números válidos.')
            continue

        if opcion == '1':
            print(f'Resultado: {num1 + num2}')
        elif opcion == '2':
            print(f'Resultado: {num1 - num2}')
        elif opcion == '3':
            print(f'Resultado: {num1 * num2}')
        elif opcion == '4':
            if num2 == 0:
                print('Error: No se puede dividir por cero')
            else:
                print(f'Resultado: {num1 / num2:.2f}')


# Para ejecutar la calculadora, descomentar la siguiente línea:
calculadora()

# =============================================================================
# 9. MÓDULOS Y FUNCIONES
# =============================================================================
print("\n" + "=" * 80)
print("9. MÓDULOS Y FUNCIONES")
print("=" * 80)

"""
Para organizar mejor nuestro código, podemos crear módulos separados con funciones
relacionadas y luego importarlas donde las necesitemos.

Ejemplo:
1. Crear un archivo llamado 'operaciones_matematicas.py' con funciones matemáticas
2. En otro archivo, importar las funciones necesarias:

from operaciones_matematicas import sumar, restar

# Y luego usar las funciones importadas
resultado = sumar(5, 3)
"""


# Ejemplo de módulo (simulado aquí para demostración)
def sumar(a, b):
    """Suma dos números."""
    return a + b


def restar(a, b):
    """Resta dos números."""
    return a - b


# Uso de las funciones del "módulo"
print('\nUso de funciones importadas:')
print(f'Suma: {sumar(10, 5)}')
print(f'Resta: {restar(10, 5)}')

# =============================================================================
# EJERCICIOS ADICIONALES PARA PRACTICAR
# =============================================================================
print("\n" + "=" * 80)
print("EJERCICIOS ADICIONALES PARA PRACTICAR")
print("=" * 80)

"""
1. Crea una función que reciba una lista de números y retorne el mayor y el menor.
   Ejemplo: entrada: [5, 2, 9, 1, 5, 6] -> salida: (9, 1)

2. Implementa una función que determine si una palabra es palíndromo (se lee igual
   al derecho y al revés). Ejemplo: "reconocer" -> True

3. Crea una función que simule un cajero automático:
   - Debe permitir consultar saldo, depositar y retirar dinero
   - Mantener el saldo actualizado entre llamadas a funciones
   - Validar que no se pueda retirar más dinero del disponible

4. Implementa una función que reciba una cadena y retorne un diccionario con
   la frecuencia de cada caracter. Ejemplo: "hola" -> {'h':1, 'o':1, 'l':1, 'a':1}

5. Crea una función generadora que produzca números de la secuencia Fibonacci.
"""


# Solución al ejercicio 1 (ejemplo)
def encontrar_extremos(numeros):
    """
    Encuentra el mayor y menor número en una lista.

    Args:
        numeros (list): Lista de números

    Returns:
        tuple: (mayor, menor)
    """
    if not numeros:
        return None, None
    return max(numeros), min(numeros)


# Ejemplo de uso
lista_numeros = [5, 2, 9, 1, 5, 6]
mayor, menor = encontrar_extremos(lista_numeros)
print(f'\nEjercicio 1 - Lista: {lista_numeros}')
print(f'Mayor: {mayor}, Menor: {menor}')

"""
CONSEJOS FINALES:
- Las funciones deben hacer una sola cosa y hacerla bien (principio de responsabilidad única)
- Nombra las funciones con verbos que describan lo que hacen (ej: calcular_total, validar_usuario)
- Usa docstrings para documentar el propósito, parámetros y retorno de cada función
- Mantén las funciones cortas y legibles (idealmente menos de 20 líneas)
- Usa parámetros con valores por defecto para hacer funciones más flexibles
- Considera usar type hints para hacer más claro qué tipos de datos espera tu función
"""

print("\n¡Fin del manual de funciones! Esperamos que te haya sido útil.")