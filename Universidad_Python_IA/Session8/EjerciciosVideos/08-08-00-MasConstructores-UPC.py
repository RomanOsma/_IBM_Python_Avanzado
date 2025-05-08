# Flexibilidad en la creacion de objetos 
# Python toma la definición de constructor que se declaró al final 

class Aritmetica:

    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado resta: {resultado}')

    # Agregar los metodos de multiplcacion y division

# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo Clase Aritmetica ***')
    aritmetica1 = Aritmetica(5, 7)
    print('Primer objeto')
    aritmetica1.sumar()
    aritmetica1.restar()
    # Segundo objeto
    aritmetica2 = Aritmetica(12, 16)
    print('Segundo Objeto')
    aritmetica2.sumar()
    aritmetica2.restar()
    # Tercer objeto
    print('Tercer Objeto')
    aritmetica3 = Aritmetica(4)
    aritmetica3.operando2 = 7
    aritmetica3.sumar()
    # Cuarto objeto
    print('Cuarto Objeto')
    artmetica4 = Aritmetica()
    artmetica4.operando1 = 2
    artmetica4.operando2 = 6
    artmetica4.restar()
    # Quinto objeto
    artmetica5 = Aritmetica(operando1=8, operando2=5)