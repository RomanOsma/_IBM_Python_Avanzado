


class ClaseA:
    def metodo_a(self):
        return "Método de ClaseA"

class ClaseB:
    def metodo_a(self):
        return "Método de ClaseB"

# Clase que hereda de ClaseA y ClaseB
class ClaseC(ClaseA, ClaseB):
    def metodo_c(self):
        return "Método de ClaseC"

# Crear una instancia de ClaseC
objeto = ClaseC()

# Acceder a métodos de las clases base
print(objeto.metodo_a())  # Salida: Método de ClaseA

print(objeto.metodo_c())  # Salida: Método de ClaseC