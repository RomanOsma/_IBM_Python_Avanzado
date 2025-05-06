#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PYTHON AVANZADO - MATERIAL DIDÁCTICO
====================================

Este archivo contiene ejemplos y explicaciones de conceptos avanzados de Python.
Está diseñado para servir como material de estudio y referencia.

Temas cubiertos:
- Comprensión de listas, diccionarios y conjuntos
- Función zip
- Manejo de cadenas
- Funciones lambda
- Map, filter y reduce
- Ordenamiento con sorted
- Generadores e iteradores
- Expresiones generadoras
- Decoradores
- Funciones sum y next
- Manejo de excepciones

Autor: [Tu Nombre]
Fecha: Abril 2025
"""

# Funciones auxiliares para mejorar la presentación de los ejemplos
def titulo(texto):
    """Muestra un título formateado para las secciones."""
    ancho = 80
    print("\n" + "=" * ancho)
    print(f"{texto.center(ancho)}")
    print("=" * ancho + "\n")


def subtitulo(texto):
    """Muestra un subtítulo formateado para las subsecciones."""
    print(f"\n{texto}")
    print("-" * len(texto))


def separador():
    """Muestra una línea separadora."""
    print("\n" + "-" * 40 + "\n")


def ejecutar_ejemplo(funcion):
    """
    Decorador que ejecuta una función de ejemplo y muestra su nombre.

    Args:
        funcion: La función a ejecutar.

    Returns:
        El resultado de la función.
    """

    def wrapper(*args, **kwargs):
        subtitulo(f"Ejemplo: {funcion.__name__.replace('_', ' ').title()}")
        print(f"Descripción: {funcion.__doc__.strip()}")
        print("\nEjecución:")
        resultado = funcion(*args, **kwargs)
        return resultado

    return wrapper


# ==============================================================================
#                          1. COMPRENSIÓN DE LISTAS
# ==============================================================================

def seccion_comprension_listas():
    """
    Explora la comprensión de listas, una forma elegante y concisa de crear
    listas basadas en secuencias o iterables existentes.

    Sintaxis básica:
    [expresion for elemento in iterable if condicion]
    """
    titulo("1. COMPRENSIÓN DE LISTAS")

    print("""La comprensión de listas es una característica poderosa que permite crear
listas de manera concisa y legible. Es una alternativa a los bucles tradicionales
para crear o transformar listas.
""")

    @ejecutar_ejemplo
    def ejemplo_numeros_pares():
        """Filtrar los números pares del 1 al 10 usando diferentes métodos."""
        numeros = range(1, 11)

        # Método 1: Usando un bucle for tradicional
        print("Método 1: Bucle for tradicional")
        numeros_pares = []
        for numero in numeros:
            if numero % 2 == 0:
                numeros_pares.append(numero)
        print(f"Números pares del 1 al 10: {numeros_pares}")

        # Método 2: Usando comprensión de listas
        print("\nMétodo 2: Comprensión de listas")
        numeros_pares = [numero for numero in numeros if numero % 2 == 0]
        print(f"Números pares del 1 al 10: {numeros_pares}")

        # Comparación de rendimiento (para grandes conjuntos de datos)
        print("\nLa comprensión de listas suele ser más rápida y utiliza menos memoria")
        print("para grandes conjuntos de datos.")

    ejemplo_numeros_pares()

    @ejecutar_ejemplo
    def ejemplo_transformaciones():
        """Transformar elementos de una lista usando comprensión de listas."""
        # Calcular el cuadrado de cada número del 1 al 5
        numeros = [1, 2, 3, 4, 5]

        cuadrados = [n ** 2 for n in numeros]
        print(f"Cuadrados: {cuadrados}")

        # Convertir temperaturas de Celsius a Fahrenheit
        celsius = [0, 10, 20, 30, 40]
        fahrenheit = [(9 / 5) * c + 32 for c in celsius]
        print(f"Celsius: {celsius}")
        print(f"Fahrenheit: {fahrenheit}")

    ejemplo_transformaciones()

    @ejecutar_ejemplo
    def ejemplo_comprension_anidada():
        """Usar comprensión de listas anidada para crear matrices."""
        # Crear una matriz 3x3 (lista de listas)
        matriz = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
        print("Matriz 3x3:")
        for fila in matriz:
            print(fila)

        # Aplanar una matriz (convertir una matriz a una lista simple)
        matriz_aplanada = [elemento for fila in matriz for elemento in fila]
        print(f"\nMatriz aplanada: {matriz_aplanada}")

    ejemplo_comprension_anidada()

    @ejecutar_ejemplo
    def ejemplo_comprension_diccionarios_conjuntos():
        """Comprensión de diccionarios y conjuntos."""
        # Comprensión de diccionarios
        numeros = range(1, 6)
        cuadrados_dict = {n: n ** 2 for n in numeros}
        print(f"Diccionario de cuadrados: {cuadrados_dict}")

        # Filtrar diccionarios
        diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        pares_dict = {k: v for k, v in diccionario.items() if v % 2 == 0}
        print(f"Diccionario filtrado (solo valores pares): {pares_dict}")

        # Comprensión de conjuntos
        letras = "abracadabra"
        letras_unicas = {letra for letra in letras}
        print(f"Letras únicas en 'abracadabra': {letras_unicas}")

    ejemplo_comprension_diccionarios_conjuntos()

    # Ejercicios para practicar
    subtitulo("Ejercicios para practicar")

    print("""1. Crear una comprensión de lista que genere los números impares del 1 al 20.
