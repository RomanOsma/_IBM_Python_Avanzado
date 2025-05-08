
# Escribe una función llamada calcular_area_rectangulo que tome la base 
# y la altura de un rectángulo como parámetros y devuelva su área. 
# Luego, escribe otra función llamada calcular_area_circulo que tome 
# el radio de un círculo y devuelva su área (usa math.pi para el valor de π).


import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Llamadas a las funciones
print(calcular_area_rectangulo(5, 10))  # 50
print(calcular_area_circulo(3))         # Aproximadamente 28.27