"""
Explora los Cuantificadores en Expresiones Regulares (Regex) con Python.

Este script se centra en los cuantificadores, que permiten especificar cuántas
veces debe aparecer un carácter, grupo o clase de caracteres para que haya
una coincidencia.

Cuantificadores cubiertos:
- *       (Asterisco): 0 o más veces.
- +       (Más): 1 o más veces.
- ?       (Interrogación): 0 o 1 vez (opcional).
- {n}     (Llaves n): Exactamente n veces.
- {n,}    (Llaves n,): Al menos n veces.
- {n,m}   (Llaves n, m): Entre n y m veces (inclusive).
- Modificador '?' (Lazy/Non-Greedy): Hace que los cuantificadores *, +, ?
  coincidan con la menor cantidad posible de caracteres.

Funciones 're' utilizadas:
- re.findall(): Encuentra todas las coincidencias no solapadas.
- re.search(): Encuentra la primera coincidencia en la cadena.

Se incluyen ejemplos variados y una sección de ejercicios al final.
Es recomendable usar raw strings (r"...") para definir los patrones regex.
"""

import re
from os import system

# Limpiar consola para mejor visualización (opcional)
if system("clear") != 0: system("cls")

print("\n--- Explorando Cuantificadores en Expresiones Regulares ---")

# --- 1. El Asterisco (*) ---
# Coincide con el elemento precedente 0 o más veces. Es "codicioso" (greedy) por defecto.
print("\n--- 1. El Asterisco (*) - 0 o más veces ---")
text_asterisco = "aaabaac a"
pattern_asterisco = r"a*" # Busca secuencias de cero o más 'a'

# Explicación de findall con *:
# 'aaabaac a'
# 1. Encuentra 'aaa' al inicio.
# 2. Después de 'aaa', encuentra 'b'. Antes de 'b', coincide con cero 'a' -> ''.
# 3. Después de 'b', encuentra 'aa'. Coincide con 'aa'.
# 4. Después de 'aa', encuentra 'c'. Antes de 'c', coincide con cero 'a' -> ''.
# 5. Después de 'c', encuentra ' '. Antes de ' ', coincide con cero 'a' -> ''.
# 6. Después de ' ', encuentra 'a'. Coincide con 'a'.
# 7. Después de 'a', llega al final. Coincide con cero 'a' -> ''.
matches_asterisco = re.findall(pattern_asterisco, text_asterisco)
print(f"Texto: '{text_asterisco}'")
print(f"Patrón: '{pattern_asterisco}'")
print(f"Coincidencias (*): {matches_asterisco}") # Output: ['aaa', '', 'aa', '', '', 'a', '']

# Ejemplo práctico: Encontrar 'file' seguido de un dígito y cero o más espacios
text_files = "file1 file2  file3 file4"
pattern_files = r"file\d\s*" # \s* -> cero o más espacios
matches_files = re.findall(pattern_files, text_files)
print(f"\nTexto: '{text_files}'")
print(f"Patrón: '{pattern_files}'")
print(f"Coincidencias (\\s*): {matches_files}") # Output: ['file1 ', 'file2  ', 'file3 ', 'file4']

# --- 2. El Signo Más (+) ---
# Coincide con el elemento precedente 1 o más veces. Es "codicioso" (greedy) por defecto.
print("\n--- 2. El Signo Más (+) - 1 o más veces ---")
text_mas = "dddd aaa ccc a bb aa casa"
pattern_mas = r"a+" # Busca secuencias de una o más 'a'

matches_mas = re.findall(pattern_mas, text_mas)
print(f"Texto: '{text_mas}'")
print(f"Patrón: '{pattern_mas}'")
print(f"Coincidencias (+): {matches_mas}") # Output: ['aaa', 'a', 'aa', 'a', 'a']

# Ejemplo práctico: Encontrar secuencias de dígitos
text_numeros = "ID: 123, Qty: 4, Code: 5678, Zip: 9"
pattern_numeros = r"\d+" # \d+ -> uno o más dígitos
matches_numeros = re.findall(pattern_numeros, text_numeros)
print(f"\nTexto: '{text_numeros}'")
print(f"Patrón: '{pattern_numeros}'")
print(f"Coincidencias (\\d+): {matches_numeros}") # Output: ['123', '4', '5678', '9']

