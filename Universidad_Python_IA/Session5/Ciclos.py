"""
============================================================
Guía de Estudio: Ciclos en Python y Ejercicios Prácticos
============================================================

Temas:
80. Ciclos en Python
81. Imprimir Valores del 1 al 5 (Ciclo while)
82. Imprimir del 1 al 5 (Ciclo for)
83. Iterar una cadena en Python
84. Ejecución Paso a Paso (Ciclo while en PyCharm)
85. Suma Acumulada en Python
86. Menú Iterativo en Python
87-88. Ejercicio Propuesto - Cajero Automático y su Solución
89-90. Ejercicio Propuesto - Calculadora y su Solución
91-92. Ejercicio Propuesto - Validación de Password y su Solución
93-94. Ejercicio Propuesto - Juego Adivinar un Número y su Solución
95. Ejemplo de Validación de un Formulario en Python
96. Ejemplo con ciclo for en Python
97-98. Ejercicio Propuesto - Dibujar Triángulo y su Solución

Cada sección incluye comentarios detallados que explican el uso de módulos, parámetros, funciones o métodos utilizados, lo que facilitará el estudio y la comprensión.
"""

# =============================================================================
# 80. Ciclos en Python
# =============================================================================
# Un ciclo (o bucle) es una estructura que permite ejecutar repetidamente un bloque de código
# mientras se cumpla una condición o durante un número determinado de iteraciones.

# =============================================================================
# 81. Imprimir Valores del 1 al 5 (Ciclo while)
# =============================================================================
print('*** Ciclo while: Imprimir del 1 al 5 ***')

contador = 1           # Inicializamos el contador en 1
VALOR_MAXIMO = 5       # Definimos el valor máximo hasta donde queremos imprimir

# La condición del while evalúa si "contador" es menor o igual a "VALOR_MAXIMO"
while contador <= VALOR_MAXIMO:
    # Utilizamos f-string para formatear la salida de manera clara
    print(f'Contador: {contador}')
    contador += 1    # Equivalente a: contador = contador + 1

print('*** Fin Ciclo while ***\n')

# =============================================================================
# 82. Imprimir del 1 al 5 (Ciclo for)
# =============================================================================
print('*** Ciclo for: Imprimir del 1 al 5 ***')

# La función range(inicio, fin) genera una secuencia de números desde "inicio" hasta "fin-1".
for contador in range(1, 6):  # range(1, 6) genera 1, 2, 3, 4, 5
    print(contador)

print('*** Fin Ciclo for ***\n')

# =============================================================================
# 83. Iterar una cadena en Python
# =============================================================================
print('*** Iterar una cadena ***')

cadena = 'Hola Mundo'
# Al iterar sobre la cadena, cada carácter se extrae en orden.
for letra in cadena:
    # El argumento "end=' '" en print evita el salto de línea por defecto y separa las letras con un espacio.
    print(letra, end=' ')
print('\n*** Fin de iterar cadena ***\n')

# =============================================================================
# 84. Ejecución Paso a Paso (Ciclo while en PyCharm)
# =============================================================================
# Este ejemplo es ideal para depurar el ciclo en un entorno como PyCharm.
# Puedes colocar puntos de interrupción (breakpoints) y ejecutar el código paso a paso.
print('*** Depuración: Ciclo while paso a paso ***')
contador = 1
while contador <= 3:
    print(f'Ejecución paso a paso, contador: {contador}')
    contador += 1  # Permite observar la actualización de la variable en cada iteración
print('*** Fin Depuración ***\n')

# =============================================================================
# 85. Suma Acumulada en Python
# =============================================================================
print('*** Suma Acumulada: Sumar los primeros 5 números ***')

MAXIMO = 5                  # Valor límite para la suma
acumulador_suma = 0         # Inicializamos el acumulador
numero = 1                  # Empezamos con el número 1

