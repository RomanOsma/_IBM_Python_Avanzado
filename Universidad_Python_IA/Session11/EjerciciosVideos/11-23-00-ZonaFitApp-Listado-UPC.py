from ClienteDao import ClienteDAO
from cliente import Cliente

print('*** Clientes Zona Fit (GYM) ***')
opcion = None
while opcion != 5:
    print(f'''Menu:
    1. Listar clientes
    2. Agregar cliente
    3. Modificar cliente
    4. Eliminar cliente
    5. Salir''')
    opcion = int(input('Escribe tu opcion (1-5): '))
    if opcion == 1:  # Listar clientes
        clientes = ClienteDAO.seleccionar()
        print('\n*** Listado de Clientes ***')
        for cliente in clientes:
            print(cliente)