# --- 3. La Interrogación (?) ---
# Coincide con el elemento precedente 0 o 1 vez (lo hace opcional).
# También se usa para hacer cuantificadores "no codiciosos" (ver sección 7).
print("\n--- 3. La Interrogación (?) - 0 o 1 vez ---")
text_interrogacion = "color colour favor flavour"
pattern_interrogacion = r"colou?r" # La 'u' es opcional

matches_interrogacion = re.findall(pattern_interrogacion, text_interrogacion)
print(f"Texto: '{text_interrogacion}'")
print(f"Patrón: '{pattern_interrogacion}'")
print(f"Coincidencias (?): {matches_interrogacion}") # Output: ['color', 'colour']

# Ejemplo práctico: Hacer opcional un prefijo (+34) en números de teléfono
text_phones = "+34 688999999 and 677888888"
# (\+34\s)? -> El grupo (+34 seguido de espacio) es opcional
pattern_phones = r"(\+34\s)?\d{9}" # \d{9} -> exactamente 9 dígitos
matches_phones = re.findall(pattern_phones, text_phones)
print(f"\nTexto: '{text_phones}'")
print(f"Patrón: '{pattern_phones}'")
# findall con grupos devuelve solo el contenido de los grupos si existen.
# Para obtener la coincidencia completa, usar finditer o search.
print(f"Grupos opcionales encontrados (?): {matches_phones}") # Output: ['+34 ', '']

# Usando finditer para ver la coincidencia completa:
matches_phones_iter = re.finditer(pattern_phones, text_phones)
print("Coincidencias completas (finditer):")
for match in matches_phones_iter:
    print(f"  - '{match.group(0)}'") # group(0) es la coincidencia completa

# --- 4. Llaves {n} ---
# Coincide con el elemento precedente exactamente n veces.
print("\n--- 4. Llaves {n} - Exactamente n veces ---")
text_llaves_n = "aaaaaa bb aaa cccc aaaa"
pattern_llaves_n = r"a{3}" # Busca exactamente tres 'a' seguidas

matches_llaves_n = re.findall(pattern_llaves_n, text_llaves_n)
print(f"Texto: '{text_llaves_n}'")
print(f"Patrón: '{pattern_llaves_n}'")
print(f"Coincidencias ({{n}}): {matches_llaves_n}") # Output: ['aaa', 'aaa', 'aaa', 'aaa'] (dos en 'aaaaaa', una en 'aaa', una en 'aaaa')

# Ejemplo práctico: Validar un código postal de 5 dígitos
text_zip = "Zip: 12345, Invalid: 9876, Valid: 54321, Too long: 123456"
pattern_zip = r"\b\d{5}\b" # \b -> límite de palabra, \d{5} -> 5 dígitos
matches_zip = re.findall(pattern_zip, text_zip)
print(f"\nTexto: '{text_zip}'")
print(f"Patrón: '{pattern_zip}'")
print(f"Coincidencias (\\d{{5}}): {matches_zip}") # Output: ['12345', '54321']

# --- 5. Llaves {n,} ---
# Coincide con el elemento precedente al menos n veces. Es "codicioso" (greedy).
print("\n--- 5. Llaves {n,} - Al menos n veces ---")
text_llaves_n_coma = "aa aaaa aaaaaa a"
pattern_llaves_n_coma = r"a{3,}" # Busca secuencias de 3 o más 'a'

matches_llaves_n_coma = re.findall(pattern_llaves_n_coma, text_llaves_n_coma)
print(f"Texto: '{text_llaves_n_coma}'")
print(f"Patrón: '{pattern_llaves_n_coma}'")
print(f"Coincidencias ({{n,}}): {matches_llaves_n_coma}") # Output: ['aaaa', 'aaaaaa']

# Ejemplo práctico: Encontrar palabras de 6 o más letras
text_palabras_largas = "ala fantastico casa árbol león cinco murcielago programacion"
pattern_palabras_largas = r"\b\w{6,}\b" # \w{6,} -> 6 o más caracteres alfanuméricos
matches_palabras_largas = re.findall(pattern_palabras_largas, text_palabras_largas)
print(f"\nTexto: '{text_palabras_largas}'")
print(f"Patrón: '{pattern_palabras_largas}'")
print(f"Coincidencias (\\w{{6,}}): {matches_palabras_largas}") # Output: ['fantastico', 'murcielago', 'programacion']

# --- 6. Llaves {n,m} ---
# Coincide con el elemento precedente entre n y m veces (inclusive). Es "codicioso" (greedy).
print("\n--- 6. Llaves {n,m} - Entre n y m veces ---")
text_llaves_n_m = "u uu uuu uuuu uuuuu"
pattern_llaves_n_m = r"u{2,3}" # Busca secuencias de 2 o 3 'u'