while numero <= MAXIMO:
    # Imprimimos la operación que se realizará en la iteración
    print(f'(acumulador_suma + numero) -> {acumulador_suma} + {numero}')
    acumulador_suma += numero  # Se acumula el valor de "numero"
    numero += 1                # Se incrementa "numero" en 1
    print(f'Suma parcial acumulada: {acumulador_suma}\n')

print(f'Resultado suma acumulada: {acumulador_suma}\n')

# =============================================================================
# 86. Menú Iterativo en Python
# =============================================================================
# Este ejemplo ilustra el uso de un ciclo while con control booleano para crear un menú interactivo.
print('*** Menú Iterativo ***')

salir = False  # Variable de control para salir del ciclo

while not salir:
    # Se muestra un menú multilinea usando triple comillas (''' ... ''')
    print('''Menu:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir''')
    # Solicitamos al usuario que ingrese una opción (convertida a entero)
    opcion = int(input('Escoje una opción: '))

    # Evaluamos la opción utilizando condicionales if-elif-else
    if opcion == 1:
        print('Creando tu cuenta...\n')
    elif opcion == 2:
        print('Eliminando tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema. Hasta pronto...\n')
        salir = True  # Cambiamos el valor a True para salir del ciclo
    else:
        print('Opción inválida, selecciona otra opción...\n')

# =============================================================================
# 87-88. Ejercicio Propuesto - Cajero Automático en Python
# =============================================================================
print('*** Aplicación de Cajero Automático ***')

saldo = 1000  # Saldo inicial del usuario en el cajero automático

salir = False
while not salir:
    print('''Operaciones disponibles:
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = int(input('Escoje una opción: '))

    if opcion == 1:
        # Mostramos el saldo actual, formateado a 2 decimales
        print(f'Tu saldo actual es: ${saldo:.2f}\n')
    elif opcion == 2:
        retiro = float(input('Ingresa el monto a retirar: '))
        if retiro <= saldo:
            saldo -= retiro  # Actualizamos el saldo restando el monto retirado
            print(f'Tu nuevo saldo es: ${saldo:.2f}\n')
        else:
            print(f'No cuentas con saldo suficiente. Saldo actual: ${saldo:.2f}\n')
    elif opcion == 3:
        deposito = float(input('Ingresa el monto a depositar: '))
        saldo += deposito  # Actualizamos el saldo sumando el monto depositado
        print(f'Tu nuevo saldo es: ${saldo:.2f}\n')
    elif opcion == 4:
        print('Saliendo del cajero automático. ¡Hasta pronto!')
        salir = True
    else:
        print('Opción inválida. Selecciona otra opción...\n')

# =============================================================================
# 89-90. Ejercicio Propuesto - Calculadora en Python
# =============================================================================
print('\n*** Calculadora ***')

# Inicializamos las variables (operando1, operando2 y resultado)
operando1 = operando2 = resultado = 0

salir = False
while not salir:
    print('''Operaciones disponibles:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    opcion = int(input('Escoje una opción: '))

    # Si la opción está entre 1 y 4, solicitamos dos números
    if 1 <= opcion <= 4:
        operando1 = float(input('Dame el valor 1: '))
        operando2 = float(input('Dame el valor 2: '))

    # Realizamos la operación correspondiente
    if opcion == 1:
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado:.2f}\n')
    elif opcion == 2:
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado:.2f}\n')
    elif opcion == 3:
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicación es: {resultado:.2f}\n')
    elif opcion == 4:
        # Validamos división entre cero
        if operando2 == 0:
            print('Error: División entre cero no permitida.\n')
        else:
            resultado = operando1 / operando2
            print(f'El resultado de la división es: {resultado:.2f}\n')
    elif opcion == 5:
        print('Saliendo de la calculadora. ¡Hasta pronto!')
        salir = True
    else:
        print('Opción inválida, selecciona otra opción...\n')

# =============================================================================
# 91-92. Ejercicio Propuesto - Validación de Password
# =============================================================================
print('\n*** Validación de Password ***')

# Se solicita al usuario que ingrese un password que tenga al menos 6 caracteres
password = input('Ingresa un password (mínimo 6 caracteres): ')

