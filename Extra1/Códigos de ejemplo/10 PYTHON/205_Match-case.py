
# En Python, no existe una estructura de switch-case como en otros lenguajes de programación 
# (por ejemplo, en C, Java o JavaScript). Sin embargo, a partir de Python 3.10, se introdujo 
# una estructura similar llamada match-case, que permite realizar comparaciones de patrones 
# de manera similar a un switch-case.

def operacion(opcion):
    match opcion:
        case 1:
            return "Opción 1 seleccionada"
        case 2:
            return "Opción 2 seleccionada"
        case 3:
            return "Opción 3 seleccionada"
        case _:
            return "Opción no válida"

print(operacion(2))  # Salida: "Opción 2 seleccionada"
print(operacion(4))  # Salida: "Opción no válida"