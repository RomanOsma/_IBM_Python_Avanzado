class Persona:

    atributo_clase = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia


# Programa principal
if __name__ == '__main__':
    print('*** Atributos de Clase ***')
    print(f'Atributo de Clase = {Persona.atributo_clase}')
    # Modificamos el atributo de clase
    Persona.atributo_clase = 10
    print(f'Atributo de Clase = {Persona.atributo_clase}')

    # Creamos un objeto
    persona1 = Persona(15)
    print(f'Atributo de Clase desde persona1: {persona1.atributo_clase}')
    print(f'Atributo de instancia desde persona1: {persona1.atributo_instancia}')

    # Creamos un objeto
    print()
    persona2 = Persona(30)
    print(f'Atributo de Clase desde persona2: {persona2.atributo_clase}')
    print(f'Atributo de instancia desde persona2: {persona2.atributo_instancia}')


