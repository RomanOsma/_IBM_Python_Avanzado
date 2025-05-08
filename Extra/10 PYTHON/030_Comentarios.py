
# Los comentarios son anotaciones que pondremos en nuestro código que el programa no va a tener en cuenta.
# Existen dos tipos de comentarios:

# Esto es un comentario de una línea

"""Esto es un comentario
que me va a ocupar
varias líneas"""

# En el caso de las funciones podemos meter docstrings:

def suma(a, b):
    """Esta función suma dos números
    :param a: Primer número
    :param b: Segundo número
    :return: La suma de a y b
    """
    return a + b

suma(1,5)