# Definimos la clase Coche
class Coche:

    def __init__(self, marca, modelo, color):
        self.marca = marca  # Atributo publico
        self._modelo = modelo  # Atributo protegido
        self.__color = color  # Atributo privado

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}''')


# Programa principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # En este momento no deberias acceder directamente
    # a los atributos protegidos o privados
    coche1.marca = 'Toyota 2'
    coche1._modelo = 'Yaris 2'  # Esto no es una buena practica
    coche1.__color = 'Azul 2'  # Ignoro la modificacion en un atributo privado
    coche1._Coche__color = 'Azul 3'  # Es una mala practica
    coche1.conducir()