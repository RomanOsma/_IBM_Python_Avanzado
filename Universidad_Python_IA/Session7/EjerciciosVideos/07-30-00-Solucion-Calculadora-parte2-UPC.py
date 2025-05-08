print(f'*** Calculadora con Funciones ***')

def mostrar_menu():
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    opcion = int(input('Escoge una opción: '))
    return opcion

def pedir_valores():
    operando1 = float(input('Dame el valor 1: '))
    operando2 = float(input('Dame el valor 2: '))
    return operando1, operando2

def ejecutar_operacion(opcion, salir):
    # Solicitamos los valores de los operandos
    if 1 <= opcion <= 4:
        operando1, operando2 = pedir_valores()
    resultado = 0
    if opcion == 1: # Sumar
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado}\n')
    elif opcion == 2:  # Resta
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado}\n')
    elif opcion == 3:  # Multiplicacion
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicación es: {resultado}\n')
    elif opcion == 4:  # División
        resultado = operando1 / operando2
        print(f'El resultado de la división es: {resultado:.2f}\n')
    elif opcion == 5:  # Salir
        print('Saliendo del programa de Calculadora. Hasta pronto...')
        salir = True
    else:
        print('Opción inválida, selecciona otra opción...\n')
    return salir

# Programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)