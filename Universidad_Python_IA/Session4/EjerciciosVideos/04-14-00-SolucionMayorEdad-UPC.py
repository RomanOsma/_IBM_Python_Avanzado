print('*** Mayor de Edad ***')

MAYOR_EDAD = 18
edad = int(input('Ingresa tu edad: '))

# Validar el valor de edad proporcionado
if edad >= MAYOR_EDAD:
    print(f'La persona con edad {edad} es mayor de edad')
else:
    print(f'La persona con edad {edad} es menor de edad')