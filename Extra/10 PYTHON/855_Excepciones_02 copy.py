print('*** Manejo de Excepciones ***')

def dividir(numerador, denominador):

    resultado = numerador / denominador
    print(f'Resultado de la división: {resultado}')


# Ejemplo de uso
dividir(10, 2)
dividir(10, 0)
dividir(10, '0')
print("El programa sigue")