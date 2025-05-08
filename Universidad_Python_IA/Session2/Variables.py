"""
========================================================
Guía Completa para Clase de Python
========================================================
Esta guía abarca desde los temas básicos hasta ejercicios prácticos,
incluyendo:
 15. Variables en Python con ChatGPT
 16. Ejemplo de Variables con Python
 17. Modificación de Variables
 18. Reglas para las Buenas Prácticas con Python y ChatGPT
 19. Ejemplo de Reglas de Buenas Prácticas
 20. Tipos de Datos en Python con ChatGPT
 21. Ejemplo de Tipos de Datos en Python
 22. Ejercicio Propuesto: Datos de un Producto
 23. Solución: Datos de un Producto
 24. Ejercicio Propuesto: Datos de un Vehículo
 25. Solución: Datos de un Vehículo
 26. Cadenas en Python
 27. Caracteres Especiales en Python
 28. Concatenación de Cadenas en Python
 29. Formato de Cadenas en Python
 30. Largo de una Cadena en Python
 31. Métodos Mayúsculas y Minúsculas en Python
 32. Manejo de Subcadenas en Python
 33. Capturar información por Consola en Python
 34. Ejercicio Propuesto - Preséntate con Python (Nueva versión)
 35. Solución Ejercicio - Preséntate con Python (Nueva versión)
 36. Ejercicio Propuesto - Receta de Cocina
 37. Solución Ejercicio - Receta de Cocina
 38. Ejercicio Propuesto - Generador de ID Único
 39. Solución Ejercicio - Generador de ID Único
 40. Ejercicio Propuesto - Generador de Nombres de Emails
 41. Solución Ejercicio - Generador de Nombres de Emails

Cada sección está comentada para facilitar la comprensión y servir de material de consulta.
"""

# ==========================================================================
# 15. Variables en Python con ChatGPT
# ==========================================================================
# En Python una variable es un nombre referencial a un objeto en memoria.
numero = 100                      # Tipo entero (int)
mensaje = "Hola, Python con ChatGPT"  # Tipo cadena (str)

print("15. Variable 'numero':", numero)
print("15. Variable 'mensaje':", mensaje)

# ==========================================================================
# 16. Ejemplo de Variables con Python
# ==========================================================================
# Ejemplo práctico de asignación de variables.
edad = 25                         # Asignación de un entero a "edad"
nombre = "María"                  # Asignación de una cadena a "nombre"
es_estudiante = True              # Variable booleana

# Se imprime cada variable con su descripción.
print("\n16. Ejemplo de Variables:")
print("Edad:", edad)
print("Nombre:", nombre)
print("Es estudiante:", es_estudiante)

# ==========================================================================
# 17. Modificación de Variables
# ==========================================================================
# Una variable puede ser modificada asignándole un nuevo valor, incluso de un tipo distinto.
valor = 10
print("\n17. Valor inicial:", valor)

valor = "Ahora soy una cadena"
print("17. Valor modificado:", valor)

# ==========================================================================
# 18. Reglas para las Buenas Prácticas con Python y ChatGPT
# ==========================================================================
# Buenas prácticas recomendadas (PEP8) incluyen:
# - Nombres descriptivos para variables y funciones.
# - Uso de 'snake_case' para nombres compuestos.
# - Código legible, con comentarios y líneas no muy extensas.
# - Separar la lógica en funciones para facilitar el mantenimiento.

# ==========================================================================
# 19. Ejemplo de Reglas de Buenas Prácticas
# ==========================================================================
def calcular_area_rectangulo(ancho: float, alto: float) -> float:
    """
    Calcula el área de un rectángulo.

    Parámetros:
        ancho (float): Medida horizontal del rectángulo.
        alto (float): Medida vertical del rectángulo.

    Retorna:
        float: El área calculada (ancho * alto).
    """
    return ancho * alto

# Ejemplo de uso
ancho_rect = 5.0
alto_rect = 3.0
area_rect = calcular_area_rectangulo(ancho_rect, alto_rect)
print("\n19. Área del rectángulo:", area_rect)

# ==========================================================================
# 20. Tipos de Datos en Python con ChatGPT
# ==========================================================================
# Python posee distintos tipos de datos básicos:
# - int: Enteros (ej. 42)
# - float: Decimales (ej. 3.14)
# - bool: Booleanos (True/False)
# - str: Cadenas de texto
# Además, estructuras compuestas como list, tuple, dict y set.
# ChatGPT puede proporcionar ejemplos y explicaciones en tiempo real sobre estos.