2. Crear una comprensión de lista que convierta una lista de palabras a mayúsculas.
3. Crear una comprensión de diccionario que genere un diccionario donde las claves
   sean números del 1 al 10 y los valores sean sus cuadrados, pero solo para 
   los números impares.
""")

    subtitulo("Soluciones")

    # Solución 1
    impares = [n for n in range(1, 21) if n % 2 != 0]
    print(f"1. Números impares del 1 al 20: {impares}")

    # Solución 2
    palabras = ["python", "es", "genial"]
    mayusculas = [palabra.upper() for palabra in palabras]
    print(f"2. Palabras en mayúsculas: {mayusculas}")

    # Solución 3
    cuadrados_impares = {n: n ** 2 for n in range(1, 11) if n % 2 != 0}
    print(f"3. Cuadrados de números impares: {cuadrados_impares}")


# ==============================================================================
#                              2. FUNCIÓN ZIP
# ==============================================================================

def seccion_funcion_zip():
    """
    Explora la función zip que permite combinar múltiples iterables element-wise.
    """
    titulo("2. FUNCIÓN ZIP")

    print("""La función zip() toma múltiples iterables y devuelve un iterador de tuplas,
donde cada tupla contiene los elementos correspondientes de los iterables de entrada.
Es útil para trabajar con múltiples secuencias en paralelo.
""")

    @ejecutar_ejemplo
    def ejemplo_basico_zip():
        """Ejemplo básico del uso de la función zip."""
        nombres = ['Juan', 'María', 'Pedro', 'Ana']
        edades = [30, 25, 35, 28]

        # Combinar nombres y edades
        personas = zip(nombres, edades)

        # zip devuelve un iterador, convertir a lista para visualizarlo
        personas_lista = list(personas)
        print(f"Lista de tuplas: {personas_lista}")

        # Iterar sobre el resultado de zip
        print("\nIterando sobre el resultado de zip:")
        for nombre, edad in zip(nombres, edades):
            print(f"{nombre} tiene {edad} años")

    ejemplo_basico_zip()

    @ejecutar_ejemplo
    def ejemplo_longitudes_diferentes():
        """Manejar iterables de diferentes longitudes con zip."""
        nombres = ['Juan', 'María', 'Pedro', 'Ana']
        edades = [30, 25, 35]  # Uno menos que nombres
        ciudades = ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao']  # Uno más que nombres

        # zip se detiene cuando se agota el iterable más corto
        combinados = list(zip(nombres, edades, ciudades))
        print(f"Resultado con longitudes diferentes: {combinados}")
        print("Nota: zip se detiene al agotar el iterable más corto (edades)")

        # Para incluir todos los elementos, se puede usar zip_longest del módulo itertools
        from itertools import zip_longest
        combinados_completos = list(zip_longest(nombres, edades, ciudades, fillvalue='N/A'))
        print(f"\nUsando zip_longest con valor de relleno 'N/A': {combinados_completos}")

    ejemplo_longitudes_diferentes()

    @ejecutar_ejemplo
    def ejemplo_desempaquetar_zip():
        """Usar zip para desempaquetar listas."""
        # Tenemos una lista de tuplas o pares
        pares = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

        # Desempaquetar en dos listas separadas
        numeros, letras = zip(*pares)
        print(f"Pares originales: {pares}")
        print(f"Números extraídos: {numeros}")
        print(f"Letras extraídas: {letras}")

    ejemplo_desempaquetar_zip()

    @ejecutar_ejemplo
    def ejemplo_zip_diccionarios():
        """Usar zip para crear diccionarios."""
        claves = ['nombre', 'edad', 'ciudad']
        valores = ['Ana', 28, 'Madrid']

        # Crear un diccionario a partir de dos listas
        persona = dict(zip(claves, valores))
        print(f"Diccionario creado: {persona}")

        # Actualizar múltiples valores de un diccionario
        nuevos_valores = ['Ana García', 29, 'Barcelona']
        persona.update(zip(claves, nuevos_valores))
        print(f"Diccionario actualizado: {persona}")

    ejemplo_zip_diccionarios()

    # Ejercicios para practicar
    subtitulo("Ejercicios para practicar")

    print("""1. Tienes dos listas: 'productos' y 'precios'. Crea un diccionario donde los productos
   sean las claves y los precios sean los valores.
