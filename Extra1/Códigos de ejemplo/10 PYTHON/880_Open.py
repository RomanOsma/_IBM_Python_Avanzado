
# Sintaxis básica

# archivo = open("nombre_del_archivo.txt", "modo")

# Modo	Significado
# 'r'	Leer (read) - ❌ Error si no existe
# 'w'	Escribir (write) - 🧨 Borra el archivo si existe
# 'a'	Añadir (append) - Añade al final
# 'x'	Crear (exclusive) - ❌ Error si ya existe
# 'b'	Modo binario (para imágenes, etc.)
# 't'	Modo texto (por defecto)


# Abrir en modo lectura
archivo = open("880_Open copy.txt", "r")

# Leer todo el contenido
contenido = archivo.read()
print(contenido)

# Cerrar el archivo
archivo.close()
# 🧠 Siempre hay que cerrar el archivo con close() para liberar recursos.

# ✅ Mejor forma: with open(...) as
# Este método cierra automáticamente el archivo, incluso si hay errores.

with open("notas.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# 🧪 Ejemplo 2: Escribir en un archivo

with open("nueva_nota.txt", "w") as archivo:
    archivo.write("Primera línea.\n")
    archivo.write("Segunda línea.")
# ⚠️ Si el archivo ya existía, se sobrescribe.

# 🧪 Ejemplo 3: Añadir contenido

with open("nueva_nota.txt", "a") as archivo:
    archivo.write("\nTercera línea (añadida).")


# 🧪 Ejemplo 4: Leer línea por línea

with open("nueva_nota.txt", "r") as archivo:
    for linea in archivo:
        print("Línea:", linea.strip())


# 🧪 Ejemplo 5: Leer todas las líneas en una lista

with open("nueva_nota.txt", "r") as archivo:
    lineas = archivo.readlines()

print(lineas)
# Resultado: ['Primera línea.\n', 'Segunda línea.', 'Tercera línea (añadida).']


# 🧪 Ejemplo 6: Capturar error si el archivo no existe

try:
    with open("no_existe.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("Ese archivo no existe.")


# 💡 Truquito: Comprobar si un archivo existe antes

import os

if os.path.exists("notas.txt"):
    print("El archivo existe.")
else:
    print("El archivo no existe.")