# ==========================================================================
# 21. Ejemplo de Tipos de Datos en Python
# ==========================================================================
# Ejemplos de distintos tipos de datos:
entero = 42                     # int
flotante = 3.1416               # float
booleano = False                # bool
cadena = "Python es versátil"   # str

lista = [1, 2, 3, 4]            # list (colección ordenada y mutable)
tupla = (5, 6, 7)               # tuple (inmutable)
diccionario = {"clave": "valor", "numero": 10}  # dict (pares clave-valor)
conjunto = {1, 2, 3}            # set (colección de elementos únicos)

print("\n21. Tipos de Datos:")
print("Entero:", entero)
print("Flotante:", flotante)
print("Booleano:", booleano)
print("Cadena:", cadena)
print("Lista:", lista)
print("Tupla:", tupla)
print("Diccionario:", diccionario)
print("Conjunto:", conjunto)

# ==========================================================================
# 22. Ejercicio Propuesto: Datos de un Producto
# ==========================================================================
# Crear una estructura (diccionario) para almacenar:
# - Nombre del producto
# - Precio
# - Stock disponible

# ==========================================================================
# 23. Solución: Datos de un Producto - Solución
# ==========================================================================
def crear_producto(nombre: str, precio: float, stock: int) -> dict:
    """
    Crea un diccionario que representa un producto.

    Parámetros:
        nombre (str): Nombre del producto.
        precio (float): Precio unitario.
        stock (int): Cantidad disponible.

    Retorna:
        dict: Diccionario con los datos del producto.
    """
    producto = {"nombre": nombre, "precio": precio, "stock": stock}
    return producto

# Ejemplo de uso
producto_ej = crear_producto("Laptop", 999.99, 15)
print("\n23. Producto creado:", producto_ej)

# ==========================================================================
# 24. Ejercicio Propuesto: Datos de un Vehículo
# ==========================================================================
# Crear una estructura para almacenar:
# - Marca
# - Modelo
# - Año de fabricación
# - Precio

# ==========================================================================
# 25. Solución: Datos de un Vehículo
# ==========================================================================
def crear_vehiculo(marca: str, modelo: str, anio: int, precio: float) -> dict:
    """
    Crea un diccionario que contiene la información de un vehículo.

    Parámetros:
        marca (str): Marca del vehículo.
        modelo (str): Modelo del vehículo.
        anio (int): Año de fabricación.
        precio (float): Precio del vehículo.

    Retorna:
        dict: Diccionario con los datos del vehículo.
    """
    vehiculo = {"marca": marca, "modelo": modelo, "anio": anio, "precio": precio}
    return vehiculo

# Ejemplo de uso
vehiculo_ej = crear_vehiculo("Toyota", "Corolla", 2020, 20000.00)
print("\n25. Vehículo creado:", vehiculo_ej)

# ==========================================================================
# 26. Cadenas en Python
# ==========================================================================
# Las cadenas (str) son secuencias inmutables de caracteres.
cadena_ej = "Esta es una cadena de ejemplo."
print("\n26. Cadena:", cadena_ej)

# ==========================================================================
# 27. Caracteres Especiales en Python
# ==========================================================================
# Para representar caracteres especiales se usan secuencias de escape.
texto_escapes = "Línea 1\nLínea 2\tcon tabulación y ' no hace falta  entre doble comillas, una barra invertida: \\ o \""
print("\n27. Texto con caracteres especiales:")
print(texto_escapes)

# ==========================================================================
# 28. Concatenación de Cadenas en Python
# ==========================================================================
# Se usa el operador '+' para concatenar.
saludo1 = "Hola"
saludo2 = "Mundo"
saludo_completo = saludo1 + " " + saludo2
print("\n28. Saludo' concatenado:", saludo_completo)
saludo3 = "Adios"
saludo4 = "Mundo"
saludo_completo2 = "".join([saludo3, " ", saludo4])
print("\n28. Saludo2' concatenado:", saludo_completo2)
saludo5 = "Otro "
saludo6 = "Mundo"
saludo_completo3 = saludo5.join([" ", saludo6])
print("\n28. Saludo3' concatenado:", saludo_completo3)

# ==========================================================================
# 29. Formato de Cadenas en Python
# ==========================================================================
# Se pueden formatear cadenas de varias maneras:
# 1. Usando el método format()
numero2 = 123
nombre2 = "numero"
formateo1 = "El {} valor es: {}".format(nombre2, numero2)
# 2. Usando f-strings (requiere Python 3.6+)
valor2= "valor"
valor_variable = 456
formateo2 = f"El {valor2} variable es: {valor_variable}"
print("\n29. Formateo de cadenas:")
print(formateo1)
print(formateo2)

