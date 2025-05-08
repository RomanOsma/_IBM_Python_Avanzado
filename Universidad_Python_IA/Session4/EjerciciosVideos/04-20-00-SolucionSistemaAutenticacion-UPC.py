print('*** Sistema de Autenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario = input('Ingresa tu usuario: ')
password = input('Ingresa tu password: ')

if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
    print('Bienvenido al Sistema...')
elif usuario == USUARIO_VALIDO:
    print('Password erroneo, favor de corregirlo!')
elif password == PASSWORD_VALIDO:
    print('Usuario erroneo, favor de corregirlo!')
else:
    print('Usuario y password erroneos, favor de corregirlos!')
