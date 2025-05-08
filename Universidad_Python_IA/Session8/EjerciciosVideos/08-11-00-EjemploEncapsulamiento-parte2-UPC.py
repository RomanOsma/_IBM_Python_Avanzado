# Definimos la clase Coche
class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color


# Programa principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # Utilizar el concepto de encapsulamiento (get/set)
    coche1.set_marca('Toyota 2')
    coche1.set_modelo('Yaris 2')
    coche1.set_color('Azul 2')
    coche1.conducir()
    coche1.marca = 'Toyota 3' # Por el dinamismo de python se agrego un nuevo atributo
    print(f'Atributos del coche1: {coche1.__dict__}')

    # Crea un segundo objeto
    coche2 = Coche('Chevrolet', 'Trax', 'Negro')
    print(f'Atributos coche2: {coche2.__dict__}')
