


# Abrir en modo lectura
archivo = open("880_Open.txt", "r")

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
