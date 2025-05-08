print('*** Expresiones Generadores ***')

generador = (x**2 for x in range(10) if x % 2 == 0)

for cuadrado_pares in generador:
    print(cuadrado_pares)