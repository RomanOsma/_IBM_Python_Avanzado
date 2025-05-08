"""
Explora los Metacaracteres Fundamentales en Expresiones Regulares (Regex) con Python.

Este script se centra en los símbolos especiales (metacaracteres) que tienen un
significado particular dentro de las expresiones regulares y cómo usarlos con
el módulo 're' de Python.

Metacaracteres cubiertos:
- .       (Punto): Cualquier carácter excepto nueva línea.
- \       (Barra invertida): Escapa caracteres especiales o introduce secuencias especiales.
- \d, \D  (Dígito / No dígito).
- \w, \W  (Alfanumérico / No alfanumérico).
- \s, \S  (Espacio en blanco / No espacio en blanco).
- ^       (Ancla de inicio): Coincide con el inicio de la cadena/línea.
- $       (Ancla de fin): Coincide con el final de la cadena/línea.
- \b, \B  (Límite de palabra / No límite de palabra).
- |       (OR lógico): Coincide con una alternativa u otra.

Funciones 're' utilizadas:
- re.findall(): Encuentra todas las coincidencias no solapadas.
- re.search(): Encuentra la primera coincidencia en la cadena.
- re.sub(): Reemplaza texto que coincide con un patrón (usado en ejercicios).

Se incluyen ejemplos variados y una sección de ejercicios al final.
Es recomendable usar raw strings (r"...") para definir los patrones regex
para evitar problemas con las barras invertidas.
"""

import re
from os import system

# Limpiar consola para mejor visualización (opcional)
if system("clear") != 0: system("cls")

print("\n--- Explorando Metacaracteres en Expresiones Regulares ---")

# --- 1. El Punto (.) ---
# Coincide con cualquier carácter individual, excepto un salto de línea (\n).
print("\n--- 1. El Punto (.) ---")
text_punto = "Hola H0la H_la H@la H la H\nla" # H\nla no coincidirá
pattern_punto = r"H.la" # Busca 'H', seguido de CUALQUIER carácter, seguido de 'la'

matches_punto = re.findall(pattern_punto, text_punto)
print(f"Texto: '{text_punto}'")
print(f"Patrón: '{pattern_punto}'")
print(f"Coincidencias (.): {matches_punto}") # Output: ['Hola', 'H0la', 'H_la', 'H@la', 'H la']

text_variado = "casa cosa cuna cesa c*sa c sa"
pattern_variado = r"c.sa"
matches_variado = re.findall(pattern_variado, text_variado)
print(f"\nTexto: '{text_variado}'")
print(f"Patrón: '{pattern_variado}'")
print(f"Coincidencias (.): {matches_variado}") # Output: ['casa', 'cosa', 'cesa', 'c*sa', 'c sa']

# --- 2. La Barra Invertida (\) ---
# Se usa para dos propósitos principales:
# a) Escapar metacaracteres: Para buscar el carácter literal en lugar de su significado especial.
# b) Introducir secuencias especiales: Como \d, \w, \s, \b, etc.
print("\n--- 2. La Barra Invertida (\\) ---")

# a) Escapar metacaracteres: Buscar un punto literal.
text_escape = "El precio es $19.99. ¡Oferta!"
pattern_escape_punto = r"\." # Busca el carácter '.' literalmente
matches_escape_punto = re.findall(pattern_escape_punto, text_escape)
print(f"Texto: '{text_escape}'")
print(f"Patrón: '{pattern_escape_punto}' (escapando el punto)")
print(f"Coincidencias (\\. literal): {matches_escape_punto}") # Output: ['.', '.']

pattern_escape_dolar = r"\$" # Busca el carácter '$' literalmente
matches_escape_dolar = re.search(pattern_escape_dolar, text_escape)
if matches_escape_dolar:
    print(f"Patrón: '{pattern_escape_dolar}' (escapando el dólar)")
    print(f"Primera coincidencia (\\$ literal): '{matches_escape_dolar.group()}'") # Output: '$'

# b) Introducir secuencias especiales (se ven a continuación)

# --- 3. Secuencias de Caracteres Comunes ---
print("\n--- 3. Secuencias de Caracteres (\\d, \\w, \\s y sus opuestos) ---")

