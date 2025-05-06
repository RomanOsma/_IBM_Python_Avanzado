# Generador ID Unico
# import random
from random import randint

print('*** Sistema Generador de ID Unico ***')
nombre = input('Cual es tu nombre? ')
nombre_2 = nombre[0:2].upper()
apellido = input('Cual es tu apellido? ')
apellido_2 = apellido[0:2].upper()
anio_nacimiento = input('Cual es tu año de nacimiento (YYYY)? ')  # Y - year
anio_nacimiento_2 = anio_nacimiento[2:4]
# Generar un valor aleatorio de 4 digitos
aleatorio = randint(1000, 9999)
# Generamos el id unico
id_unico = f'{nombre_2}{apellido_2}{anio_nacimiento_2}{aleatorio}'
print(f'''\nHola {nombre}, 
    Tu nuevo número de identificación (ID) generado por el sistema es:
    {id_unico}
    Felicidades!''')