# Se valida que la longitud del password sea adecuada. La función len() retorna la cantidad de caracteres.
while len(password) < 6:
    print('El password no cumple con los requisitos. Debe tener al menos 6 caracteres.')
    password = input('Ingresa un nuevo valor de password: ')

print('El valor del password es válido.\n')

# =============================================================================
# 93-94. Ejercicio Propuesto - Juego Adivinar un Número
# =============================================================================
print('*** Juego: Adivinar el Número Secreto ***')

from random import randint  # Importamos la función randint para generar un número aleatorio

# Generamos un número aleatorio entre 1 y 50
numero_secreto = randint(1, 50)
intentos = 0
INTENTOS_MAXIMOS = 5
adivinanza = None

# Bucle while: se ejecuta mientras la adivinanza no sea igual al número secreto y el número de intentos sea menor al máximo permitido.
while adivinanza != numero_secreto and intentos < INTENTOS_MAXIMOS:
    adivinanza = int(input('Adivina el número secreto (entre 1 y 50): '))
    intentos += 1
    # Proporcionamos retroalimentación al usuario
    if adivinanza < numero_secreto:
        print('El número secreto es mayor.')
    elif adivinanza > numero_secreto:
        print('El número secreto es menor.')

# Mensaje final, dependiendo si se adivinó o se agotaron los intentos
if adivinanza == numero_secreto:
    print(f'¡Felicidades! Adivinaste el número secreto en {intentos} intentos.')
else:
    print(f'Lo siento, has agotado tus {INTENTOS_MAXIMOS} intentos. El número secreto era: {numero_secreto}\n')

# =============================================================================
# 95. Ejemplo de Validación de un Formulario en Python
# =============================================================================
print('*** Validación de un Formulario ***')

# Se solicita que el usuario ingrese un nombre de usuario que no sea vacío.
nombre_usuario = ''
while not nombre_usuario:
    nombre_usuario = input('Ingresa tu nombre de usuario: ').strip()
    # .strip() elimina espacios en blanco al principio y al final
print(f'Nombre de usuario válido: {nombre_usuario}\n')

# =============================================================================
# 96. Ejemplo: Repetición de un Mensaje con ciclo for
# =============================================================================
print('*** Repetición de un Mensaje ***')

mensaje = input('Proporciona un mensaje a repetir: ')
numero_de_repeticiones = int(input('Proporciona el número de repeticiones: '))

# Iteramos usando un ciclo for sobre un rango. La variable "_" se utiliza convencionalmente cuando no se necesita usar el índice.
for _ in range(numero_de_repeticiones):
    print(mensaje)
print('*** Fin Repetición de Mensaje ***\n')

# =============================================================================
# 97-98. Ejercicio Propuesto - Dibujar Triángulo Simétrico en Python
# =============================================================================
print('*** Dibujar Triángulo Simétrico ***')

numero_de_filas = int(input('Proporciona el número de filas para el triángulo: '))

# Dibujar un triángulo simétrico: en cada fila se imprimen espacios y asteriscos
for fila in range(1, numero_de_filas + 1):
    # Calculamos la cantidad de espacios en blanco necesarios para alinear el triángulo en el centro
    espacios_en_blanco = " " * (numero_de_filas - fila)
    # Calculamos el número de asteriscos. Para un triángulo simétrico, la cantidad de asteriscos es (2*fila - 1)
    caracteres = '*' * (2 * fila - 1)
    # Imprime la línea combinando espacios y asteriscos
    print(f'{espacios_en_blanco}{caracteres}')

print('*** Fin Triángulo ***\n')

# =============================================================================
# Fin de la Guía
# =============================================================================
# Esta guía integra ejemplos teóricos y prácticos sobre el uso de ciclos en Python,
# incluyendo while, for, iteración de cadenas, validaciones y ejercicios interactivos.
# Cada sección incluye comentarios detallados que explican los métodos, atributos y parámetros utilizados,
# ofreciendo así una herramienta de estudio completa para profundizar en estos temas.
