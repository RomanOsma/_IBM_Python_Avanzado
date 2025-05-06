print('*** Anexar información Archivo ***')

nombre_archivo = 'mi_archivo.txt'

with open(nombre_archivo, 'r') as archivo:
    # Anexar informacion al archivo
    lineas=archivo.readlines()
    print(f'Impresion directa del archivo {nombre_archivo}\n')
    print(lineas)
    print(f'Impresion linea a linea {nombre_archivo}\n')
    for linea in lineas:
        print(linea)
    #strip() elimina los epacios y salto del linea
    print(f'Impresion linea a linea sin espacios{nombre_archivo}\n')
    for linea in lineas:
        print(linea.strip())
print(f'Impresion informacion dal archivo {nombre_archivo}\n')
with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())
print(f'Impresion informacion dal archivo con .read() {nombre_archivo}\n')