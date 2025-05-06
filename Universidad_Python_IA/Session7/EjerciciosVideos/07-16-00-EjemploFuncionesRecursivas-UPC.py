print('*** Imprimir del 1 al 5 de forma recursiva ***')


# Definir la funcion recursiva
def funcion_recursiva(numero):
    # Caso Base
    if numero == 1:
        print(numero, end=' ')
    else:  # Caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=' ')


# Programa principal
if __name__ == '__main__':
    funcion_recursiva(5)
