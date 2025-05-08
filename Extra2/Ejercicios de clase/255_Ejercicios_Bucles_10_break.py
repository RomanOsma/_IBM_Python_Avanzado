




# Escribe un programa que pida al usuario que ingrese números. 
# El programa debe seguir pidiendo números hasta que el usuario ingrese el número 0. 
# En ese momento, el programa debe detenerse y mostrar la suma de todos los números ingresados.


suma = 0

while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break  # Salir del bucle si el número es 0
    suma += numero

print(f"La suma de todos los números ingresados es: {suma}")



