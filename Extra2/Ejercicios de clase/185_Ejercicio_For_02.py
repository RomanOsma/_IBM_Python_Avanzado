

# Escribe un programa que solicite al usuario un número entero positivo y luego 
# imprima la tabla de multiplicar de ese número del 1 al 10.


numero = int(input("Introduce un número entero positivo: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")