2. Dadas tres listas de la misma longitud, usa zip y una comprensión de listas para
   obtener una lista con la suma de los elementos correspondientes.
3. Tienes una lista de tuplas donde cada tupla contiene un nombre y una puntuación.
   Usa zip para separar esta lista en dos listas: una de nombres y otra de puntuaciones.
""")

    subtitulo("Soluciones")

    # Solución 1
    productos = ['manzana', 'plátano', 'naranja']
    precios = [1.2, 0.9, 1.5]
    diccionario_productos = dict(zip(productos, precios))
    print(f"1. Diccionario de productos: {diccionario_productos}")

    # Solución 2
    lista1 = [1, 2, 3, 4]
    lista2 = [5, 6, 7, 8]
    lista3 = [9, 10, 11, 12]
    sumas = [a + b + c for a, b, c in zip(lista1, lista2, lista3)]
    print(f"2. Suma de elementos correspondientes: {sumas}")

    # Solución 3
    puntuaciones = [('Ana', 95), ('Juan', 88), ('María', 92)]
    nombres, puntos = zip(*puntuaciones)
    print(f"3. Nombres: {nombres}")
    print(f"   Puntuaciones: {puntos}")


# ==============================================================================
#                           3. MANEJO DE CADENAS
# ==============================================================================

def seccion_manejo_cadenas():
    """
    Explora las operaciones más comunes y útiles para manipular cadenas de texto.
    """
    titulo("3. MANEJO DE CADENAS")

    print("""Python ofrece numerosos métodos para trabajar con cadenas de texto.
