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
        print(f'Dir. mem self: {id(self)}')
        print(f'Dir. mem hex self: {hex(id(self))}')


# Creacion de Objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona('Layla', 'Acosta') # Se llama de manera automatica el constructor
    persona1.mostrar_contacto()
    print(f'Dir. mem persona1: {id(persona1)}')
    print(f'Dir. mem hex persona1: {hex(id(persona1))}')

    # Creamos un segundo objeto
    print()
    persona2 = Persona('Ian', 'Sanchez')
    persona2.mostrar_contacto()
    print(f'Dir. mem persona2: {id(persona2)}')
    print(f'Dir. mem hex persona2: {hex(id(persona2))}')

