print('*** Usando kwargs para imprimir información ***')

# Funcion que acepta argumentos variables de tipo llave valor
def imprimir_info(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

# Llamamos a la funcion
imprimir_info(nombre='Karla', edad=30, ciudad='México')
imprimir_info(nombre='Carlos', edad=28, ciudad='Guadalajara', puesto='Gerente')