# \d: Coincide con cualquier dígito decimal (0-9). Es equivalente a [0-9].
# \D: Coincide con cualquier carácter que NO sea un dígito decimal. Es equivalente a [^0-9].
text_digitos = "Pedido 123 completado. Ref: AB456."
pattern_digitos = r"\d"
pattern_no_digitos = r"\D"
matches_digitos = re.findall(pattern_digitos, text_digitos)
matches_no_digitos = re.findall(pattern_no_digitos, text_digitos)
print(f"Texto: '{text_digitos}'")
print(f"Coincidencias (\\d): {matches_digitos}") # Output: ['1', '2', '3', '4', '5', '6']
print(f"Coincidencias (\\D): {matches_no_digitos}") # Output: ['P', 'e', 'd', 'i', 'd', 'o', ' ', ' ', 'c', 'o', 'm', 'p', 'l', 'e', 't', 'a', 'd', 'o', '.', ' ', 'R', 'e', 'f', ':', ' ', 'A', 'B', '.']

# Ejemplo práctico con \d: Encontrar un número de teléfono (formato simple)
text_telefono = "Llama al 987654321 o al 123-456-789. También +34 654321987."
# Usamos \d{9} para 9 dígitos seguidos y \d{3}-\d{3}-\d{3} para el formato con guiones.
# También buscamos el formato internacional simple +34 seguido de 9 dígitos.
# Nota: {n} es un cuantificador (se verá en detalle más adelante). | significa OR.
pattern_telefono = r"\d{9}|\d{3}-\d{3}-\d{3}|\+\d{2}\s\d{9}"
matches_telefono = re.findall(pattern_telefono, text_telefono)
print(f"\nTexto: '{text_telefono}'")
print(f"Patrón: '{pattern_telefono}'")
print(f"Números encontrados (\\d y cuantificadores): {matches_telefono}") # Output: ['987654321', '123-456-789', '+34 654321987']

# \w: Coincide con cualquier carácter alfanumérico (letras a-z, A-Z, dígitos 0-9) y el guion bajo (_).
#    Es equivalente a [a-zA-Z0-9_].
# \W: Coincide con cualquier carácter que NO sea alfanumérico ni guion bajo. Es equivalente a [^a-zA-Z0-9_].
text_alfanum = "user_name@example.com #tag123"
pattern_alfanum = r"\w"
pattern_no_alfanum = r"\W"
matches_alfanum = re.findall(pattern_alfanum, text_alfanum)
matches_no_alfanum = re.findall(pattern_no_alfanum, text_alfanum)
print(f"\nTexto: '{text_alfanum}'")
print(f"Coincidencias (\\w): {matches_alfanum}") # Letras, números y _
print(f"Coincidencias (\\W): {matches_no_alfanum}") # @ . # espacio

# \s: Coincide con cualquier carácter de espacio en blanco (espacio, tabulación \t, nueva línea \n, retorno de carro \r, etc.).
# \S: Coincide con cualquier carácter que NO sea un espacio en blanco.
text_espacios = "Hola\tmundo\n¿Cómo estás?"
pattern_espacios = r"\s"
pattern_no_espacios = r"\S"
matches_espacios = re.findall(pattern_espacios, text_espacios)
matches_no_espacios = re.findall(pattern_no_espacios, text_espacios)
print(f"\nTexto: '{text_espacios}' (con tab y nueva línea)")
print(f"Coincidencias (\\s): {matches_espacios}") # Output: ['\t', '\n', ' ']
print(f"Coincidencias (\\S): {matches_no_espacios}") # Output: ['H', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o', '¿', 'C', 'ó', 'm', 'o', 'e', 's', 't', 'á', 's', '?']

# --- 4. Anclas (^ y $) ---
# No coinciden con caracteres, sino con posiciones en la cadena.
print("\n--- 4. Anclas (^ y $) ---")

# ^: Coincide con el inicio de la cadena (o el inicio de una línea en modo multilínea).
text_inicio = "Python es genial\nJava también mola"
pattern_inicio = r"^Python" # Busca "Python" solo si está al principio de la cadena

match_inicio = re.search(pattern_inicio, text_inicio)
if match_inicio:
    print(f"Texto: '{text_inicio}'")
    print(f"Patrón: '{pattern_inicio}'")
    print(f"Coincidencia (^): '{match_inicio.group()}' encontrada al inicio.")
else:
    print(f"Patrón '{pattern_inicio}' no encontrado al inicio de '{text_inicio}'")

pattern_no_inicio = r"^Java"
match_no_inicio = re.search(pattern_no_inicio, text_inicio)
if not match_no_inicio:
    print(f"Patrón '{pattern_no_inicio}' NO encontrado al inicio de la cadena principal.")

# $: Coincide con el final de la cadena (o el final de una línea en modo multilínea).
text_fin = "El código termina aquí."
pattern_fin = r"aquí\.$" # Busca "aquí." solo si está al final de la cadena (escapamos el '.')

match_fin = re.search(pattern_fin, text_fin)
if match_fin:
    print(f"\nTexto: '{text_fin}'")
    print(f"Patrón: '{pattern_fin}'")
    print(f"Coincidencia ($): '{match_fin.group()}' encontrada al final.")