matches_llaves_n_m = re.findall(pattern_llaves_n_m, text_llaves_n_m)
print(f"Texto: '{text_llaves_n_m}'")
print(f"Patrón: '{pattern_llaves_n_m}'")
# Explicación:
# 'u' -> no coincide
# 'uu' -> coincide con 'uu'
# 'uuu' -> coincide con 'uuu'
# 'uuuu' -> coincide con 'uuu' (greedy), queda 'u' que no coincide
# 'uuuuu' -> coincide con 'uuu' (greedy), queda 'uu' que coincide con 'uu'
print(f"Coincidencias ({{n,m}}): {matches_llaves_n_m}") # Output: ['uu', 'uuu', 'uuu', 'uuu', 'uu']

# Ejemplo práctico: Encontrar palabras de 4 a 6 letras
text_palabras_nm = "ala casa árbol león cinco murcielago sol"
pattern_palabras_nm = r"\b\w{4,6}\b" # \w{4,6} -> entre 4 y 6 caracteres alfanuméricos
matches_palabras_nm = re.findall(pattern_palabras_nm, text_palabras_nm)
print(f"\nTexto: '{text_palabras_nm}'")
print(f"Patrón: '{pattern_palabras_nm}'")
print(f"Coincidencias (\\w{{4,6}}): {matches_palabras_nm}") # Output: ['casa', 'árbol', 'león', 'cinco']

# --- 7. Cuantificadores Codiciosos (Greedy) vs. No Codiciosos (Lazy/Non-Greedy) ---
# Por defecto, los cuantificadores *, +, ?, {n,}, {n,m} son "codiciosos": intentan
# coincidir con la mayor cantidad posible de texto.
# Añadiendo un '?' después del cuantificador, se vuelven "no codiciosos" o "perezosos":
# intentan coincidir con la menor cantidad posible de texto.
print("\n--- 7. Codicioso (Greedy) vs. No Codicioso (Lazy) ---")

text_html = "<div>Contenido 1</div><div>Contenido 2</div>"

# Cuantificador codicioso: .* coincide con todo desde el primer < hasta el último >
pattern_greedy = r"<.*>"
matches_greedy = re.findall(pattern_greedy, text_html)
print(f"Texto: '{text_html}'")
print(f"Patrón Codicioso: '{pattern_greedy}'")
print(f"Coincidencias (Greedy): {matches_greedy}") # Output: ['<div>Contenido 1</div><div>Contenido 2</div>']

# Cuantificador no codicioso: .*? coincide con la menor cantidad de caracteres posible
# hasta encontrar el siguiente >
pattern_lazy = r"<.*?>" # El ? después de * lo hace no codicioso
matches_lazy = re.findall(pattern_lazy, text_html)
print(f"Patrón No Codicioso: '{pattern_lazy}'")
print(f"Coincidencias (Lazy): {matches_lazy}") # Output: ['<div>', '</div>', '<div>', '</div>']

# Ejemplo con + vs +?
text_plus = "aaaaa"
pattern_plus_greedy = r"a+"
pattern_plus_lazy = r"a+?" # Intenta coincidir con la menor cantidad (1 'a')
matches_plus_greedy = re.findall(pattern_plus_greedy, text_plus)
matches_plus_lazy = re.findall(pattern_plus_lazy, text_plus)
print(f"\nTexto: '{text_plus}'")
print(f"Coincidencias (a+): {matches_plus_greedy}") # Output: ['aaaaa']
print(f"Coincidencias (a+?): {matches_plus_lazy}") # Output: ['a', 'a', 'a', 'a', 'a']

###
# EJERCICIOS (Cuantificadores)
# Pon en práctica lo aprendido sobre cuantificadores.
# Descomenta las soluciones para verificar tus respuestas.
###

print("\n--- EJERCICIOS ---")

# Ejercicio 1: Encontrar palabras con exactamente 4 letras
# Usa \b, \w y {n}.
print("\nEjercicio 1: Palabras de 4 letras")
texto_ej1 = "gato sol casa luna python elefante"
# patron_ej1 = r"\b\w{4}\b"
# solucion_ej1 = re.findall(patron_ej1, texto_ej1)
# print(f"Texto: '{texto_ej1}'")
# print(f"Palabras de 4 letras: {solucion_ej1}") # Esperado: ['gato', 'casa', 'luna']

