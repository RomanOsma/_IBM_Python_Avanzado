# Factorial de 5!
print('*** Factorial del Número 5')


# Definir la funcion factorial recursiva
def factorial_recursivo(numero):
    # Caso base: fatorial de 0 o 1 es 1
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    # Caso recursivo, calcular factorial del numero reducido en 1
    else:
        factorial_parcial = numero * factorial_recursivo(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial


# Programa principal
if __name__ == '__main__':
    # Solicitar al usuario el numero del cual desea calcular el factorial
    numero = int(input('Proporciona el número para calcular su factorial: '))
    # Verificamos si el numero es negativo
    if numero < 0:
        print('El favtorial no está definido para números negativos')
    else:
        # Llamamos a la función factorial_recursivo para calcular el factorial
        resultado = factorial_recursivo(numero)
        print(f'El factorial de {numero} es: {resultado}')