Estos métodos permiten realizar operaciones como dividir, buscar, reemplazar,
limpiar y formatear texto de manera eficiente.
""")

    @ejecutar_ejemplo
    def ejemplo_split_join():
        """Dividir y unir cadenas con split() y join()."""
        # Dividir una cadena con split()
        cadena = "Python es un lenguaje de programación"
        palabras = cadena.split()
        print(f"Cadena original: '{cadena}'")
        print(f"Después de split(): {palabras}")

        # Dividir por un carácter específico
        fecha = "2025-04-19"
        componentes = fecha.split('-')
        print(f"\nFecha original: '{fecha}'")
        print(f"Componentes después de split('-'): {componentes}")

        # Unir cadenas con join()
        print("\nUnir con join():")
        palabras = ['Python', 'es', 'genial']
        cadena_unida = ' '.join(palabras)
        print(f"Lista original: {palabras}")
        print(f"Después de ' '.join(): '{cadena_unida}'")

        # Unir con un separador diferente
        separador = ' -> '
        ruta = separador.join(['inicio', 'medio', 'fin'])
        print(f"\nUniendo con '{separador}': '{ruta}'")

    ejemplo_split_join()

    @ejecutar_ejemplo
    def ejemplo_busqueda_reemplazo():
        """Buscar y reemplazar texto en cadenas."""
        cadena = "Python es un lenguaje de programación y Python es fácil de aprender"

        # Buscar con find() - devuelve el índice de la primera ocurrencia o -1 si no encuentra
        posicion = cadena.find('Python')
        posicion_segunda = cadena.find('Python', posicion + 1)  # Buscar a partir de la posición siguiente

        print(f"Cadena: '{cadena}'")
        print(f"Posición de 'Python': {posicion}")
        print(f"Posición de la segunda 'Python': {posicion_segunda}")

        # Buscar con in - devuelve un booleano
        contiene_python = 'Python' in cadena
        contiene_java = 'Java' in cadena
        print(f"\n¿Contiene 'Python'?: {contiene_python}")
        print(f"¿Contiene 'Java'?: {contiene_java}")

        # Contar ocurrencias
        ocurrencias = cadena.count('Python')
        print(f"\nOcurrencias de 'Python': {ocurrencias}")

        # Reemplazar con replace()
        nueva_cadena = cadena.replace('Python', 'Ruby')
        print(f"\nDespués de reemplazar 'Python' con 'Ruby':")
        print(f"'{nueva_cadena}'")

        # Reemplazar un número limitado de ocurrencias
        nueva_cadena = cadena.replace('Python', 'Ruby', 1)  # Solo la primera ocurrencia
        print(f"\nDespués de reemplazar solo la primera ocurrencia:")
        print(f"'{nueva_cadena}'")

    ejemplo_busqueda_reemplazo()

    @ejecutar_ejemplo
    def ejemplo_limpieza_formato():
        """Limpiar y formatear cadenas."""
        # Eliminar espacios en blanco con strip(), lstrip() y rstrip()
        cadena = "   Python   "
        print(f"Cadena original: '{cadena}'")
        print(f"Con strip(): '{cadena.strip()}'")
        print(f"Con lstrip(): '{cadena.lstrip()}'")
        print(f"Con rstrip(): '{cadena.rstrip()}'")

        # Eliminar caracteres específicos
        cadena = "...Python..."
        print(f"\nCadena original: '{cadena}'")
        print(f"strip('.'): '{cadena.strip('.')}'")

        # Cambio de mayúsculas/minúsculas
        cadena = "Python Es Genial"
        print(f"\nCadena original: '{cadena}'")
        print(f"lower(): '{cadena.lower()}'")
        print(f"upper(): '{cadena.upper()}'")
        print(f"capitalize(): '{cadena.capitalize()}'")
        print(f"title(): '{cadena.title()}'")
        print(f"swapcase(): '{cadena.swapcase()}'")

        # Verificar tipo de contenido
        print("\nVerificación de contenido:")
        print(f"'123'.isdigit(): {'123'.isdigit()}")
        print(f"'abc'.isalpha(): {'abc'.isalpha()}")
        print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
        print(f"'PYTHON'.isupper(): {'PYTHON'.isupper()}")
        print(f"'python'.islower(): {'python'.islower()}")

    ejemplo_limpieza_formato()

    @ejecutar_ejemplo
    def ejemplo_operaciones_adicionales():
        """Operaciones adicionales con cadenas."""
        # Multiplicación de cadenas
        cadena = "Python "
        repetida = cadena * 3
        print(f"'{cadena}' * 3 = '{repetida}'")

        # Justificación de texto
        texto = "Python"
        print(f"\nJustificación del texto '{texto}':")
        print(f"center(20, '*'): '{texto.center(20, '*')}'")
        print(f"ljust(20, '*'): '{texto.ljust(20, '*')}'")
        print(f"rjust(20, '*'): '{texto.rjust(20, '*')}'")

        # Formateo de cadenas
        nombre = "María"
        edad = 28

        # Usando format()
        plantilla = "Hola, me llamo {} y tengo {} años"
        mensaje = plantilla.format(nombre, edad)
        print(f"\nUsando format(): '{mensaje}'")

        # Usando f-strings (disponible desde Python 3.6)
        mensaje = f"Hola, me llamo {nombre} y tengo {edad} años"
        print(f"Usando f-strings: '{mensaje}'")

    ejemplo_operaciones_adicionales()

    # Ejercicios para practicar
    subtitulo("Ejercicios para practicar")

    print("""1. Tienes una cadena con nombres separados por comas. Conviértela en una
   lista de nombres, elimina los espacios en blanco sobrantes y ordénalos alfabéticamente.
2. Reemplaza todas las vocales de una cadena por asteriscos (*).
3. Tienes una lista de direcciones de correo electrónico. Crea una nueva lista que
   contenga solo los nombres de usuario (la parte antes del @).
""")

    subtitulo("Soluciones")

    # Solución 1
    nombres_texto = "Juan, María, Pedro,  Ana ,  Carlos"
    nombres_lista = [nombre.strip() for nombre in nombres_texto.split(',')]
    nombres_ordenados = sorted(nombres_lista)
    print(f"1. Nombres originales: '{nombres_texto}'")
    print(f"   Nombres ordenados: {nombres_ordenados}")

    # Solución 2
    texto = "Python es un lenguaje de programación"
    vocales = 'aeiouAEIOU'
    resultado = ''.join(['*' if c in vocales else c for c in texto])
    print(f"2. Texto original: '{texto}'")
    print(f"   Reemplazando vocales: '{resultado}'")

    # Solución 3
    emails = ['usuario1@example.com', 'nombre.apellido@empresa.org', 'otro@sitio.net']
    usuarios = [email.split('@')[0] for email in emails]
    print(f"3. Emails: {emails}")
    print(f"   Usuarios: {usuarios}")


# ==============================================================================
#                            4. FUNCIONES LAMBDA
# ==============================================================================

def seccion_funciones_lambda():
    """
    Explora las funciones lambda (anónimas) y sus aplicaciones.
    """
    titulo("4. FUNCIONES LAMBDA")

    print("""Las funciones lambda, también conocidas como funciones anónimas, son pequeñas
