




# Escribe un programa que pida al usuario que ingrese números. 
# Si el número ingresado es negativo, el programa debe ignorarlo y pedir otro número. 
# Si el número es positivo, el programa debe sumarlo. 
# El programa debe detenerse cuando el usuario ingrese 0 y mostrar la suma de todos 
# los números positivos ingresados.

suma = 0

while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break  # Salir del bucle si el número es 0
    if numero < 0:
        print("Número negativo ignorado.")
        continue  # Saltar a la siguiente iteración si el número es negativo
    suma += numero

print(f"La suma de todos los números positivos ingresados es: {suma}")



