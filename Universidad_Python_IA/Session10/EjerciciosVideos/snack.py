class Snack:
    contador_snacks = 0

    def __init__(self, nombre='', precio=0.0):
        Snack.contador_snacks += 1
        self.id_snack = Snack.contador_snacks
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return (f'Snack: id_snack = {self.id_snack}, nombre = {self.nombre}, '
                f'precio = {self.precio}')

    def escribir_snack(self):
        return f'{self.id_snack},{self.nombre},{self.precio}'
