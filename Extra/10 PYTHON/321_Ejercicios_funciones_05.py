

# Escribe una función llamada es_primo que tome un número como parámetro y 
# devuelva True si es primo y False si no lo es. Luego, escribe otra función 
# llamada lista_primos que tome un número n y devuelva una lista con todos 
# los números primos menores que n.


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def lista_primos(n):
    return [x for x in range(2, n) if es_primo(x)]

# Llamadas a las funciones
print(es_primo(17))  # True
print(lista_primos(20))  # [2, 3, 5, 7, 11, 13, 17, 19]