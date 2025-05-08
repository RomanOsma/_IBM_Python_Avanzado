
# Escribe una función llamada contar_vocales que tome una cadena de texto 
# como parámetro y devuelva el número de vocales (a, e, i, o, u) que contiene. 
# Ignora mayúsculas y minúsculas.


def contar_vocales(texto):
    texto = texto.lower()
    vocales = "aeiou"
    return sum(1 for letra in texto if letra in vocales)

# Llamada a la función
print(contar_vocales("Hola Mundo"))  # 4