funciones sin nombre definidas con la palabra clave lambda. Son útiles cuando
necesitamos funciones simples de una sola expresión, especialmente como argumentos
para funciones de orden superior como map(), filter() y sorted().

Sintaxis:
lambda argumentos: expresión
""")

    @ejecutar_ejemplo
    def ejemplo_lambda_basico():
        """Ejemplos básicos de funciones lambda."""
        # Función normal vs lambda
        print("Función normal vs lambda:")

        # Definición normal de una función
        def cuadrado(x):
            return x ** 2

        # Equivalente con lambda
        cuadrado_lambda = lambda x: x ** 2

        # Probando ambas funciones
        valor = 5
        print(f"cuadrado({valor}) = {cuadrado(valor)}")
        print(f"cuadrado_lambda({valor}) = {cuadrado_lambda(valor)}")

        # Lambda con múltiples argumentos
        print("\nLambda con múltiples argumentos:")
        suma = lambda x, y: x + y
        print(f"suma(3, 4) = {suma(3, 4)}")

        # Lambda con condicionales
        print("\nLambda con condicionales:")
        valor_absoluto = lambda x: x if x >= 0 else -x
        print(f"valor_absoluto(5) = {valor_absoluto(5)}")
        print(f"valor_absoluto(-5) = {valor_absoluto(-5)}")

    ejemplo_lambda_basico()

    @ejecutar_ejemplo
    def ejemplo_lambda_aplicaciones():
        """Aplicaciones comunes de las funciones lambda."""
        # Lambda como argumento de otras funciones
        numeros = [1, 2, 3, 4, 5]

        # Usar lambda con map() para aplicar una función a cada elemento
        cuadrados = list(map(lambda x: x ** 2, numeros))
        print(f"Cuadrados usando map con lambda: {cuadrados}")

        # Usar lambda con filter() para filtrar elementos
        pares = list(filter(lambda x: x % 2 == 0, numeros))
        print(f"Números pares usando filter con lambda: {pares}")

        # Usar lambda con sorted() para ordenamiento personalizado
        estudiantes = [
            {'nombre': 'Ana', 'nota': 85},
            {'nombre': 'Juan', 'nota': 92},
            {'nombre': 'María', 'nota': 78}
        ]

        ordenados_por_nota = sorted(estudiantes, key=lambda est: est['nota'], reverse=True)
        print("\nEstudiantes ordenados por nota (descendente):")
        for est in ordenados_por_nota:
            print(f"{est['nombre']}: {est['nota']}")

    ejemplo_lambda_aplicaciones()

    @ejecutar_ejemplo
    def ejemplo_lambda_vs_alternativas():
        """Comparación de lambdas con alternativas."""
        # Lambda vs comprensión de listas
        numeros = [1, 2, 3, 4, 5]

        print("Diferentes formas de calcular cuadrados:")

        # Usando lambda con map
        cuadrados_map = list(map(lambda x: x ** 2, numeros))
        print(f"Con map y lambda: {cuadrados_map}")

        # Usando comprensión de listas
        cuadrados_comprension = [x ** 2 for x in numeros]
        print(f"Con comprensión de listas: {cuadrados_comprension}")

        # Usando un bucle for tradicional
        cuadrados_for = []
        for x in numeros:
            cuadrados_for.append(x ** 2)
        print(f"Con bucle for: {cuadrados_for}")

        print("\nVentajas y desventajas:")
        print("- Lambda con map: conciso, funcional, pero menos legible para operaciones complejas")
        print("- Comprensión de listas: muy legible, idiomático en Python")
        print("- Bucle for: más verboso pero más flexible para lógica compleja")

    ejemplo_lambda_vs_alternativas()

    # Ejercicios para practicar
    subtitulo("Ejercicios para practicar")

    print("""1. Escribe una función lambda que verifique si un número es divisible por 3 y por 5.
2. Tienes una lista de cadenas. Utiliza map() con una función lambda para obtener
   la longitud de cada cadena.
3. Dada una lista de diccionarios con las claves 'nombre' y 'edad', usa sorted() con
   una función lambda para ordenarlos primero por edad y luego por nombre.
