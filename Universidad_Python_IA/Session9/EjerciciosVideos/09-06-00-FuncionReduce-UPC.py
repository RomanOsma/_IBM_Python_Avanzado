from functools import reduce

print('*** Funciones Lambda ***')

# Funcion cuadrado sin usar lambda
def cuadrado(x):
    return x ** 2

print(f'El cuadrado de 5: {cuadrado(5)}')

# Funcion lambda (anonima)

cuadrado_lambda = lambda x: x ** 2
print(f'El cuadrado de 2: {cuadrado_lambda(2)}')
print(f'El cuadrado de 4: {cuadrado_lambda(4)}')


# Con map y lambda
# Creamos una lista de numeros
numeros = [1, 2, 3, 4, 5]

# Aplicar una funcion lambda para obtener el cuadrado de cada numero

cuadrados = list(map(lambda x: x ** 2, numeros))
print(f'Resultado de usar map y lambda: {cuadrados}')

# Con filter y lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f'Resultado de usar filter para filtrar numeros pares: {pares}')

# reduce y map
suma_acumulativa = reduce(lambda x, y: x + y, numeros)
print(f'Suma acumulativa aplicando reduce: {suma_acumulativa}')