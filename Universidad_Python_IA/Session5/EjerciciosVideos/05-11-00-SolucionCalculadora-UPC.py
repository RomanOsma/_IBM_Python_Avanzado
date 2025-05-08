print('*** Calculadora en Python ***')
operando1 = operando2 = resultado = 0 # Definimos las variables
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')
    opcion = int(input('Escoje una opción: '))
    # Validamos que no sea la opcion 5
    #if opcion <= 1 and opcion <= 4:
    if 1 <= opcion <= 4:
        # Solicitamos los valores
        operando1 = float(input('Dame el valor 1: '))
        operando2 = float(input('Dame el valor 2: '))
    # Revisamos el tipo de operación a realizar
    if opcion == 1: # Suma
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado:.2f}\n')
    elif opcion == 2: # Resta
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado:.2f}\n')
    elif opcion == 3: # Multiplicacion
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicación es: {resultado:.2f}\n')
    elif opcion == 4: # División
        resultado = operando1 / operando2
        print(f'El resultado de la división es: {resultado:.2f}\n')
    elif opcion == 5: # Salir
        print(f'Saliendo del programa de Calculadora. Hasta pronto!')
        salir = True
    else:
        print('Opción inválida, selecciona otra opción...\n')