print('*** Dibujar Triángulo Simétrico ***')

numero_de_filas = int(input('Proporciona el número de filas: '))

# Iterar sobre cada fila del triángulo
for fila in range(1, numero_de_filas + 1):
    espacios_en_blanco = " " * (numero_de_filas - fila) # Calculo de la cantidad de espacios en blanco
    caracteres = '*' * (2 * fila - 1) # Calcular la cantidad de caracteres para la fila actual
    print(f'{espacios_en_blanco}{caracteres}') # Imprimiendo espacios y asteriscos