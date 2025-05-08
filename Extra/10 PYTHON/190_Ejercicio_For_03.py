

# Escribe un programa que solicite al usuario una cadena de texto y luego imprima cada 
# carácter de la cadena junto con su frecuencia (cuántas veces aparece en la cadena). 
# Utiliza un diccionario para almacenar las frecuencias.


cadena = input("Introduce una cadena de texto: ")
frecuencias = {}

for caracter in cadena:
    if caracter in frecuencias:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1

for caracter, frecuencia in frecuencias.items():
    print(f"'{caracter}': {frecuencia} veces")