# Ejercicio 2: Encontrar números con 3 o más dígitos
# Usa \b, \d y {n,}.
print("\nEjercicio 2: Números >= 3 dígitos")
texto_ej2 = "Ref: 12, ID: 345, Code: 6789, Val: 0, Num: 98765"
# patron_ej2 = r"\b\d{3,}\b"
# solucion_ej2 = re.findall(patron_ej2, texto_ej2)
# print(f"Texto: '{texto_ej2}'")
# print(f"Números >= 3 dígitos: {solucion_ej2}") # Esperado: ['345', '6789', '98765']

# Ejercicio 3: Encontrar etiquetas HTML simples (como <a> o <span>)
# Usa <, >, \w, + y el cuantificador no codicioso *?.
print("\nEjercicio 3: Etiquetas HTML simples")
texto_ej3 = "<p>Este es un <b>ejemplo</b> con <i>etiquetas</i>.</p>"
# patron_ej3 = r"<.*?>" # Encuentra cualquier cosa entre < y > (lazy)
# O más específico para etiquetas simples: r"<\w+>" o r"</?\w+>" para incluir cierre
# patron_ej3_especifico = r"</?\w+>"
# solucion_ej3 = re.findall(patron_ej3_especifico, texto_ej3)
# print(f"Texto: '{texto_ej3}'")
# print(f"Etiquetas encontradas: {solucion_ej3}") # Esperado: ['<p>', '<b>', '</b>', '<i>', '</i>', '</p>']

# Ejercicio 4: Validar formato de hora HH:MM (simple)
# Usa ^, $, \d, {n} o {n,m}. Considera horas de 00 a 23 y minutos de 00 a 59.
# Una versión simple podría ser \d{1,2}:\d{2}
print("\nEjercicio 4: Validar Hora HH:MM")
horas_ej4 = ["12:30", "9:05", "25:10", "1:65", "10:3", "00:00", "23:59"]
# patron_ej4 = r"^(?:[01]\d|2[0-3]):[0-5]\d$" # Patrón más preciso
# patron_ej4_simple = r"^\d{1,2}:\d{2}$" # Patrón simple (no valida rangos 0-23, 0-59)
# print(f"Probando horas: {horas_ej4}")
# for hora in horas_ej4:
#     if re.search(patron_ej4, hora):
#         print(f"  '{hora}' es válida.")
#     else:
#         print(f"  '{hora}' NO es válida.")
# Esperado (con patrón preciso): 12:30, 9:05, 00:00, 23:59 válidas.

# Ejercicio 5: Extraer precios en formato $XX.YY
# Usa \$, \d+, \. y {n}.
print("\nEjercicio 5: Extraer Precios $XX.YY")
texto_ej5 = "Los precios son $10.99, $5.00, $150.75 y $99."
# patron_ej5 = r"\$\d+\.\d{2}\b" # $ seguido de 1+ dígitos, punto literal, 2 dígitos
# solucion_ej5 = re.findall(patron_ej5, texto_ej5)
# print(f"Texto: '{texto_ej5}'")
# print(f"Precios encontrados: {solucion_ej5}") # Esperado: ['$10.99', '$5.00', '$150.75']

# Ejercicio 6: Encontrar secuencias de 2 a 4 vocales juntas
# Usa [], {n,m} y re.IGNORECASE.
print("\nEjercicio 6: Secuencias de 2-4 vocales")
texto_ej6 = "aeiou beauutiful idea caaos aaeeiioouu"
# patron_ej6 = r"[aeiou]{2,4}"
# solucion_ej6 = re.findall(patron_ej6, texto_ej6, flags=re.IGNORECASE)
# print(f"Texto: '{texto_ej6}'")
# print(f"Secuencias vocales (2-4): {solucion_ej6}") # Esperado: ['aeio', 'eauu', 'ea', 'aa', 'eeiioo', 'uu'] (revisar salida esperada según greedy)
# Revisión: 'aeiou' -> 'aeio' (greedy {2,4})
# 'beauutiful' -> 'eauu' (greedy {2,4})
# 'idea' -> 'ea' ({2,4})
# 'caaos' -> 'aa' ({2,4})
# 'aaeeiioouu' -> 'aaee' (greedy {2,4}), 'iioo' (greedy {2,4}), 'uu' ({2,4})
# Salida esperada: ['aeio', 'eauu', 'ea', 'aa', 'aaee', 'iioo', 'uu']
