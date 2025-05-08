print('*** Valor Dentro Rango ***')
# Condiciones
MINIMO = 0
MAXIMO = 5

# Solicitamos un valor entre 0 y 5
dato = int(input('Proporciona un dato entre 0 y 5: '))

# Verificamos si estamos dentro de rango
#dentro_rango = dato >= MINIMO and dato <= MAXIMO
dentro_rango = MINIMO <= dato <= MAXIMO
print(f'Valor dentro de rango? {dentro_rango}')