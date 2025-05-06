print('*** Manejo de Excepciones ***')

def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        print(f'Resultado de la división: {resultado}')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    finally:
        print(f'Terminamos de procesar la excepcion\n')
    # except ZeroDivisionError:
    #     print('Error: No se puede dividir entre cero')
    # except TypeError:
    #     print('Error: Los operandos deben ser numericos')

# Ejemplo de uso
dividir(10, 2)
dividir(10, 0)
dividir(10, '0')
