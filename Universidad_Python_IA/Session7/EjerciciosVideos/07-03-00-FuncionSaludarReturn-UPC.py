print('*** Manejo de Funciones ***')

# 1. Definir una funcion llamada saludar
def saludar(mensaje):
    print(f'Mensaje recibido: {mensaje}')
    return 'Terminó ok la ejecución de la función saludar'

# 2. Llamar la funcion (ya tiene que estar definida)
argumento = 'Hola desde la función saludar'
valor_devuelto = saludar(argumento)
print(f'Valor devuelto de la función: {valor_devuelto}')