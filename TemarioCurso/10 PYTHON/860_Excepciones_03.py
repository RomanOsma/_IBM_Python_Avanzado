try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero.")
except ValueError:
    print("¡Error! Debes introducir un número válido.")
else:
    print("La operación se realizó con éxito.")
finally:
    print("Fin del bloque try-except.")

# Si pones 0, se lanza ZeroDivisionError.

# Si pones "abc", se lanza ValueError.

# else se ejecuta si no hay error.

# finally siempre se ejecuta.