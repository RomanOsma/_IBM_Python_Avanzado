print('*** Suma Acumulada ***')

# Sumar los primeros 5 numeros
MAXIMO = 5
acumulador_suma = 0
numero = 1
while numero <= MAXIMO:
    # Imprimir lo que se va a sumar
    print(f'(acumulador_suma + numero) -> {acumulador_suma} + {numero}')
    # Ejecuta la suma iterativa o acumulada
    acumulador_suma += numero
    numero += 1
    # Imprimir el resultado parcial
    print(f'Suma parcial acumulada: {acumulador_suma}\n')

print(f'\nResultado suma acumulada: {acumulador_suma}')