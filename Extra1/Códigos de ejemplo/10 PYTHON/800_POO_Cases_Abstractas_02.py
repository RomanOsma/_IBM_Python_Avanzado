
from abc import ABC, abstractmethod

# Definir una clase abstracta
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass  # Este método debe ser implementado por las subclases

# Subclase que hereda de la clase abstracta
class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

# Subclase que hereda de la clase abstracta
class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

# Crear instancias de las subclases
perro = Perro()
gato = Gato()

print(perro.hacer_sonido())  # Salida: ¡Guau!
print(gato.hacer_sonido())   # Salida: ¡Miau!

# ------------------------------
# Si una subclase no implementa todos los métodos abstractos de la clase base, 
# Python lanzará un error al intentar instanciar la subclase. Por ejemplo:

# class Pajaro(Animal):
#     pass

# # Esto lanzará un error porque no se implementó el método abstracto
# pajaro = Pajaro()  # TypeError: Can't instantiate abstract class Pajaro with abstract method hacer_sonido