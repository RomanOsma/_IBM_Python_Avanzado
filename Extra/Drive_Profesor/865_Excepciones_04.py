
# Ejemplo 2: Acceso a una lista fuera de rango

lista = [1, 2, 3]

try:
    print(lista[5])
except IndexError as e:
    print(f"Error: {e}")



# Ejemplo 3: Uso de múltiples excepciones

try:
    num = int(input("Número: "))
    print(10 / num)
except (ValueError, ZeroDivisionError) as e:
    print("Ocurrió un error:", e)    



# Ejemplo 4: Bucle hasta que el usuario lo haga bien

while True:
    try:
        edad = int(input("Introduce tu edad: "))
        break
    except ValueError:
        print("Eso no es un número. Inténtalo otra vez.")



