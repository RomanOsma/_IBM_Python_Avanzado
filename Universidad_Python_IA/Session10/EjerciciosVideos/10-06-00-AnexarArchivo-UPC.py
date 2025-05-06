print('*** Anexar información Archivo ***')

nombre_archivo = 'mi_archivo.txt'
#fallo queria intentar un contador para le numero de veces escrito pero debe ser realizado fuera de la llamda a la escritura y pasarlo por parametro
numero_escritura=1


with open(nombre_archivo, 'a') as archivo:
    # Anexar informacion al archivo
    numero_escritura +=1
    archivo.write('Anexando informacion ... \n')
    archivo.write('Saliendo de anexar informacion...\n')
    archivo.write(f'Numero de escrituras {numero_escritura}...\n')

print(f'Se ha anexado informacion al archivo {nombre_archivo}')
