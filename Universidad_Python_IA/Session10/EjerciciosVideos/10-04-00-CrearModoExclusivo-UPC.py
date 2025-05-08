print('*** Abrir un archivo en modo exclusivo ***')

nombre_archivo = 'mi_archivo.txt'
try:
    with open(nombre_archivo, 'x') as archivo:
        archivo.write('Escritura en modo exclusivo\n')
        archivo.write('Espero te sea util\n')
    print(f'Se ha creado el archivo {nombre_archivo}')
except FileExistsError as e:
    print(f'El archivo {nombre_archivo} ya existe ')
    print(f'Detalle del error: {e}')