# ==========================================================================
# 30. Largo de una Cadena en Python
# ==========================================================================
# Se utiliza la función len() para obtener el número de caracteres.
largo_cadena = len(cadena_ej)
print("\n30. Largo de la cadena:", largo_cadena)

# ==========================================================================
# 31. Métodos Mayúsculas y Minúsculas en Python
# ==========================================================================
# upper() y lower() convierten la cadena a mayúsculas o minúsculas, respectivamente.
mayusculas = cadena_ej.upper()
minusculas = cadena_ej.lower()
print("\n31. Cadena en mayúsculas:", mayusculas)
print("31. Cadena en minúsculas:", minusculas)

# ==========================================================================
# 32. Manejo de Subcadenas en Python
# ==========================================================================
# Se utiliza slicing para extraer una parte de la cadena.
# Sintaxis: cadena[inicio:fin] (fin no se incluye)
subcadena = cadena_ej[8:18]
# Sintaxis: cadena[inicio:] (hasta el final de la cadena)
subcadena2 = cadena_ej[8:]
print("\n32. Subcadena extraída:", subcadena)
print("\n32. Subcadena extraída:", subcadena2)

# ==========================================================================
# 33. Capturar información por Consola en Python
# ==========================================================================
# input() permite leer información introducida por el usuario.
nombre_usuario = input("\n33. Ingresa tu nombre: ")
print("33. ¡Bienvenido,", nombre_usuario + "!")
print(f"33. ¡Bienvenido, {nombre_usuario} !")

# Nota: Al usar input(), el valor capturado es de tipo cadena (str).

# ==========================================================================
# 34. Ejercicio Propuesto - Preséntate con Python (Nueva versión)
# ==========================================================================
# Se solicita que el usuario ingrese información personal (nombre, edad, ciudad)
# y se presente en un formato estructurado.

# ==========================================================================
# 35. Solución Ejercicio - Preséntate con Python (Nueva versión)
# ==========================================================================
def presentate():
    """
    Captura datos personales del usuario y muestra una presentación formateada.

    Se solicitan:
        - Nombre (str)
        - Edad (int)
        - Ciudad (str)

    No retorna valor, solo imprime la presentación.
    """
    nombre3 = input("34. Ingresa tu nombre: ")
    apellido2 = input("34. Ingresa tu apeliido: ")
    email = f"{nombre.lower()}.{apellido.lower()}@miemppresa.com"
    # Convertir la edad a entero después de capturarla como cadena.
    edad2 = int(input("34. Ingresa tu edad: "))
    ciudad = input("34. Ingresa tu ciudad: ")

    # Formateo de la presentación.
    presentacion = f"¡Hola, mi nombre es {nombre3} {apellido2}, mi email es {email} tengo {edad2} años y soy de {ciudad}."
    print("35. Presentación:\n", presentacion)

# Llamada a la función de presentación (se puede comentar para pruebas automáticas)
# presentate()

# ==========================================================================
# 36. Ejercicio Propuesto - Receta de Cocina
# ==========================================================================
# Se pide capturar datos de una receta:
# - Nombre del plato.
# - Lista de ingredientes (separados por comas).
# - Instrucciones de preparación.
#
# Luego, mostrar la receta de manera formateada.

# ==========================================================================
# 37. Solución Ejercicio - Receta de Cocina
# ==========================================================================
def crear_receta():
    """
    Captura los datos de una receta y retorna un diccionario con la información.

    Se solicitan:
        - Nombre del plato (str)
        - Ingredientes (str): Se espera una cadena separada por comas.
        - Tiempo = (int) Se espera Tiempo de preparaciónen minutos "
        - Dificultad = (str) ("Facil, Media, Alta")
        - instrucciones = (str) Se espera Instrucciones de preparación:

    Retorna:
        dict: Información de la receta.
    """
    nombre_plato = input("Nombre del plato: ")
    ingredientes = input("Ingresa los ingredientes separados por comas: ")
    tiempo = int(input("Tiempo de preparación: "))
    dificultad = input("Dificultad de preparación: ")
    instrucciones = input("Instrucciones de preparación: ")
    print(f"¡nombre es {nombre_plato}")
    print(f"¡ingredientes es {ingredientes}")
    print(f"¡tiempo es {tiempo}")
    print(f"¡dificultad es {dificultad}")

    # Separamos los ingredientes en una lista usando split() y eliminamos espacios sobrantes.
    lista_ingredientes = [ingrediente.strip() for ingrediente in ingredientes.split(',')]

    print(lista_ingredientes)

    receta = {
        "nombre": nombre_plato,
        "ingredientes": lista_ingredientes,
        "tiempo": tiempo,
        "dificultad": dificultad,
        "instrucciones": instrucciones
    }
    return receta


