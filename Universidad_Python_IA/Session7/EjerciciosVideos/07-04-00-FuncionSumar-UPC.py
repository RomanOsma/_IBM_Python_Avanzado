print('*** Función sumar ***')

# Definición de la función sumar
def sumar(a, b):
    resultado = a + b
    return resultado

# Llamamos a la función saludar
#arg1, arg2 = 5, 7
arg1 = float(input('Proporciona el argumento 1: '))
arg2 = float(input('Proporciona el argumento 2: '))
resultado_suma = sumar(arg1, arg2)
print(f'Resultado suma: {resultado_suma}')

