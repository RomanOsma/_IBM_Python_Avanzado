
# Solicitar la edad y el dinero al usuario
edad = int(input("Introduce tu edad: "))
dinero = float(input("Introduce la cantidad de dinero que tienes: "))

# Verificar las condiciones para comprar el coche
if edad >= 18 and dinero >= 20000:
    print("¡Felicidades! Puedes comprar el coche.")
elif edad >= 18 and dinero < 20000:
    print("Tienes la edad suficiente, pero no tienes suficiente dinero para comprar el coche.")
elif edad < 18 and dinero >= 20000:
    print("Tienes suficiente dinero, pero no tienes la edad suficiente para comprar el coche.")
else:
    print("No tienes ni la edad suficiente ni el dinero necesario para comprar el coche.")
