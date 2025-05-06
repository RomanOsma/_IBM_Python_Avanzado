print('*** Obtener coordenadas ***')

def obtener_coordenadas():
    x, y, z = 10, 20, 30
    #return (x, y, z) # No hay necesidad de usar parentesis para definir la tupla
    return x, y, z

# Llamar la funcion
resultado = obtener_coordenadas()
print(resultado)

# Unpacking de la tupla
x1, y1, z1 = resultado

# Imprimir los valores de manera individual
print(f'Coordenada x = {x1}, Coordenada y = {y1}, Coordenada z = {z1}')