else:
    print(f"Patrón '{pattern_fin}' no encontrado al final de '{text_fin}'")

# Combinando ^ y $: Para asegurar que toda la cadena coincida con el patrón.
text_completo = "12345"
# Nota: + es un cuantificador (1 o más), se verá en detalle más adelante.
pattern_completo_digitos = r"^\d+$" # La cadena debe contener solo dígitos, de principio a fin

match_completo = re.search(pattern_completo_digitos, text_completo)
if match_completo:
    print(f"\nTexto: '{text_completo}' coincide completamente con el patrón '{pattern_completo_digitos}'.")
else:
    print(f"\nTexto: '{text_completo}' NO coincide completamente con '{pattern_completo_digitos}'.")

text_no_completo = "123a45"
match_no_completo = re.search(pattern_completo_digitos, text_no_completo)
if not match_no_completo:
    print(f"Texto: '{text_no_completo}' NO coincide completamente con '{pattern_completo_digitos}'.")


# --- 5. Límites de Palabra (\b y \B) ---
# \b: Coincide con una posición de límite de palabra. Es una posición entre un \w y un \W (o viceversa),
#     o entre \w y el inicio/fin de la cadena. No consume caracteres.
# \B: Coincide con una posición que NO es un límite de palabra.
print("\n--- 5. Límites de Palabra (\\b y \\B) ---")

text_limites = "El casamiento fue casualidad, no una casa."
pattern_limite = r"\bcas" # Busca "cas" al inicio de una palabra
pattern_no_limite = r"\Bcas" # Busca "cas" que NO esté al inicio de una palabra

matches_limite = re.findall(pattern_limite, text_limites)
matches_no_limite = re.findall(pattern_no_limite, text_limites)

print(f"Texto: '{text_limites}'")
print(f"Coincidencias (\\bcas): {matches_limite}") # Output: ['cas', 'cas', 'cas'] (casamiento, casualidad, casa)
print(f"Coincidencias (\\Bcas): {matches_no_limite}") # Output: [] (no hay 'cas' dentro de una palabra)

# Ejemplo buscando palabra completa "casa":
pattern_palabra_completa = r"\bcasa\b" # Busca la palabra exacta "casa"
matches_palabra_completa = re.findall(pattern_palabra_completa, text_limites)
print(f"Coincidencias (\\bcasa\\b): {matches_palabra_completa}") # Output: ['casa']

# --- 6. Alternancia (|) ---
# Actúa como un operador OR lógico. Coincide con la expresión de la izquierda O la de la derecha.
print("\n--- 6. Alternancia (|) ---")

text_alternancia = "Me gusta el perro, el gato y el loro."
pattern_alternancia = r"perro|gato|canario" # Busca "perro" O "gato" O "canario"

matches_alternancia = re.findall(pattern_alternancia, text_alternancia)
print(f"Texto: '{text_alternancia}'")
print(f"Patrón: '{pattern_alternancia}'")
print(f"Coincidencias (|): {matches_alternancia}") # Output: ['perro', 'gato']

# Ejemplo más complejo: encontrar 'apple', 'banana' o cualquier palabra de 4 letras
text_frutas = "apple banana kiwi pear grape"
# Nota: {4} es un cuantificador (exactamente 4 veces), se verá en detalle más adelante.
pattern_frutas_varias = r"apple|banana|\b\w{4}\b" # apple O banana O palabra de 4 letras

matches_frutas_varias = re.findall(pattern_frutas_varias, text_frutas)
print(f"\nTexto: '{text_frutas}'")
print(f"Patrón: '{pattern_frutas_varias}'")
print(f"Coincidencias (| y \\w{{4}}): {matches_frutas_varias}") # Output: ['apple', 'banana', 'kiwi', 'pear']

# --- Comparación con Métodos de String ---
# Python tiene métodos como `find()`, `startswith()`, `endswith()`, `isdigit()`, etc.
# Para tareas simples (buscar una subcadena exacta, verificar inicio/fin),
# estos métodos suelen ser más legibles y eficientes.
# Regex brilla cuando necesitas patrones complejos, flexibilidad, o buscar
# múltiples variaciones a la vez (ej. validar emails, extraer números con formatos
# específicos, encontrar diferentes palabras clave).

###
# EJERCICIOS (Metacaracteres)
# Pon en práctica lo aprendido sobre metacaracteres.
# Nota: Algunos ejercicios usan cuantificadores (+, {n}) que se explican formalmente
# en el siguiente archivo (357_quantifiers-t.py), pero son útiles aquí.
# Descomenta las soluciones para verificar tus respuestas.
###