""")

    subtitulo("Soluciones")

    # Solución 1
    es_divisible = lambda n: n % 3 == 0 and n % 5 == 0
    print(f"1. ¿15 es divisible por 3 y 5?: {es_divisible(15)}")
    print(f"   ¿10 es divisible por 3 y 5?: {es_divisible(10)}")

    # Solución 2
    palabras = ["Python", "es", "un", "lenguaje", "genial"]
    longitudes = list(map(lambda s: len(s), palabras))
    print(f"2. Palabras: {palabras}")
    print(f"   Longitudes: {longitudes}")

    # Solución 3
    personas = [
        {'nombre': 'Ana', 'edad': 30},
        {'nombre': 'Carlos', 'edad': 25},
        {'nombre': 'Berta', 'edad': 30},
        {'nombre': 'Daniel', 'edad': 25}
    ]
    ordenadas = sorted(personas, key=lambda p: (p['edad'], p['nombre']))
    print("3. Personas ordenadas por edad y nombre:")
    for p in ordenadas:
        print(f"   {p['nombre']}, {p['edad']} años")


# ==============================================================================
#                           5. MAP, FILTER Y REDUCE
# ==============================================================================

def seccion_map_filter_reduce():
    """
    Explora las funciones de programación funcional map(), filter() y reduce().
    """
    titulo("5. MAP, FILTER Y REDUCE")

    print("""Las funciones map(), filter() y reduce() son parte del paradigma de programación
funcional en Python. Permiten procesar colecciones de datos de manera declarativa,
sin necesidad de escribir bucles explícitos.
""")

    @ejecutar_ejemplo
    def ejemplo_map():
        """Uso de la función map() para transformar datos."""
        # map() aplica una función a cada elemento de un iterable
        numeros = [1, 2, 3, 4, 5]

        # Calcular el cuadrado de cada número
        cuadrados = map(lambda x: x ** 2, numeros)
        print(f"Números originales: {numeros}")
        print(f"Cuadrados con map(): {list(cuadrados)}")

        # map() con múltiples iterables
        numeros1 = [1, 2, 3]
        numeros2 = [10, 20, 30]

        # Sumar elementos correspondientes
        sumas = map(lambda x, y: x + y, numeros1, numeros2)
        print(f"\nSuma elemento a elemento: {list(sumas)}")

        # Usando una función definida previamente con map()
        def fahrenheit_a_celsius(f):
            return (f - 32) * 5 / 9

        temperaturas_f = [32, 68, 86, 104, 212]
        temperaturas_c = list(map(fahrenheit_a_celsius, temperaturas_f))

        print("\nConversión de temperaturas de Fahrenheit a Celsius:")
        print(f"Fahrenheit: {temperaturas_f}")
        print(f"Celsius: {[round(temp, 1) for temp in temperaturas_c]}")

    ejemplo_map()

    @ejecutar_ejemplo
    def ejemplo_filter():
        """Uso de la función filter() para filtrar datos."""
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Filtrar números pares
        pares = filter(lambda x: x % 2 == 0, numeros)
        print(f"Números originales: {numeros}")
        print(f"Números pares: {list(pares)}")

        # Filtrar con función personalizada
        def es_primo(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        primos = list(filter(es_primo, numeros))
        print(f"\nNúmeros primos: {primos}")

    ejemplo_filter()

    @ejecutar_ejemplo
    def ejemplo_reduce():
        """Uso de reduce() para operaciones acumulativas."""
        from functools import reduce

        numeros = [1, 2, 3, 4, 5]

        # Suma acumulativa
        suma_total = reduce(lambda x, y: x + y, numeros)
        print(f"Suma de {numeros}: {suma_total}")

        # Encontrar el máximo valor
        maximo = reduce(lambda x, y: x if x > y else y, numeros)
        print(f"Máximo valor: {maximo}")

        # Concatenar cadenas
        palabras = ["Python", " ", "es", " ", "genial"]
        concatenacion = reduce(lambda x, y: x + y, palabras)
        print(f"Concatenación: '{concatenacion}'")

    ejemplo_reduce()

    # Ejercicios para practicar
    subtitulo("Ejercicios para practicar")

    print("""1. Usa map() para convertir una lista de temperaturas en Celsius a Fahrenheit.
2. Usa filter() para obtener las palabras con más de 5 letras de una lista.
3. Usa reduce() para calcular el producto de todos los números en una lista.
""")

    subtitulo("Soluciones")

    # Solución 1
    celsius = [0, 10, 20, 30, 40]
    fahrenheit = list(map(lambda c: (9 / 5) * c + 32, celsius))
    print(f"1. Celsius: {celsius} -> Fahrenheit: {fahrenheit}")

    # Solución 2
    palabras = ["programación", "python", "lambda", "reduce", "funcional"]
    filtradas = list(filter(lambda s: len(s) > 5, palabras))
    print(f"2. Palabras con más de 5 letras: {filtradas}")

    # Solución 3
    from functools import reduce
    numeros = [2, 3, 4, 5]
    producto = reduce(lambda x, y: x * y, numeros)
    print(f"3. Producto de {numeros}: {producto}")


# ==============================================================================
#                       6. ORDENAMIENTO CON SORTED
# ==============================================================================

def seccion_ordenamiento_sorted():
    """
    Explora el uso avanzado de la función sorted() para ordenar estructuras complejas.
    """
    titulo("6. ORDENAMIENTO CON SORTED")

    print("""La función sorted() permite ordenar iterables de manera flexible usando el parámetro key.
