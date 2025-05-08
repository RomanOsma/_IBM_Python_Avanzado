# Definicion de la clase
class Persona:

    def inicializar_persona(self, nombre, apellido):
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
    persona1 = Persona()  # Crea un objeto vacio en memoria
    persona1.inicializar_persona('Layla', 'Acosta')
    persona1.mostrar_contacto()

    # Creamos un segundo objeto
    print()
    persona2 = Persona()
    persona2.inicializar_persona('Ian', 'Sanchez')
    persona2.mostrar_contacto()