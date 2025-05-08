#import modulo_funcion_sumar

from modulo_funcion_sumar import sumar

if __name__ == '__main__':
    print('*** Función sumar ***')

    # Llamamos a la función saludar
    # arg1, arg2 = 5, 7
    arg1 = float(input('Proporciona el argumento 1: '))
    arg2 = float(input('Proporciona el argumento 2: '))
    resultado_suma = sumar(arg1, arg2)
    print(f'Resultado suma: {resultado_suma}')