def mostrar_receta(receta: dict):
    """
    Muestra la receta formateada.

    Parámetros:
        receta (dict): Diccionario que contiene 'nombre', 'ingredientes' e 'instrucciones'.
    """
    print("\n37. Receta de Cocina")
    print("Plato:", receta.get("nombre"))
    print("Ingredientes:")
    for ing in receta.get("ingredientes", []):
        print(" -", ing)
    print("Instrucciones:", receta.get("instrucciones"))


# Ejemplo de uso:
receta_ej = crear_receta()
mostrar_receta(receta_ej)

# ==========================================================================
# 38. Ejercicio Propuesto - Generador de ID Único
# ==========================================================================
# Se solicita generar un identificador único utilizando el módulo uuid.
# El ejercicio consiste en implementar una función que retorne un ID único.

# ==========================================================================
# 39. Solución Ejercicio - Generador de ID Único
# ==========================================================================
import uuid  # Importa el módulo para generar IDs únicos


def generar_id_unico() -> str:
    """
    Genera un identificador único basado en uuid4.

    Retorna:
        str: Cadena única generada.
    """

    id_unico = uuid.uuid4()  # uuid4 genera un UUID aleatorio.
    return str(id_unico)


# Ejemplo de uso:
id_generado = generar_id_unico()
print("\n39. ID Único generado:", id_generado)

import random  # Módulo para generar números aleatorios


def generar_id_unico(nombre: str, apellido: str, anio_nacimiento: int) -> str:
    """
    Genera un ID único a partir de los datos del usuario y un número aleatorio.

    Parámetros:
    - nombre (str): Nombre del usuario.
    - apellido (str): Apellido del usuario.
    - anio_nacimiento (int): Año de nacimiento del usuario.

    Retorna:
    - str: ID único generado con el formato especificado.
    """

    # Tomamos las primeras dos letras del nombre y las convertimos en mayúsculas
    parte_nombre = nombre[:2].upper()

    # Tomamos las primeras dos letras del apellido y las convertimos en mayúsculas
    parte_apellido = apellido[:2].upper()

    # Extraemos los dos últimos dígitos del año de nacimiento (ej. 1995 → '95')
    parte_anio = str(anio_nacimiento)[-2:]

    # Generamos un número aleatorio de 4 dígitos entre 1000 y 9999
    valor_aleatorio = str(random.randint(1000, 9999))

    # Concatenamos todas las partes para formar el ID único
    id_unico = parte_nombre + parte_apellido + parte_anio + valor_aleatorio

    return id_unico


# =========================
# Ejemplo de uso
# =========================
nombre = "Juan"
apellido = "Perez"
anio_nacimiento = 1995

id_generado = generar_id_unico(nombre, apellido, anio_nacimiento)

# Imprimimos el resultado como lo requiere el ejercicio
print("Resultado ID Único:", id_generado)


# ==========================================================================
# 40. Ejercicio Propuesto - Generador de Nombres de Emails
# ==========================================================================
# Se pide que, dado un nombre completo, se genere una dirección de correo electrónico
# en un formato predefinido. Por ejemplo, a partir de "Juan Pérez" se puede generar
# "juan.perez@ejemplo.com".

# ==========================================================================
# 41. Solución Ejercicio - Generador de Nombres de Emails
# ==========================================================================
def generar_email(nombre_completo: str, dominio: str = "ejemplo.com") -> str:
    """
    Genera un email a partir de un nombre completo.

    Parámetros:
        nombre_completo (str): Nombre y apellido(s) del usuario.
        dominio (str): Dominio del email. Valor por defecto "ejemplo.com".

    Retorna:
        str: Dirección de email en formato 'nombre.apellido@dominio'
    """
    # Convertir a minúsculas y eliminar espacios extra.
    nombre_procesado = nombre_completo.strip().lower()
    # Reemplazar espacios internos por puntos.
    nombre_email = nombre_procesado.replace(" ", ".")
    email = f"{nombre_email}@{dominio}"
    return email


# Ejemplo de uso:
nombre_usuario_email = input("\n40. Ingresa tu nombre completo para generar tu email: ")
email_generado = generar_email(nombre_usuario_email)
print("41. Email generado:", email_generado)

# ==========================================================================
# Fin de la Guía Completa
# ==========================================================================
# Esta guía ha sido diseñada para cubrir de forma práctica y detallada
# los temas abordados en clase, incluyendo ejemplos y ejercicios resueltos.
# Se recomienda revisar cada sección y realizar los ejercicios de manera
# interactiva para reforzar el aprendizaje.