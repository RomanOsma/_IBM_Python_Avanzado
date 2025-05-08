print(f'*** Calculadora con Funciones ***')

def mostrar_menu():
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    opcion = int(input('Escoge una opción: '))
    return opcion

def ejecutar_operacion(opcion, salir):
    pass

# Programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)