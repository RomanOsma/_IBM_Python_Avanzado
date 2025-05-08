# Definicion de la clase
class Persona:

    # Constructor __init__ (dunder - double underscore)
    def __init__(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido


    def mostrar_contacto(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')


# Creacion de Objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona('Layla', 'Acosta') # Se llama de manera automatica el constructor
    persona1.mostrar_contacto()

    # Creamos un segundo objeto
    print()
    persona2 = Persona('Ian', 'Sanchez')
    persona2.mostrar_contacto()