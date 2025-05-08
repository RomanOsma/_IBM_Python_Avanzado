class Aritmetica:

    def __init__(self, operando1=None, operando2=None):
        self._operando1 = operando1
        self._operando2 = operando2

    def sumar(self):
        resultado = self._operando1 + self._operando2
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self._operando1 - self._operando2
        print(f'Resultado resta: {resultado}')

    # Agregar los metodos de multiplcacion y division

    # Metodos get/set para cada atributo
    def get_operando1(self):
        return self._operando1

    def set_operando1(self, operando1):
        self._operando1 = operando1

    def get_operando2(self):
        return self._operando2

    def set_operando2(self, operando2):
        self._operando2 = operando2


# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo Clase Aritmetica ***')
    print('Objeto Aritmetica 1')
    aritmetica1 = Aritmetica(5, 7)
    print(f'Valor operando1 del objeto aritmetica1: {aritmetica1.get_operando1()}')
    print(f'Valor operando2 del objeto aritmetica1: {aritmetica1.get_operando2()}')
    aritmetica1.sumar()
    aritmetica1.restar()
    print('\nObjeto Aritmetica 2')
    aritmetica2 = Aritmetica(4, 9)
    print(f'Valor operando1 del objeto aritmetica2: {aritmetica2.get_operando1()}')
    print(f'Valor operando2 del objeto aritmetica2: {aritmetica2.get_operando2()}')
    aritmetica2.sumar()
    aritmetica2.restar()
    aritmetica2.set_operando1(10)
    aritmetica2.set_operando2(15)
    print(f'Valor operando1 del objeto aritmetica2: {aritmetica2.get_operando1()}')
    print(f'Valor operando2 del objeto aritmetica2: {aritmetica2.get_operando2()}')
    aritmetica2.sumar()
    aritmetica2.restar()