# Ejercicio 1: Encontrar todas las palabras que terminan en "ar"
# Usa \b y un patrón que termine en "ar". \w+ significa uno o más caracteres alfanuméricos.
print("\n--- EJERCICIOS ---")
print("\nEjercicio 1: Palabras que terminan en 'ar'")
texto_ej1 = "Cantar, bailar, jugar, programar, reir, amar."
# patron_ej1 = r"\b\w+ar\b" # \w+ (cuantificador) significa uno o más caracteres alfanuméricos
# solucion_ej1 = re.findall(patron_ej1, texto_ej1)
# print(f"Texto: '{texto_ej1}'")
# print(f"Palabras terminadas en 'ar': {solucion_ej1}") # Esperado: ['Cantar', 'bailar', 'jugar', 'programar', 'amar']

# Ejercicio 2: Validar un código postal simple (5 dígitos)
# Usa ^, $, y \d{5} (cuantificador) para asegurar que la cadena completa sea exactamente 5 dígitos.
print("\nEjercicio 2: Validar Código Postal (5 dígitos)")
codigos_ej2 = ["12345", "abcde", "1234", "123456", "12-345"]
# patron_ej2 = r"^\d{5}$" # \d{5} (cuantificador) significa exactamente 5 dígitos
# for codigo in codigos_ej2:
#     if re.search(patron_ej2, codigo):
#         print(f"'{codigo}' es un CP válido.")
#     else:
#         print(f"'{codigo}' NO es un CP válido.")
# Esperado: 12345 válido, los demás no.

# Ejercicio 3: Extraer hashtags
# Un hashtag empieza con # seguido de caracteres alfanuméricos (\w+).
print("\nEjercicio 3: Extraer Hashtags")
texto_ej3 = "Me encanta #Python y #Regex! Son #geniales123."
# patron_ej3 = r"#\w+" # \w+ (cuantificador) significa uno o más caracteres alfanuméricos
# solucion_ej3 = re.findall(patron_ej3, texto_ej3)
# print(f"Texto: '{texto_ej3}'")
# print(f"Hashtags encontrados: {solucion_ej3}") # Esperado: ['#Python', '#Regex', '#geniales123']

# Ejercicio 4: Encontrar "Error" o "Warning" al inicio de una línea
# Usa ^ y | y el flag re.MULTILINE para que ^ funcione por línea.
print("\nEjercicio 4: Encontrar 'Error' o 'Warning' al inicio de línea")
log_ej4 = """
Info: Proceso iniciado.
Warning: Disco casi lleno.
Error: No se pudo conectar.
Info: Proceso finalizado.
Error: Fallo crítico.
"""
# patron_ej4 = r"^(Error|Warning)" # Necesitamos el flag re.MULTILINE para que ^ funcione por línea
# solucion_ej4 = re.findall(patron_ej4, log_ej4, flags=re.MULTILINE)
# print(f"Log:\n{log_ej4}")
# print(f"Líneas que empiezan con Error o Warning: {solucion_ej4}") # Esperado: ['Warning', 'Error', 'Error']

# Ejercicio 5: Reemplazar espacios múltiples por uno solo
# Usa \s+ (cuantificador + para 1 o más espacios) y re.sub().
print("\nEjercicio 5: Reemplazar espacios múltiples")
texto_ej5 = "Muchos    espacios   aquí.   Y  aquí   también."
# patron_ej5 = r"\s+" # \s+ (cuantificador) significa uno o más espacios en blanco
# reemplazo_ej5 = " "
# solucion_ej5 = re.sub(patron_ej5, reemplazo_ej5, texto_ej5)
# print(f"Original: '{texto_ej5}'")
# print(f"Corregido: '{solucion_ej5}'") # Esperado: 'Muchos espacios aquí. Y aquí también.'

# Ejercicio 6: Encontrar archivos .txt
# Dada una cadena con nombres de archivo, extrae solo los que terminan en ".txt".
# Usa \w, \., y $
print("\nEjercicio 6: Encontrar archivos .txt")
files_ej6 = "file1.txt file2.pdf midu-of.webp secret.txt report.txt.zip"
# patron_ej6 = r"\b[\w-]+\.txt\b" # \b para límite de palabra, [\w-]+ para nombre (incluye guiones), \. para punto literal, txt, \b
# solucion_ej6 = re.findall(patron_ej6, files_ej6)
# print(f"Archivos: '{files_ej6}'")
# print(f"Archivos .txt encontrados: {solucion_ej6}") # Esperado: ['file1.txt', 'secret.txt']