Es especialmente útil para ordenar estructuras complejas como listas de diccionarios.
""")

    @ejecutar_ejemplo
    def ejemplo_ordenamiento_basico():
        """Ordenar listas y diccionarios con sorted()."""
        # Ordenamiento básico de listas
        empleados = ['Juan', 'Pedro', 'María']
        empleados_ordenados = sorted(empleados, reverse=True)
        print(f"Orden descendente: {empleados_ordenados}")

        # Ordenamiento de diccionarios por clave
        empleados_dict = [
            {'nombre': 'Juan', 'salario': 3000},
            {'nombre': 'María', 'salario': 2500},
            {'nombre': 'Pedro', 'salario': 3500}
        ]
        orden_por_salario = sorted(empleados_dict, key=lambda x: x['salario'])
        print(f"\nOrden por salario: {orden_por_salario}")

        # Ordenamiento múltiple
        orden_compuesto = sorted(empleados_dict, key=lambda x: (x['salario'], x['nombre']))
        print(f"\nOrden compuesto (salario y nombre): {orden_compuesto}")

    ejemplo_ordenamiento_basico()

    # Ejercicios para practicar
    subtitulo("Ejercicios para practicar")
    print("""1. Ordena una lista de tuplas (nombre, edad) primero por edad y luego alfabéticamente.
2. Ordena una lista de cadenas ignorando mayúsculas/minúsculas.
3. Ordena un diccionario por sus valores en lugar de sus claves.""")

    subtitulo("Soluciones")
    # Solución 1
    personas = [('Ana', 25), ('Carlos', 19), ('Berta', 25)]
    ordenados = sorted(personas, key=lambda x: (x[1], x[0]))
    print(f"1. {ordenados}")

    # Solución 2
    palabras = ["Python", "azul", "Árbol", "banana"]
    orden_insensible = sorted(palabras, key=lambda s: s.lower())
    print(f"2. {orden_insensible}")

    # Solución 3
    diccionario = {'manzana': 3, 'banana': 1, 'naranja': 2}
    orden_por_valor = dict(sorted(diccionario.items(), key=lambda item: item[1]))
    print(f"3. {orden_por_valor}")


# ==============================================================================
#                       7. GENERADORES E ITERADORES
# ==============================================================================

def seccion_generadores_iteradores():
    """
    Explica cómo crear generadores y trabajar con iteradores para manejar flujos de datos eficientes.
    """
    titulo("7. GENERADORES E ITERADORES")

    print("""Los generadores producen valores bajo demanda usando yield, optimizando el uso de memoria.
Los iteradores permiten recorrer secuencias elemento a elemento.
""")

    @ejecutar_ejemplo
    def ejemplo_generador_funcion():
        """Generador que produce números hasta un máximo."""

        def generador(maximo):
            contador = 0
            while contador < maximo:
                yield contador
                contador += 1

        print("Generador de números del 0 al 4:")
        for num in generador(5):
            print(num, end=" ")

    ejemplo_generador_funcion()

    @ejecutar_ejemplo
    def ejemplo_expresion_generadora():
        """Expresión generadora para cuadrados de pares."""
        generador = (x ** 2 for x in range(10) if x % 2 == 0)
        print("\nCuadrados de números pares:")
        for num in generador:
            print(num, end=" ")

    ejemplo_expresion_generadora()

    # Ejercicios para practicar
    subtitulo("Ejercicios para practicar")
    print("""1. Crea un generador que produzca la secuencia Fibonacci.
2. Usa una expresión generadora para obtener números divisibles por 7 entre 0-100.
3. Implementa un iterador personalizado para una lista.""")

    subtitulo("Soluciones")

    # Solución 1
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fib = fibonacci()
    print("1. Primeros 10 Fibonacci:", [next(fib) for _ in range(10)])

    # Solución 2
    divisibles_7 = (x for x in range(101) if x % 7 == 0)
    print("2. Divisibles por 7:", list(divisibles_7))

    # Solución 3
    class MiIterador:
        def __init__(self, datos):
            self.datos = datos
            self.indice = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.indice < len(self.datos):
                elemento = self.datos[self.indice]
                self.indice += 1
                return elemento
            raise StopIteration

    print("3. Iterador personalizado:", list(MiIterador([1, 2, 3])))


# ==============================================================================
#                            8. DECORADORES
# ==============================================================================

def seccion_decoradores():
    """
    Explica cómo crear y usar decoradores para modificar comportamiento de funciones.
    """
    titulo("8. DECORADORES")

    print("""Los decoradores son funciones que envuelven otras funciones para añadir funcionalidad.
