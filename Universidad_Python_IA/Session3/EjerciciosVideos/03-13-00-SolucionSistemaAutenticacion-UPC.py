print('*** Sistema Autenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario_ingresado = input('Cual es tu usuario? ')
password_ingresado = input('Cual es tu password? ')

datos_correctos = (USUARIO_VALIDO == usuario_ingresado
                   and PASSWORD_VALIDO == password_ingresado)

print(f'Datos correctos? {datos_correctos}')