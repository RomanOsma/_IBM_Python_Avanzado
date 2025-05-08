print('*** El mayor de dos números ***')

numero1 = int(input('Proporciona el número 1: '))
numero2 = int(input('Proporciona el número 2: '))

# El mayor de dos números
# if numero1 > numero2:
#     print(f'El número 1 es mayor: {numero1}' )
# else:
#     print(f'El número 2 es mayor: {numero2}')

# El mayor de dos numeros pero usando el operador ternario
resultado = "Número 1" if numero1 > numero2 else "Número 2"
print(f'El mayor de los dos números es: {resultado}')