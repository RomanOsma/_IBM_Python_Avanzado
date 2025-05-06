"""
========================================================
CLASE: Variables en Python
========================================================

Objetivo:
    - Comprender qué es una variable en Python.
    - Conocer la dinámica del tipado y asignación de valores.
    - Aprender normas de nomenclatura de variables.
    - Ver ejemplos prácticos de variables de diferentes tipos.

Contexto:
    En Python, una variable es un nombre de referencia que apunta a un objeto. Debido a que Python es un
    lenguaje de tipado dinámico, no es necesario declarar el tipo de la variable explícitamente. El intérprete
    lo determina en tiempo de ejecución basado en el valor que se le asigne.

Estructura del archivo:
    1. Asignación de variables básicas (números, cadenas, booleanos).
    2. Variables compuestas: listas, tuplas, diccionarios.
    3. Reglas y convenciones de nomenclatura.
    4. Ejemplos de conversión de tipos (casting).
    5. Comentarios sobre funciones y parámetros en ejemplos prácticos.
"""

# ========================================================
# 1. Asignación de Variables Básicas
# ========================================================

# En Python, la asignación se realiza mediante el operador '='.
# No es necesario declarar el tipo, ya que se infiere del valor asignado.

# Variables numéricas:
numero_entero = 10  # Entero
numero_flotante = 3.14  # Número de punto flotante (float)

# Variables de cadena:
mensaje = "Hola, Python"  # Cadena de texto (string)

# Variable booleana:
es_valido = True  # Valor booleano (True o False)

# Ejemplo de impresión:
print("Número entero:", numero_entero)  # Imprime: Número entero: 10
print("Número flotante:", numero_flotante)  # Imprime: Número flotante: 3.14
print("Mensaje:", mensaje)  # Imprime: Mensaje: Hola, Python
print("Es válido:", es_valido)  # Imprime: Es válido: True

# Comentarios:
# - En el ejemplo anterior, se asignan distintos tipos de datos a variables.
# - La función print() se utiliza para mostrar los valores en la salida estándar.
# - Los comentarios comienzan con el símbolo '#' y ayudan a documentar el código.

# ========================================================
# 2. Variables Compuestas
# ========================================================

# Listas:
# Una lista es una colección ordenada y mutable de elementos.
lista_numeros = [1, 2, 3, 4, 5]
lista_cadenas = ["uno", "dos", "tres"]

# Tuplas:
# Una tupla es similar a una lista pero es inmutable.
tupla_ejemplo = (10, 20, 30)

# Diccionarios:
# Un diccionario es una colección de pares clave-valor.
diccionario = {
    "nombre": "Angel",
    "edad": 40,
    "profesion": "Vago"
}

# Ejemplo de impresión de estructuras compuestas:
print("\nLista de números:", lista_numeros)
print("\nLista de cadenas:", lista_cadenas)
print("Tupla:", tupla_ejemplo)
print("Diccionario:", diccionario)

# Comentarios:
# - Las listas permiten añadir, modificar y eliminar elementos.
# - Las tuplas, una vez definidas, no pueden modificarse; son útiles para datos constantes.
# - Los diccionarios se utilizan cuando se requiere asociar claves con valores para un acceso rápido.

# ========================================================
# 3. Reglas y Convenciones de Nomenclatura de Variables
# ========================================================

# Reglas básicas:
# 1. El nombre de la variable debe comenzar con una letra (a-z, A-Z) o el carácter '_'.
# 2. El nombre solo puede contener letras, números y guiones bajos.
# 3. Python es sensible a mayúsculas y minúsculas, es decir, 'Variable' y 'variable' son diferentes.

# Ejemplos:
nombre_estudiante = "Ana"
edad_estudiante = 22

# Comentarios:
# - Se recomienda utilizar nombres descriptivos para facilitar la comprensión del código.
# - El estilo 'snake_case' es el más común en Python para nombrar variables y funciones.

# ========================================================
# 4. Conversión de Tipos (Casting)
# ========================================================

# Es posible convertir explícitamente de un tipo a otro:
numero_str = "123"  # Cadena que representa un número

# Conversión de cadena a entero:
numero_convertido = int(numero_str)
print("\nNúmero convertido a entero:", numero_convertido)  # Imprime: Número convertido a entero: 123

# Conversión de entero a cadena:
entero_a_cadena = str(numero_entero)
print("Número entero convertido a cadena:", entero_a_cadena)


# Comentarios:
# - Las funciones int(), str(), float(), etc., son usadas para convertir tipos.
# - Es importante asegurarse de que la cadena represente un número válido antes de convertirla, para evitar errores.

# ========================================================
# 5. Ejemplo Práctico: Uso en Funciones
# ========================================================

def saludar(nombre: str, saludo: str = "Hola") -> str:
    """
    Función para saludar a una persona.

    Parámetros:
        nombre (str): El nombre de la persona a saludar.
        saludo (str): La palabra de saludo a usar. Valor por defecto es "Hola".

    Retorna:
        str: Una cadena con el saludo personalizado.
    """
    # Concatenación de cadenas para formar el saludo completo.
    mensaje_saludo = f"{saludo}, {nombre}!"
    return mensaje_saludo


# Uso de la función:
mensaje_personalizado = saludar("Carlos")
print("\nEjemplo de función saludar:", mensaje_personalizado)  # Imprime: Hola, Carlos!

# Comentarios:
# - Se utiliza la anotación de tipos (type hints) para indicar qué tipo de datos se espera que sean los parámetros y el valor de retorno.
# - El parámetro 'saludo' tiene un valor por defecto, lo que significa que es opcional al llamar a la función.
# - La función utiliza la sintaxis f-string para interpolar variables en la cadena.

# ========================================================
# Conclusiones
# ========================================================

# - Las variables en Python son herramientas fundamentales para almacenar y manipular datos.
# - Su tipado dinámico permite una gran flexibilidad, pero implica estar atento a los cambios en el tipo de datos.
# - Es crucial seguir las buenas prácticas de nomenclatura y comentar adecuadamente el código para mejorar la mantenibilidad y legibilidad.

# Fin del archivo de ejemplo sobre variables en Python.