Se usan con @nombre_decorador antes de la definición de la función.
""")

    @ejecutar_ejemplo
    def ejemplo_decorador_basico():
        """Decorador que mide tiempo de ejecución."""
        import time

        def medir_tiempo(func):
            def wrapper(*args, **kwargs):
                inicio = time.time()
                resultado = func(*args, **kwargs)
                fin = time.time()
                print(f"Tiempo de ejecución: {fin - inicio:.4f}s")
                return resultado

            return wrapper

        @medir_tiempo
        def operacion_larga():
            time.sleep(2)
            print("Operación completada")

        operacion_larga()

    ejemplo_decorador_basico()

    # Ejercicios para practicar
    subtitulo("Ejercicios para practicar")
    print("""1. Crea un decorador que convierta el resultado de una función a mayúsculas.
2. Implementa un decorador con argumentos para repetir una función N veces.
3. Crea un decorador que valide los tipos de los argumentos.""")

    subtitulo("Soluciones")

    # Solución 1
    def mayusculas(func):
        def wrapper(*args):
            return func(*args).upper()

        return wrapper

    @mayusculas
    def saludo(nombre):
        return f"Hola {nombre}"

    print(f"1. {saludo('Ana')}")

    # Solución 2
    def repetir(n_veces):
        def decorador(func):
            def wrapper(*args):
                for _ in range(n_veces):
                    func(*args)

            return wrapper

        return decorador

    @repetir(3)
    def decir_hola():
        print("Hola")

    print("2. ", end="")
    decir_hola()

    # Solución 3
    def validar_tipos(*tipos):
        def decorador(func):
            def wrapper(*args):
                for i, (arg, tipo) in enumerate(zip(args, tipos)):
                    if not isinstance(arg, tipo):
                        raise TypeError(f"Arg {i} debe ser {tipo.__name__}")
                return func(*args)

            return wrapper

        return decorador

    @validar_tipos(int, int)
    def suma(a, b):
        return a + b

    print(f"3. Suma válida: {suma(5, 3)}")


# ==============================================================================
#                       9. MANEJO DE EXCEPCIONES
# ==============================================================================

def seccion_manejo_excepciones():
    """
    Cubre técnicas avanzadas para manejar y crear excepciones personalizadas.
    """
    titulo("9. MANEJO DE EXCEPCIONES")

    print("""El manejo de excepciones permite controlar errores durante la ejecución.
Se usan bloques try-except-finally y se pueden crear excepciones personalizadas.
""")

    @ejecutar_ejemplo
    def ejemplo_excepciones_personalizadas():
        """Excepción personalizada para validar edades."""

        class EdadInvalidaError(Exception):
            def __init__(self, edad):
                super().__init__(f"Edad {edad} no está entre 18-99")

        def validar_edad(edad):
            if not 18 <= edad <= 99:
                raise EdadInvalidaError(edad)
            print("Edad válida")

        try:
            validar_edad(150)
        except EdadInvalidaError as e:
            print(f"Error: {e}")

    ejemplo_excepciones_personalizadas()

    # Ejercicios para practicar
    subtitulo("Ejercicios para practicar")
    print("""1. Maneja una división por cero con try-except.
2. Crea una excepción para números negativos en raíz cuadrada.
3. Implementa un bloque try-except-finally para abrir/cerrar archivos.""")

    subtitulo("Soluciones")
    # Solución 1
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("1. No se puede dividir por cero")

    # Solución 2
    class RaizNegativaError(Exception):
        pass

    def raiz_cuadrada(n):
        if n < 0:
            raise RaizNegativaError
        return n ** 0.5

    try:
        raiz_cuadrada(-4)
    except RaizNegativaError:
        print("2. No existe raíz de números negativos")

    # Solución 3
    try:
        archivo = open("inexistente.txt", "r")
    except FileNotFoundError:
        print("3. Archivo no encontrado")
    finally:
        print("   Bloque finally ejecutado")


# ==============================================================================
#                     EJECUTAR TODAS LAS SECCIONES
# ==============================================================================
if __name__ == "__main__":
    seccion_comprension_listas()
    seccion_funcion_zip()
    seccion_manejo_cadenas()
    seccion_funciones_lambda()
    seccion_map_filter_reduce()
    seccion_ordenamiento_sorted()
    seccion_generadores_iteradores()
    seccion_decoradores()
    seccion_manejo_excepciones()
