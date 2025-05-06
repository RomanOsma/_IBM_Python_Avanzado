class Animal:
    def hacer_sonido(self):
        print('Hago un pitido...')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

print('*** Ejemplo Polimorfismo ***')
print('Clase Padre Animal: ')
animal1 = Animal()
animal1.hacer_sonido()
# Definir un objeto de la clase perro
print('\nClase Hija Perro: ')
perro1 = Perro()
# Polimorfismo (se manda a llamar el metodo segun el objeto que se esta ejecutando)
perro1.hacer_sonido()
# Definir un objeto de la clase gato
print('\nClase Hija Gato:')
gato1 = Gato()
gato1.hacer_sonido()